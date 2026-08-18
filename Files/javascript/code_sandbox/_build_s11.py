"""S11: JS Arrays through JS Array const."""
from __future__ import annotations

import json

from _gen_lib import S, build_and_snap


def nf_script(snippet: str) -> str:
    """Compile snippet with new Function so parse-time SyntaxError can be caught."""
    return f"""      let msg;
      try {{
        new Function({json.dumps(snippet)})();
        msg = "ran without error";
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText =
        msg + "\\n" + "(caught via new Function; a raw <script> would fail to parse)";"""


def catch_script(setup: str, attempt: str) -> str:
    """Run setup, then try/catch a runtime TypeError and print name + message."""
    setup_lines = "\n".join(("      " + line) if line else "" for line in setup.split("\n"))
    return f"""{setup_lines}
      let msg;
      try {{
        {attempt}
        msg = "ran without error";
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText = msg;"""


CARS = 'const cars = ["Saab", "Volvo", "BMW"];'
FR4 = 'const fruits = ["Banana", "Orange", "Apple", "Mango"];'
FR3 = 'const fruits = ["Banana", "Orange", "Apple"];'
FR5 = 'const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];'
PTS = "const points = [40, 100, 1, 5, 25, 10];"
NUMS = "const numbers = [45, 4, 9, 16, 25];"
N_FIND = "const numbers = [4, 9, 16, 25, 29];"
MONTHS = 'const months = ["Jan", "Feb", "Mar", "Apr"];'
CARS_OBJ = """const cars = [
  {type:"Volvo", year:2016},
  {type:"Saab", year:2001},
  {type:"BMW", year:2010}
];"""


# ---------------------------------------------------------------------------
# 11.1 JS Arrays
# ---------------------------------------------------------------------------

ARRAYS = [
    S(
        "literal-cars",
        'const cars = ["Saab", "Volvo", "BMW"]',
        [
            "An **array literal** is a comma-separated list inside **`[]`**.",
            "Declare arrays with **`const`**. Indexes start at **0**.",
        ],
        CARS,
        [("cars", "JSON.stringify(cars)")],
        'cars is **["Saab","Volvo","BMW"]**. The hero Tryit and the “Creating an Array” Tryit are the same snippet — shown once.',
    ),
    S(
        "literal-multiline",
        "Array literal spanning lines",
        [
            "Spaces and line breaks do not matter. A declaration may span **multiple lines**.",
        ],
        'const cars = [\n  "Saab",\n  "Volvo",\n  "BMW"\n];',
        [("cars", "JSON.stringify(cars)")],
        'Same value: **["Saab","Volvo","BMW"]**.',
    ),
    S(
        "empty-then-assign",
        "Empty array, then assign by index",
        [
            "Create **`[]`**, then set `cars[0]`, `cars[1]`, `cars[2]`.",
        ],
        'const cars = [];\ncars[0] = "Saab";\ncars[1] = "Volvo";\ncars[2] = "BMW";',
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "new-array-cars",
        'new Array("Saab", "Volvo", "BMW")',
        [
            "`new Array(...)` with **several arguments** builds the same list as a literal.",
            "Prefer **`[]`** for simplicity, readability, and speed.",
        ],
        'const cars = new Array("Saab", "Volvo", "BMW");',
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]** — same as the literal.',
    ),
    S(
        "access-index-0",
        "Access cars[0]",
        [
            "Read an element by **index**. **`[0]`** is the first element.",
        ],
        CARS + '\nlet car = cars[0];',
        [("car", "car"), ("cars", "JSON.stringify(cars)")],
        'car is **"Saab"**.',
    ),
    S(
        "change-element",
        'cars[0] = "Opel"',
        [
            "Assignment to an index **replaces** that element. `const` still allows this.",
        ],
        CARS + '\ncars[0] = "Opel";',
        [("cars", "JSON.stringify(cars)")],
        '**["Opel","Volvo","BMW"]**.',
    ),
    S(
        "tostring",
        "fruits.toString()",
        [
            "`toString()` joins elements with **commas** (no spaces).",
        ],
        FR4 + "\nlet text = fruits.toString();",
        [("text", "text")],
        "**Banana,Orange,Apple,Mango**.",
    ),
    S(
        "display-array-name",
        "Display the array by name",
        [
            "Referring to the array name stringifies it the same way as `toString()`.",
        ],
        CARS + "\nlet text = String(cars);",
        [("text", "text")],
        "**Saab,Volvo,BMW**.",
    ),
    S(
        "json-stringify",
        "JSON.stringify(cars)",
        [
            "`JSON.stringify` shows **quotes** and **brackets** — useful for nested data.",
        ],
        CARS + "\nlet text = JSON.stringify(cars);",
        [("text", "text")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "array-numbered-person",
        "Array: person[0] is John",
        [
            "Arrays are objects, but you access **elements by number**.",
        ],
        'const person = ["John", "Doe", 46];',
        [("person", "JSON.stringify(person)"), ("person[0]", "person[0]")],
        '**["John","Doe",46]**. `person[0]` is **"John"**.',
    ),
    S(
        "object-named-person",
        "Object: person.firstName is John",
        [
            "Objects use **names** for members, not numbered indexes.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:46};',
        [("person", "JSON.stringify(person)"), ("person.firstName", "person.firstName")],
        '`firstName` is **"John"**.',
    ),
    S(
        "mixed-objects-functions",
        "Array elements can be objects, functions, arrays",
        [
            "No Tryit on the page — arrays are heterogeneous.",
            "This demo stores a **function reference**, a **function**, and a **nested array**.",
        ],
        'function myFunction() {\n  return "hello";\n}\nconst myCars = ["Saab", "Volvo"];\nconst myArray = [];\nmyArray[0] = Date.now;\nmyArray[1] = myFunction;\nmyArray[2] = myCars;',
        [
            ("typeof myArray[0]", "typeof myArray[0]"),
            ("myArray[1]()", "myArray[1]()"),
            ("myArray[2]", "JSON.stringify(myArray[2])"),
        ],
        '`Date.now` is a **function**. `myArray[1]()` is **"hello"**. Nested cars are **["Saab","Volvo"]**.',
    ),
    S(
        "length",
        "fruits.length",
        [
            "`length` is the number of elements. It is **one more** than the highest index.",
        ],
        FR4 + "\nlet length = fruits.length;",
        [("length", "length")],
        "**4**.",
    ),
    S(
        "first-element",
        "First element fruits[0]",
        [
            "The first element is always index **0**.",
        ],
        FR4 + "\nlet fruit = fruits[0];",
        [("fruit", "fruit")],
        "**Banana**.",
    ),
    S(
        "last-element",
        "Last element fruits[fruits.length - 1]",
        [
            "`length - 1` is the last valid index.",
        ],
        FR4 + "\nlet fruit = fruits[fruits.length - 1];",
        [("fruit", "fruit")],
        "**Mango**.",
    ),
    S(
        "for-loop",
        "for loop over fruits",
        [
            "A classic **`for`** from `0` to `length - 1` visits every index.",
        ],
        FR4 + """
let fLen = fruits.length;
let text = "";
for (let i = 0; i < fLen; i++) {
  text += fruits[i] + (i < fLen - 1 ? ", " : "");
}""",
        [("text", "text")],
        "**Banana, Orange, Apple, Mango**.",
    ),
    S(
        "foreach",
        "fruits.forEach(myFunction)",
        [
            "`forEach` calls a function once per element.",
        ],
        FR4 + """
let text = "";
fruits.forEach(myFunction);
function myFunction(value) {
  text += value + " ";
}""",
        [("text", "text")],
        "**Banana Orange Apple Mango** (trailing space from the callback).",
    ),
    S(
        "push",
        'fruits.push("Lemon")',
        [
            "`push` appends at the **end**.",
        ],
        FR3 + '\nfruits.push("Lemon");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Apple","Lemon"]**.',
    ),
    S(
        "add-via-length",
        "fruits[fruits.length] = Lemon",
        [
            "Writing at `fruits.length` also **appends**.",
        ],
        FR3 + '\nfruits[fruits.length] = "Lemon";',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Apple","Lemon"]**.',
    ),
    S(
        "holes-warning",
        "WARNING fruits[6] = Lemon creates holes",
        [
            "A **high index** grows `length` and leaves **empty slots** in between.",
            "`JSON.stringify` prints holes as **`null`**. `3 in fruits` is still **false**.",
        ],
        FR3 + '\nfruits[6] = "Lemon";',
        [
            ("fruits", "JSON.stringify(fruits)"),
            ("fruits.length", "fruits.length"),
            ("fruits[3]", "fruits[3]"),
            ("3 in fruits", "3 in fruits"),
        ],
        'JSON **["Banana","Orange","Apple",null,null,null,"Lemon"]**. length **7**. `fruits[3]` is **undefined**. `3 in fruits` is **false**.',
    ),
    S(
        "numbered-indexes",
        "Numbered indexes (not associative)",
        [
            "JavaScript arrays always use **numbered** indexes.",
        ],
        'const person = [];\nperson[0] = "John";\nperson[1] = "Doe";\nperson[2] = 46;',
        [
            ("person", "JSON.stringify(person)"),
            ("person.length", "person.length"),
            ("person[0]", "person[0]"),
        ],
        'length **3**. `person[0]` is **"John"**.',
    ),
    S(
        "named-indexes-warning",
        "WARNING named indexes become an object",
        [
            "Named keys do **not** make an associative array. `length` stays **0**.",
            "Some array methods then give **wrong** results.",
        ],
        'const person = [];\nperson["firstName"] = "John";\nperson["lastName"] = "Doe";\nperson["age"] = 46;',
        [
            ("person.length", "person.length"),
            ("person[0]", "person[0]"),
            ("person.firstName", "person.firstName"),
            ("Array.isArray(person)", "Array.isArray(person)"),
        ],
        'length **0**. `person[0]` is **undefined**. `firstName` is **"John"**. It is still an Array object, but **not** a list of elements.',
    ),
    S(
        "new-array-six-vs-literal",
        "new Array(40, 100, 1, 5, 25, 10) vs literal",
        [
            "Several numeric arguments create an array **of those numbers** — same as `[...]`.",
        ],
        "const a = new Array(40, 100, 1, 5, 25, 10);\nconst b = [40, 100, 1, 5, 25, 10];",
        [("a", "JSON.stringify(a)"), ("b", "JSON.stringify(b)")],
        "Both are **[40,100,1,5,25,10]**.",
    ),
    S(
        "typeof-object",
        "typeof fruits is object",
        [
            "`typeof` on an array is **`object`** because arrays are objects.",
        ],
        'const fruits = ["Banana", "Orange", "Apple"];\nlet type = typeof fruits;',
        [("type", "type")],
        "**object**.",
    ),
    S(
        "isarray",
        "Array.isArray(fruits)",
        [
            "`Array.isArray` is the ES5 way to recognize an array.",
        ],
        'const fruits = ["Banana", "Orange", "Apple"];\nArray.isArray(fruits);',
        [("Array.isArray(fruits)", "Array.isArray(fruits)")],
        "**true**.",
    ),
    S(
        "instanceof",
        "fruits instanceof Array",
        [
            "`instanceof Array` is **true** when the value was created as an array.",
        ],
        'const fruits = ["Banana", "Orange", "Apple"];\nfruits instanceof Array;',
        [("fruits instanceof Array", "fruits instanceof Array")],
        "**true**.",
    ),
    S(
        "nested-arrays-objects",
        "Nested arrays and objects",
        [
            "Object values may be arrays; array values may be objects.",
            "The page’s loop Tryit walks `cars` then each `models` list.",
        ],
        """const myObj = {
  name: "John",
  age: 30,
  cars: [
    {name:"Ford", models:["Fiesta", "Focus", "Mustang"]},
    {name:"BMW", models:["320", "X3", "X5"]},
    {name:"Fiat", models:["500", "Panda"]}
  ]
};
let x = "";
for (let i in myObj.cars) {
  x += myObj.cars[i].name + ": ";
  for (let j in myObj.cars[i].models) {
    x += myObj.cars[i].models[j] + " ";
  }
}""",
        [("x", "x")],
        "**Ford: Fiesta Focus Mustang BMW: 320 X3 X5 Fiat: 500 Panda** (trailing spaces).",
    ),
]


# ---------------------------------------------------------------------------
# 11.2 JS Array Constructor
# ---------------------------------------------------------------------------

CONSTRUCTOR = [
    S(
        "new-array-empty",
        "new Array() — empty",
        [
            "`new Array()` with **no arguments** creates an empty array.",
        ],
        "const a = new Array();",
        [("a", "JSON.stringify(a)"), ("a.length", "a.length")],
        "**[]**. length **0**.",
    ),
    S(
        "new-array-3",
        "new Array(3) — three empty spots",
        [
            "A **single number** is a length, not an element. Dangerous special case.",
            "`JSON.stringify` shows holes as **null**, but `0 in a` is **false**.",
        ],
        "const a = new Array(3);",
        [
            ("a", "JSON.stringify(a)"),
            ("a.length", "a.length"),
            ("0 in a", "0 in a"),
        ],
        "JSON **[null,null,null]**. length **3**. `0 in a` is **false** (empty slots, not nulls).",
    ),
    S(
        "new-array-string-3",
        'new Array("3") — one string element',
        [
            "A **non-number** single argument is **one element**, not a length.",
        ],
        'const a = new Array("3");',
        [("a", "JSON.stringify(a)"), ("a.length", "a.length")],
        '**["3"]**. length **1**.',
    ),
    S(
        "new-array-three-cars",
        'new Array("Saab", "Volvo", "BMW")',
        [
            "Multiple arguments become **elements**.",
        ],
        'const a = new Array("Saab", "Volvo", "BMW");',
        [("a", "JSON.stringify(a)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "array-fn-empty",
        "Array() without new — empty",
        [
            "`Array()` and `new Array()` do the **same** thing.",
            "If you omit `new`, the function adds it behind the scenes.",
        ],
        "const a = Array();",
        [("a", "JSON.stringify(a)"), ("a.length", "a.length")],
        "**[]**. length **0**.",
    ),
    S(
        "array-fn-3",
        "Array(3) without new — three empty spots",
        [
            "Same length trap **without** `new`.",
        ],
        "const a = Array(3);",
        [
            ("a", "JSON.stringify(a)"),
            ("a.length", "a.length"),
            ("0 in a", "0 in a"),
        ],
        "JSON **[null,null,null]**. length **3**. `0 in a` is **false**.",
    ),
    S(
        "array-fn-string-3",
        'Array("3") without new',
        [
            "One string argument is still **one element**.",
        ],
        'const a = Array("3");',
        [("a", "JSON.stringify(a)")],
        '**["3"]**.',
    ),
    S(
        "array-fn-three-cars",
        'Array("Saab", "Volvo", "BMW") without new',
        [
            "Multiple arguments without `new` still build that list.",
        ],
        'const a = Array("Saab", "Volvo", "BMW");',
        [("a", "JSON.stringify(a)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "six-numbers-new-vs-literal",
        "Six numbers: new Array vs []",
        [
            "Several numbers are **elements**, matching the literal.",
        ],
        "const a = new Array(40, 100, 1, 5, 25, 10);\nconst b = [40, 100, 1, 5, 25, 10];",
        [("a", "JSON.stringify(a)"), ("b", "JSON.stringify(b)")],
        "Both **[40,100,1,5,25,10]**.",
    ),
    S(
        "new-array-three-nums",
        "new Array(40, 100, 1) — three elements",
        [
            "Three numeric arguments → **three elements**.",
        ],
        "const points = new Array(40, 100, 1);",
        [("points", "JSON.stringify(points)"), ("points.length", "points.length")],
        "**[40,100,1]**. length **3**.",
    ),
    S(
        "new-array-two-nums",
        "new Array(40, 100) — two elements",
        [
            "Two numeric arguments → **two elements**.",
        ],
        "const points = new Array(40, 100);",
        [("points", "JSON.stringify(points)"), ("points.length", "points.length")],
        "**[40,100]**. length **2**.",
    ),
    S(
        "new-array-40-trap",
        "WARNING new Array(40) — 40 empty slots",
        [
            "**Single-number trap:** this is **not** `[40]`.",
            "The page shows this Tryit twice (the “???” line and the warning). Included once.",
        ],
        "const points = new Array(40);",
        [
            ("points.length", "points.length"),
            ("0 in points", "0 in points"),
            ("points[0]", "points[0]"),
        ],
        "length **40**. `0 in points` is **false**. `points[0]` is **undefined**.",
    ),
    S(
        "literal-40",
        "[40] — one element",
        [
            "A literal **`[40]`** is one number, not forty holes.",
        ],
        "const points = [40];",
        [("points", "JSON.stringify(points)"), ("points.length", "points.length")],
        "**[40]**. length **1**.",
    ),
    S(
        "literal-preferred",
        "Array literal (preferred)",
        [
            "Use **`[]`**. It is faster to type, easier to read, and avoids the number trap.",
        ],
        CARS,
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
]


# ---------------------------------------------------------------------------
# 11.3 JS Array Methods
# ---------------------------------------------------------------------------

METHODS = [
    S(
        "length-read",
        "fruits.length",
        [
            "`length` is the **size** of the array.",
        ],
        FR4 + "\nlet size = fruits.length;",
        [("size", "size")],
        "**4**.",
    ),
    S(
        "length-set",
        "fruits.length = 2",
        [
            "Setting `length` **truncates** (or extends with holes).",
        ],
        FR4 + "\nfruits.length = 2;",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange"]**.',
    ),
    S(
        "tostring",
        "fruits.toString()",
        [
            "`toString()` is a comma-separated string. Every object has `toString`.",
        ],
        FR4 + "\nlet myList = fruits.toString();",
        [("myList", "myList")],
        "**Banana,Orange,Apple,Mango**.",
    ),
    S(
        "at-2",
        "fruits.at(2)",
        [
            "ES2022 `at()` returns the element at that **index**.",
        ],
        FR4 + "\nlet fruit = fruits.at(2);",
        [("fruit", "fruit")],
        "**Apple**.",
    ),
    S(
        "bracket-2",
        "fruits[2]",
        [
            "`fruits[2]` is the same **positive** index as `at(2)`.",
        ],
        FR4 + "\nlet fruit = fruits[2];",
        [("fruit", "fruit")],
        "**Apple**.",
    ),
    S(
        "at-negative-vs-bracket",
        "WARNING fruits[-1] vs fruits.at(-1)",
        [
            "JS **`[-1]`** is the property named `\"-1\"`, not the last element.",
            "`at(-1)` was added to read from the **end**.",
        ],
        FR4 + "\nlet bracket = fruits[-1];\nlet fromEnd = fruits.at(-1);",
        [("fruits[-1]", "bracket"), ("fruits.at(-1)", "fromEnd")],
        '`fruits[-1]` is **undefined**. `fruits.at(-1)` is **Mango**.',
    ),
    S(
        "join-star",
        'fruits.join(" * ")',
        [
            "`join` is like `toString` but you pick the **separator**.",
        ],
        FR4 + '\nlet text = fruits.join(" * ");',
        [("text", "text")],
        "**Banana * Orange * Apple * Mango**.",
    ),
    S(
        "pop",
        "fruits.pop()",
        [
            "`pop` **removes the last** element.",
        ],
        FR4 + "\nfruits.pop();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Apple"]**.',
    ),
    S(
        "pop-return",
        "let fruit = fruits.pop()",
        [
            "`pop` **returns** the removed value.",
        ],
        FR4 + "\nlet fruit = fruits.pop();",
        [("fruit", "fruit"), ("fruits", "JSON.stringify(fruits)")],
        'fruit is **"Mango"**. fruits is **["Banana","Orange","Apple"]**.',
    ),
    S(
        "push-kiwi",
        'fruits.push("Kiwi")',
        [
            "`push` **appends** at the end.",
        ],
        FR4 + '\nfruits.push("Kiwi");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Apple","Mango","Kiwi"]**.',
    ),
    S(
        "push-return-length",
        'let length = fruits.push("Kiwi")',
        [
            "`push` **returns the new length**.",
        ],
        FR4 + '\nlet length = fruits.push("Kiwi");',
        [("length", "length"), ("fruits", "JSON.stringify(fruits)")],
        'length **5**. fruits **["Banana","Orange","Apple","Mango","Kiwi"]**.',
    ),
    S(
        "shift",
        "fruits.shift()",
        [
            "`shift` removes the **first** element and moves the rest down.",
        ],
        FR4 + "\nfruits.shift();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Orange","Apple","Mango"]**.',
    ),
    S(
        "shift-return",
        "let fruit = fruits.shift()",
        [
            "`shift` **returns** the removed first value.",
        ],
        FR4 + "\nlet fruit = fruits.shift();",
        [("fruit", "fruit"), ("fruits", "JSON.stringify(fruits)")],
        'fruit is **"Banana"**. fruits is **["Orange","Apple","Mango"]**.',
    ),
    S(
        "unshift-lemon",
        'fruits.unshift("Lemon")',
        [
            "`unshift` inserts at the **beginning**.",
        ],
        FR4 + '\nfruits.unshift("Lemon");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Lemon","Banana","Orange","Apple","Mango"]**.',
    ),
    S(
        "unshift-return-length",
        'let length = fruits.unshift("Lemon")',
        [
            "`unshift` **returns the new length** (the page’s second unshift Tryit).",
        ],
        FR4 + '\nlet length = fruits.unshift("Lemon");',
        [("length", "length"), ("fruits", "JSON.stringify(fruits)")],
        'length **5**. fruits **["Lemon","Banana","Orange","Apple","Mango"]**.',
    ),
    S(
        "change-index-0",
        'fruits[0] = "Kiwi"',
        [
            "Indexes start at **0**. Assignment replaces that slot.",
        ],
        FR4 + '\nfruits[0] = "Kiwi";',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Kiwi","Orange","Apple","Mango"]**.',
    ),
    S(
        "append-via-length",
        "fruits[fruits.length] = Kiwi",
        [
            "Writing at `length` **appends**.",
        ],
        FR4 + '\nfruits[fruits.length] = "Kiwi";',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Apple","Mango","Kiwi"]**.',
    ),
    S(
        "isarray",
        "Array.isArray(fruits)",
        [
            "ES5 `Array.isArray` identifies arrays.",
        ],
        FR4 + "\nArray.isArray(fruits);",
        [("Array.isArray(fruits)", "Array.isArray(fruits)")],
        "**true**.",
    ),
    S(
        "delete-holes",
        "WARNING delete fruits[0]",
        [
            "`delete` leaves an **undefined hole**. Prefer `pop` / `shift` / `splice`.",
        ],
        FR4 + "\ndelete fruits[0];",
        [
            ("fruits", "JSON.stringify(fruits)"),
            ("fruits[0]", "fruits[0]"),
            ("0 in fruits", "0 in fruits"),
            ("fruits.length", "fruits.length"),
        ],
        'JSON **[null,"Orange","Apple","Mango"]**. `fruits[0]` is **undefined**. `0 in fruits` is **false**. length still **4**.',
    ),
    S(
        "concat-two",
        "concat two arrays",
        [
            "`concat` **merges** arrays and returns a **new** array. Originals stay.",
        ],
        'const myGirls = ["Cecilie", "Lone"];\nconst myBoys = ["Emil", "Tobias", "Linus"];\nconst myChildren = myGirls.concat(myBoys);',
        [
            ("myChildren", "JSON.stringify(myChildren)"),
            ("myGirls", "JSON.stringify(myGirls)"),
        ],
        '**["Cecilie","Lone","Emil","Tobias","Linus"]**. myGirls is unchanged.',
    ),
    S(
        "concat-three",
        "concat three arrays",
        [
            "`concat` takes **any number** of array arguments.",
        ],
        'const arr1 = ["Cecilie", "Lone"];\nconst arr2 = ["Emil", "Tobias", "Linus"];\nconst arr3 = ["Robin", "Morgan"];\nconst myChildren = arr1.concat(arr2, arr3);',
        [("myChildren", "JSON.stringify(myChildren)")],
        '**["Cecilie","Lone","Emil","Tobias","Linus","Robin","Morgan"]**.',
    ),
    S(
        "concat-string",
        'concat an array with "Peter"',
        [
            "Arguments may be **values**, not only arrays.",
        ],
        'const arr1 = ["Emil", "Tobias", "Linus"];\nconst myChildren = arr1.concat("Peter");',
        [("myChildren", "JSON.stringify(myChildren)")],
        '**["Emil","Tobias","Linus","Peter"]**.',
    ),
    S(
        "copywithin-2-0",
        "copyWithin(2, 0)",
        [
            "Copy to index **2** from index **0** through the end. **Overwrites**. Length unchanged.",
        ],
        FR4 + "\nfruits.copyWithin(2, 0);",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Banana","Orange"]**.',
    ),
    S(
        "copywithin-2-0-2",
        "copyWithin(2, 0, 2)",
        [
            "Copy to index **2** the slice **[0, 2)** (end not included).",
        ],
        'const fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi"];\nfruits.copyWithin(2, 0, 2);',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Banana","Orange","Kiwi"]**.',
    ),
    S(
        "flat",
        "[[1,2],[3,4],[5,6]].flat()",
        [
            "ES2019 `flat()` concatenates **one level** of sub-arrays by default.",
        ],
        "const myArr = [[1,2],[3,4],[5,6]];\nconst newArr = myArr.flat();",
        [("newArr", "JSON.stringify(newArr)")],
        "**[1,2,3,4,5,6]**.",
    ),
    S(
        "flatmap",
        "flatMap(x => [x, x * 10])",
        [
            "`flatMap` maps, then flattens **one** level.",
        ],
        "const myArr = [1, 2, 3, 4, 5, 6];\nconst newArr = myArr.flatMap(x => [x, x * 10]);",
        [("newArr", "JSON.stringify(newArr)")],
        "**[1,10,2,20,3,30,4,40,5,50,6,60]**.",
    ),
    S(
        "splice-add",
        'splice(2, 0, "Lemon", "Kiwi")',
        [
            "Start at **2**, delete **0**, insert Lemon and Kiwi. **Mutates**.",
        ],
        FR4 + '\nfruits.splice(2, 0, "Lemon", "Kiwi");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Lemon","Kiwi","Apple","Mango"]**.',
    ),
    S(
        "splice-replace",
        'splice(2, 2, "Lemon", "Kiwi")',
        [
            "Delete **2** items at index 2, insert two new ones. Returns the **deleted** items.",
        ],
        FR4 + '\nlet removed = fruits.splice(2, 2, "Lemon", "Kiwi");',
        [
            ("fruits", "JSON.stringify(fruits)"),
            ("removed", "JSON.stringify(removed)"),
        ],
        'fruits **["Banana","Orange","Lemon","Kiwi"]**. removed **["Apple","Mango"]**.',
    ),
    S(
        "splice-remove",
        "splice(0, 1) — remove without holes",
        [
            "Delete 1 at index 0. No insert. Cleaner than `delete`.",
        ],
        FR4 + "\nfruits.splice(0, 1);",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Orange","Apple","Mango"]**.',
    ),
    S(
        "tospliced",
        "months.toSpliced(0, 1)",
        [
            "ES2023 `toSpliced` returns a **new** array. Original stays.",
        ],
        MONTHS + "\nconst spliced = months.toSpliced(0, 1);",
        [
            ("spliced", "JSON.stringify(spliced)"),
            ("months", "JSON.stringify(months)"),
        ],
        'spliced **["Feb","Mar","Apr"]**. months still **["Jan","Feb","Mar","Apr"]**.',
    ),
    S(
        "slice-1",
        "slice(1)",
        [
            "`slice(1)` copies from index **1** to the end. Source is unchanged.",
        ],
        FR5 + "\nconst citrus = fruits.slice(1);",
        [
            ("citrus", "JSON.stringify(citrus)"),
            ("fruits", "JSON.stringify(fruits)"),
        ],
        '**["Orange","Lemon","Apple","Mango"]**. fruits unchanged.',
    ),
    S(
        "slice-3",
        "slice(3)",
        [
            "`slice(3)` starts at **Apple**.",
        ],
        FR5 + "\nconst citrus = fruits.slice(3);",
        [("citrus", "JSON.stringify(citrus)")],
        '**["Apple","Mango"]**.',
    ),
    S(
        "slice-1-3",
        "slice(1, 3)",
        [
            "`slice(start, end)` copies **up to but not including** end.",
        ],
        FR5 + "\nconst citrus = fruits.slice(1, 3);",
        [("citrus", "JSON.stringify(citrus)")],
        '**["Orange","Lemon"]**.',
    ),
    S(
        "slice-2",
        "slice(2)",
        [
            "Omitting end still means **the rest** of the array.",
        ],
        FR5 + "\nconst citrus = fruits.slice(2);",
        [("citrus", "JSON.stringify(citrus)")],
        '**["Lemon","Apple","Mango"]**.',
    ),
    S(
        "auto-tostring",
        "fruits.toString() for display",
        [
            "When a primitive is needed, JS calls `toString` on the array.",
        ],
        FR4 + "\nlet text = fruits.toString();",
        [("text", "text")],
        "**Banana,Orange,Apple,Mango**.",
    ),
    S(
        "auto-string-coercion",
        "String(fruits) without calling toString",
        [
            "The matching Tryit assigns the array into HTML; coercion is the same.",
        ],
        FR4 + "\nlet text = String(fruits);",
        [("text", "text")],
        "**Banana,Orange,Apple,Mango** — same as `toString()`.",
    ),
]


# ---------------------------------------------------------------------------
# 11.4 JS Array Search
# ---------------------------------------------------------------------------

SEARCH = [
    S(
        "indexof-apple",
        'indexOf("Apple") + 1',
        [
            "`indexOf` returns the **first** index, or **-1**. The page adds **1** for a 1-based position.",
        ],
        'const fruits = ["Apple", "Orange", "Apple", "Mango"];\nlet position = fruits.indexOf("Apple") + 1;',
        [("position", "position"), ("indexOf", 'fruits.indexOf("Apple")')],
        "First index is **0**, so position is **1**.",
    ),
    S(
        "lastindexof-apple",
        'lastIndexOf("Apple") + 1',
        [
            "`lastIndexOf` is the **last** occurrence, still +1 on the page.",
        ],
        'const fruits = ["Apple", "Orange", "Apple", "Mango"];\nlet position = fruits.lastIndexOf("Apple") + 1;',
        [("position", "position"), ("lastIndexOf", 'fruits.lastIndexOf("Apple")')],
        "Last index is **2**, so position is **3**.",
    ),
    S(
        "includes-mango",
        'includes("Mango")',
        [
            "ES2016 `includes` is a **boolean** membership test.",
        ],
        FR4 + '\nfruits.includes("Mango");',
        [('fruits.includes("Mango")', 'fruits.includes("Mango")')],
        "**true**.",
    ),
    S(
        "includes-nan-vs-indexof",
        "includes(NaN) vs indexOf(NaN)",
        [
            "No Tryit — the page notes `includes` finds **NaN**; `indexOf` does not.",
        ],
        "const a = [NaN];",
        [("a.indexOf(NaN)", "a.indexOf(NaN)"), ("a.includes(NaN)", "a.includes(NaN)")],
        "`indexOf` is **-1**. `includes` is **true**.",
    ),
    S(
        "find-gt-18",
        "find first value > 18",
        [
            "`find` returns the **value** of the first match, or `undefined`.",
            "Callback args: value, index, array.",
        ],
        N_FIND
        + """
let first = numbers.find(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}""",
        [("first", "first")],
        "**25**.",
    ),
    S(
        "findindex-gt-18",
        "findIndex of first value > 18",
        [
            "`findIndex` returns the **index** of that first match, or **-1**.",
        ],
        N_FIND
        + """
let first = numbers.findIndex(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}""",
        [("first", "first")],
        "**3**.",
    ),
    S(
        "findlast-gt-40",
        "findLast(x => x > 40)",
        [
            "ES2023 `findLast` searches **from the end** and returns the value.",
        ],
        "const temp = [27, 28, 30, 40, 42, 35, 30];\nlet high = temp.findLast(x => x > 40);",
        [("high", "high")],
        "**42**.",
    ),
    S(
        "findlastindex-gt-40",
        "findLastIndex(x => x > 40)",
        [
            "`findLastIndex` is the **index** of that last match.",
        ],
        "const temp = [27, 28, 30, 40, 42, 35, 30];\nlet pos = temp.findLastIndex(x => x > 40);",
        [("pos", "pos")],
        "**4**.",
    ),
]


# ---------------------------------------------------------------------------
# 11.5 JS Array Sort
# ---------------------------------------------------------------------------

SORT = [
    S(
        "sort-alpha",
        "fruits.sort() — alphabetic",
        [
            "Default `sort` compares **as strings** and **mutates** the array.",
        ],
        FR4 + "\nfruits.sort();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Apple","Banana","Mango","Orange"]**.',
    ),
    S(
        "reverse",
        "fruits.reverse()",
        [
            "`reverse` flips **in place** (no sort).",
        ],
        FR4 + "\nfruits.reverse();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Mango","Apple","Orange","Banana"]**.',
    ),
    S(
        "sort-then-reverse",
        "sort then reverse — descending alpha",
        [
            "Sort first, then reverse, for **Z→A** strings.",
        ],
        FR4 + "\nfruits.sort();\nfruits.reverse();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Orange","Mango","Banana","Apple"]**.',
    ),
    S(
        "tosorted",
        "months.toSorted()",
        [
            "ES2023 `toSorted` returns a **new** sorted array.",
        ],
        MONTHS + "\nconst sorted = months.toSorted();",
        [
            ("sorted", "JSON.stringify(sorted)"),
            ("months", "JSON.stringify(months)"),
        ],
        'sorted **["Apr","Feb","Jan","Mar"]**. months unchanged.',
    ),
    S(
        "toreversed",
        "months.toReversed()",
        [
            "`toReversed` returns a **new** reversed array.",
        ],
        MONTHS + "\nconst reversed = months.toReversed();",
        [
            ("reversed", "JSON.stringify(reversed)"),
            ("months", "JSON.stringify(months)"),
        ],
        'reversed **["Apr","Mar","Feb","Jan"]**. months unchanged.',
    ),
    S(
        "numeric-asc",
        "sort(function(a, b){return a - b})",
        [
            "Compare function: negative → `a` first. `a - b` is **ascending** numbers.",
        ],
        PTS + "\npoints.sort(function(a, b){return a - b});",
        [("points", "JSON.stringify(points)")],
        "**[1,5,10,25,40,100]**.",
    ),
    S(
        "numeric-desc",
        "sort(function(a, b){return b - a})",
        [
            "`b - a` is **descending** numbers.",
        ],
        PTS + "\npoints.sort(function(a, b){return b - a});",
        [("points", "JSON.stringify(points)")],
        "**[100,40,25,10,5,1]**.",
    ),
    S(
        "alpha-vs-numeric-buttons",
        "Default sort vs numeric sort (the button demo)",
        [
            "The page’s two buttons run **string sort** vs **`a - b`**.",
            "String sort of numbers is wrong: `\"25\"` vs `\"100\"` compares `\"2\"` and `\"1\"`.",
        ],
        PTS
        + """
const alpha = points.slice().sort();
const numeric = points.slice().sort(function(a, b){return a - b});""",
        [
            ("alpha", "JSON.stringify(alpha)"),
            ("numeric", "JSON.stringify(numeric)"),
        ],
        "Alphabetic **[1,10,100,25,40,5]**. Numeric **[1,5,10,25,40,100]**.",
    ),
    S(
        "random-sort",
        "sort(function(){return 0.5 - Math.random()})",
        [
            "A random compare **shuffles**, but it is **biased**. Still run it.",
        ],
        PTS + "\npoints.sort(function(){return 0.5 - Math.random()});",
        [("points", "JSON.stringify(points)")],
        "The printed order is **random** (one permutation of 40, 100, 1, 5, 25, 10). Do not treat this shuffle as fair.",
    ),
    S(
        "fisher-yates",
        "Fisher–Yates shuffle",
        [
            "The unbiased shuffle: swap `i` with a random index `≤ i`, walking **backward**.",
        ],
        PTS
        + """
for (let i = points.length - 1; i > 0; i--) {
  let j = Math.floor(Math.random() * (i + 1));
  let k = points[i];
  points[i] = points[j];
  points[j] = k;
}""",
        [("points", "JSON.stringify(points)")],
        "The printed order is **random** but a **fair** permutation of the six numbers.",
    ),
    S(
        "min-max-via-sort-asc",
        "Lowest / highest after ascending sort",
        [
            "After `a - b`, `[0]` is min and `[length-1]` is max. Sorting all of it is **overkill** for one extremum.",
        ],
        PTS
        + """
points.sort(function(a, b){return a - b});
let lowest = points[0];
let highest = points[points.length - 1];""",
        [
            ("points", "JSON.stringify(points)"),
            ("lowest", "lowest"),
            ("highest", "highest"),
        ],
        "Sorted **[1,5,10,25,40,100]**. lowest **1**, highest **100**.",
    ),
    S(
        "min-max-via-sort-desc",
        "Highest / lowest after descending sort",
        [
            "After `b - a`, `[0]` is max.",
        ],
        PTS
        + """
points.sort(function(a, b){return b - a});
let highest = points[0];
let lowest = points[points.length - 1];""",
        [
            ("points", "JSON.stringify(points)"),
            ("highest", "highest"),
            ("lowest", "lowest"),
        ],
        "Sorted **[100,40,25,10,5,1]**. highest **100**, lowest **1**.",
    ),
    S(
        "math-min-apply",
        "Math.min.apply(null, arr)",
        [
            "`Math.min.apply(null, [1,2,3])` is `Math.min(1,2,3)`.",
        ],
        PTS
        + """
function myArrayMin(arr) {
  return Math.min.apply(null, arr);
}
let min = myArrayMin(points);""",
        [("min", "min")],
        "**1**.",
    ),
    S(
        "math-max-apply",
        "Math.max.apply(null, arr)",
        [
            "Same idea for the **highest** value.",
        ],
        PTS
        + """
function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}
let max = myArrayMax(points);""",
        [("max", "max")],
        "**100**.",
    ),
    S(
        "homemade-min",
        "Home-made myArrayMin",
        [
            "Loop, compare to `Infinity`. Fastest simple min.",
        ],
        PTS
        + """
function myArrayMin(arr) {
  let len = arr.length;
  let min = Infinity;
  while (len--) {
    if (arr[len] < min) {
      min = arr[len];
    }
  }
  return min;
}
let min = myArrayMin(points);""",
        [("min", "min")],
        "**1**.",
    ),
    S(
        "homemade-max",
        "Home-made myArrayMax",
        [
            "Loop, compare to `-Infinity`.",
        ],
        PTS
        + """
function myArrayMax(arr) {
  let len = arr.length;
  let max = -Infinity;
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}
let max = myArrayMax(points);""",
        [("max", "max")],
        "**100**.",
    ),
    S(
        "cars-objects",
        "Array of car objects",
        [
            "No Tryit for the unsorted list — still a runnable demo of objects in an array.",
        ],
        CARS_OBJ,
        [("cars", "JSON.stringify(cars)")],
        'Three cars: Volvo 2016, Saab 2001, BMW 2010.',
    ),
    S(
        "sort-cars-year",
        "Sort cars by year",
        [
            "`a.year - b.year` sorts **numeric** properties.",
        ],
        CARS_OBJ + "\ncars.sort(function(a, b){return a.year - b.year});",
        [("cars", "JSON.stringify(cars)")],
        "Saab 2001, BMW 2010, Volvo 2016.",
    ),
    S(
        "sort-cars-type",
        "Sort cars by type string",
        [
            "Compare lowercased strings with **-1 / 0 / 1**.",
        ],
        CARS_OBJ
        + """
cars.sort(function(a, b){
  let x = a.type.toLowerCase();
  let y = b.type.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
});""",
        [("cars", "JSON.stringify(cars)")],
        "BMW, Saab, Volvo.",
    ),
    S(
        "stable-sort",
        "Stable sort by price (ES2019)",
        [
            "Equal keys must keep **relative order**. Sort these eight rows by `price`.",
        ],
        """const myArr = [
  {name:"X00",price:100}, {name:"X01",price:100},
  {name:"X02",price:100}, {name:"X03",price:100},
  {name:"X04",price:110}, {name:"X05",price:110},
  {name:"X06",price:110}, {name:"X07",price:110}
];
myArr.sort(function(a, b){return a.price - b.price});
const names = myArr.map(o => o.name + " " + o.price);""",
        [("names", "JSON.stringify(names)")],
        '**["X00 100","X01 100","X02 100","X03 100","X04 110","X05 110","X06 110","X07 110"]** — X00 stayed before X01, and so on.',
    ),
]


# ---------------------------------------------------------------------------
# 11.6 JS Array Iterations
# ---------------------------------------------------------------------------

ITERATIONS = [
    S(
        "for-of",
        "for...of over car values",
        [
            "`for...of` yields **values**. Recommended for arrays.",
        ],
        'const cars = ["BMW", "Volvo", "Mini"];\nlet text = "";\nfor (let x of cars) {\n  text += x + ",";\n}',
        [("text", "text")],
        "**BMW,Volvo,Mini,**",
    ),
    S(
        "for-in-indexes",
        "for...in over indexes (not recommended)",
        [
            "`for...in` yields **keys** (indexes as strings). Built for **objects**, not arrays.",
        ],
        'const cars = ["BMW", "Volvo", "Mini"];\nlet text = "";\nfor (let x in cars) {\n  text += x + ",";\n}',
        [("text", "text")],
        "**0,1,2,**",
    ),
    S(
        "for-in-values",
        "for...in with cars[x]",
        [
            "You can read `cars[x]`, but `for...in` is still a **bad idea** for arrays.",
        ],
        'const cars = ["BMW", "Volvo", "Mini"];\nlet text = "";\nfor (let x in cars) {\n  text += cars[x] + "";\n}',
        [("text", "text")],
        "**BMWVolvoMini** (the Tryit concatenates with an empty separator).",
    ),
    S(
        "foreach-three-args",
        "forEach with value, index, array",
        [
            "Callback receives **value, index, array**. This demo uses value only in the body.",
        ],
        NUMS
        + """
let txt = "";
numbers.forEach(myFunction);
function myFunction(value, index, array) {
  txt += value + " ";
}""",
        [("txt", "txt")],
        "**45 4 9 16 25** (trailing space).",
    ),
    S(
        "foreach-value-only",
        "forEach with value only",
        [
            "Unused index/array parameters may be **omitted**.",
        ],
        NUMS
        + """
let txt = "";
numbers.forEach(myFunction);
function myFunction(value) {
  txt += value + " ";
}""",
        [("txt", "txt")],
        "**45 4 9 16 25** (trailing space).",
    ),
    S(
        "map-three-args",
        "map value * 2 (three-arg callback)",
        [
            "`map` returns a **new** array. Original stays.",
        ],
        """const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);
function myFunction(value, index, array) {
  return value * 2;
}""",
        [
            ("numbers2", "JSON.stringify(numbers2)"),
            ("numbers1", "JSON.stringify(numbers1)"),
        ],
        "New **[90,8,18,32,50]**. Original unchanged.",
    ),
    S(
        "map-value-only",
        "map value * 2 (value only)",
        [
            "Same result with a **one-parameter** callback.",
        ],
        """const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);
function myFunction(value) {
  return value * 2;
}""",
        [("numbers2", "JSON.stringify(numbers2)")],
        "**[90,8,18,32,50]**.",
    ),
    S(
        "flatmap",
        "flatMap(x => [x, x * 10])",
        [
            "Map then flatten one level — same Tryit idea as the methods page.",
        ],
        "const myArr = [1, 2, 3, 4, 5, 6];\nconst newArr = myArr.flatMap(x => [x, x * 10]);",
        [("newArr", "JSON.stringify(newArr)")],
        "**[1,10,2,20,3,30,4,40,5,50,6,60]**.",
    ),
    S(
        "filter-three-args",
        "filter values > 18 (three-arg callback)",
        [
            "`filter` keeps elements that pass the test. **New** array.",
        ],
        NUMS
        + """
const over18 = numbers.filter(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}""",
        [("over18", "JSON.stringify(over18)")],
        "**[45,25]**.",
    ),
    S(
        "filter-value-only",
        "filter values > 18 (value only)",
        [
            "Same filter with unused parameters dropped.",
        ],
        NUMS
        + """
const over18 = numbers.filter(myFunction);
function myFunction(value) {
  return value > 18;
}""",
        [("over18", "JSON.stringify(over18)")],
        "**[45,25]**.",
    ),
    S(
        "reduce-four-args",
        "reduce sum (four-arg callback)",
        [
            "`reduce` folds left-to-right into **one value**. Does not change the array.",
            "Args: total, value, index, array.",
        ],
        NUMS
        + """
let sum = numbers.reduce(myFunction);
function myFunction(total, value, index, array) {
  return total + value;
}""",
        [("sum", "sum")],
        "**99** (45+4+9+16+25).",
    ),
    S(
        "reduce-two-args",
        "reduce sum (total, value)",
        [
            "Same sum without unused parameters.",
        ],
        NUMS
        + """
let sum = numbers.reduce(myFunction);
function myFunction(total, value) {
  return total + value;
}""",
        [("sum", "sum")],
        "**99**.",
    ),
    S(
        "reduce-initial-100",
        "reduce sum with initial 100",
        [
            "The second argument to `reduce` is the **starting total**.",
        ],
        NUMS
        + """
let sum = numbers.reduce(myFunction, 100);
function myFunction(total, value) {
  return total + value;
}""",
        [("sum", "sum")],
        "**199**.",
    ),
    S(
        "reduceright-four-args",
        "reduceRight sum (four-arg callback)",
        [
            "`reduceRight` folds **right-to-left**. Same sum for addition.",
        ],
        NUMS
        + """
let sum = numbers.reduceRight(myFunction);
function myFunction(total, value, index, array) {
  return total + value;
}""",
        [("sum", "sum")],
        "**99**.",
    ),
    S(
        "reduceright-two-args",
        "reduceRight sum (total, value)",
        [
            "Same right-fold with a shorter callback.",
        ],
        NUMS
        + """
let sum = numbers.reduceRight(myFunction);
function myFunction(total, value) {
  return total + value;
}""",
        [("sum", "sum")],
        "**99**.",
    ),
    S(
        "every-three-args",
        "every value > 18 (three-arg callback)",
        [
            "`every` is **true** only if **all** elements pass.",
        ],
        NUMS
        + """
let allOver18 = numbers.every(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}""",
        [("allOver18", "allOver18")],
        "**false** (4, 9, and 16 fail).",
    ),
    S(
        "every-value-only",
        "every value > 18 (value only)",
        [
            "Same test with a one-parameter callback.",
        ],
        NUMS
        + """
let allOver18 = numbers.every(myFunction);
function myFunction(value) {
  return value > 18;
}""",
        [("allOver18", "allOver18")],
        "**false**.",
    ),
    S(
        "some-three-args",
        "some value > 18",
        [
            "`some` is **true** if **any** element passes.",
        ],
        NUMS
        + """
let someOver18 = numbers.some(myFunction);
function myFunction(value, index, array) {
  return value > 18;
}""",
        [("someOver18", "someOver18")],
        "**true** (45 and 25 pass).",
    ),
    S(
        "from-string",
        'Array.from("ABCDEFG")',
        [
            "`Array.from` builds an array from an **iterable** (here a string).",
        ],
        'let text = "ABCDEFG";\nconst letters = Array.from(text);',
        [("letters", "JSON.stringify(letters)")],
        '**["A","B","C","D","E","F","G"]**.',
    ),
    S(
        "from-map",
        "Array.from(array, x => x * 2)",
        [
            "Optional map function runs on each new element.",
        ],
        "const myNumbers = [1,2,3,4];\nconst myArr = Array.from(myNumbers, (x) => x * 2);",
        [("myArr", "JSON.stringify(myArr)")],
        "**[2,4,6,8]**.",
    ),
    S(
        "keys",
        "fruits.keys() iterator",
        [
            "`keys()` is an **iterator** of indexes.",
        ],
        FR4
        + """
const keys = fruits.keys();
let text = "";
for (let x of keys) {
  text += x + " ";
}""",
        [("text", "text")],
        "**0 1 2 3** (trailing space).",
    ),
    S(
        "entries",
        "fruits.entries() key/value pairs",
        [
            "`entries()` yields **[index, value]** pairs.",
        ],
        FR4
        + """
const f = fruits.entries();
let text = "";
for (let x of f) {
  text += String(x);
}""",
        [("text", "text")],
        "**0,Banana1,Orange2,Apple3,Mango** (each pair stringifies as `index,value`).",
    ),
    S(
        "with-method",
        'months.with(2, "March")',
        [
            "ES2023 `with` returns a **new** array with one index updated.",
        ],
        'const months = ["Januar", "Februar", "Mar", "April"];\nconst myMonths = months.with(2, "March");',
        [
            ("myMonths", "JSON.stringify(myMonths)"),
            ("months", "JSON.stringify(months)"),
        ],
        'myMonths **["Januar","Februar","March","April"]**. Original still has **"Mar"**.',
    ),
    S(
        "spread-join-two",
        "Spread join two arrays",
        [
            "`...` expands an array into **elements**.",
        ],
        "const arr1 = [1, 2, 3];\nconst arr2 = [4, 5, 6];\nconst arr3 = [...arr1, ...arr2];",
        [("arr3", "JSON.stringify(arr3)")],
        "**[1,2,3,4,5,6]**.",
    ),
    S(
        "spread-year",
        "Spread four quarter arrays",
        [
            "The page uses **Des** (not Dec) in q4.",
        ],
        """const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "Des"];
const year = [...q1, ...q2, ...q3, ...q4];""",
        [("year", "JSON.stringify(year)")],
        '**["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Des"]**.',
    ),
    S(
        "spread-copy",
        "Spread copy an array",
        [
            "`[...arr1]` is a **shallow copy**.",
        ],
        "const arr1 = [1, 2, 3];\nconst arr2 = [...arr1];",
        [
            ("arr2", "JSON.stringify(arr2)"),
            ("arr1 === arr2", "arr1 === arr2"),
        ],
        "**[1,2,3]**. `arr1 === arr2` is **false** (different array).",
    ),
    S(
        "spread-math-min-max",
        "Math.min / Math.max with spread",
        [
            "Spread turns an array into **argument list**.",
        ],
        "const numbers = [23, 55, 21, 87, 56];\nlet minValue = Math.min(...numbers);\nlet maxValue = Math.max(...numbers);",
        [("minValue", "minValue"), ("maxValue", "maxValue")],
        "min **21**, max **87**.",
    ),
    S(
        "rest-a",
        "[a, ...rest] = arr1",
        [
            "Rest **collects leftover** elements after destructuring.",
        ],
        "let a, rest;\nconst arr1 = [1,2,3,4,5,6,7,8];\n[a, ...rest] = arr1;",
        [("a", "a"), ("rest", "JSON.stringify(rest)")],
        "a **1**. rest **[2,3,4,5,6,7,8]**.",
    ),
    S(
        "rest-a-b",
        "[a, b, ...rest] = arr1",
        [
            "Two named bindings, then the rest.",
        ],
        "let a, b, rest;\nconst arr1 = [1,2,3,4,5,6,7,8];\n[a, b, ...rest] = arr1;",
        [("a", "a"), ("b", "b"), ("rest", "JSON.stringify(rest)")],
        "a **1**, b **2**, rest **[3,4,5,6,7,8]**.",
    ),
]


# ---------------------------------------------------------------------------
# 11.7 JS Array Reference (one Example per table row)
# ---------------------------------------------------------------------------

FR = FR4
N18 = N_FIND


def _ref(stem: str, title: str, meaning: str, code: str, displays: list, outcome: str) -> dict:
    return S(stem, title, [meaning], code, displays, outcome)


REFERENCE = [
    _ref(
        "literal",
        "[] — creates a new Array",
        "An array **literal** creates a new array.",
        CARS,
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    _ref(
        "new-array",
        "new Array() — creates a new Array",
        "`new Array()` with no args is an **empty** array.",
        "const a = new Array();",
        [("a", "JSON.stringify(a)")],
        "**[]**.",
    ),
    _ref(
        "at",
        "at() — indexed element",
        "`at(2)` is **Apple**. `at` also accepts negatives.",
        FR + "\nlet fruit = fruits.at(2);",
        [("fruit", "fruit")],
        "**Apple**.",
    ),
    _ref(
        "concat",
        "concat() — join arrays",
        "`concat` returns a **new** joined array.",
        'const a = ["Cecilie", "Lone"];\nconst b = a.concat(["Emil"]);',
        [("b", "JSON.stringify(b)")],
        '**["Cecilie","Lone","Emil"]**.',
    ),
    _ref(
        "constructor",
        "constructor — function that created Array.prototype",
        "Instance `constructor` is **Array**.",
        FR + "\nfruits.constructor;\nfruits.constructor === Array;",
        [
            ("String(fruits.constructor)", "String(fruits.constructor)"),
            ("fruits.constructor === Array", "fruits.constructor === Array"),
        ],
        "`function Array() { [native code] }`. `=== Array` is **true**.",
    ),
    _ref(
        "copywithin",
        "copyWithin() — copy within the array",
        "`copyWithin(2, 0)` overwrites from index 2 using items from 0.",
        FR + "\nfruits.copyWithin(2, 0);",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Banana","Orange"]**.',
    ),
    _ref(
        "entries",
        "entries() — [index, value] iterator",
        "`Array.from(fruits.entries())` materializes the pairs.",
        FR + "\nconst pairs = Array.from(fruits.entries());",
        [("pairs", "JSON.stringify(pairs)")],
        '**[[0,"Banana"],[1,"Orange"],[2,"Apple"],[3,"Mango"]]**.',
    ),
    _ref(
        "every",
        "every() — all pass a test?",
        "`every(v => v > 18)` on [4, 9, 16, 25, 29].",
        N18 + "\nlet ok = numbers.every(v => v > 18);",
        [("ok", "ok")],
        "**false**.",
    ),
    _ref(
        "fill",
        "fill() — fill with a static value",
        "`fill(\"Kiwi\")` replaces every element.",
        FR + '\nfruits.fill("Kiwi");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Kiwi","Kiwi","Kiwi","Kiwi"]**.',
    ),
    _ref(
        "filter",
        "filter() — keep elements that pass",
        "Keep values **> 18**.",
        N18 + "\nconst over = numbers.filter(v => v > 18);",
        [("over", "JSON.stringify(over)")],
        "**[25,29]**.",
    ),
    _ref(
        "find",
        "find() — first matching value",
        "First value **> 18**.",
        N18 + "\nlet first = numbers.find(v => v > 18);",
        [("first", "first")],
        "**25**.",
    ),
    _ref(
        "findindex",
        "findIndex() — first matching index",
        "Index of first value **> 18**.",
        N18 + "\nlet i = numbers.findIndex(v => v > 18);",
        [("i", "i")],
        "**3**.",
    ),
    _ref(
        "findlast",
        "findLast() — last matching value",
        "From the end, first value **> 40**.",
        "const temp = [27, 28, 30, 40, 42, 35, 30];\nlet high = temp.findLast(x => x > 40);",
        [("high", "high")],
        "**42**.",
    ),
    _ref(
        "findlastindex",
        "findLastIndex() — last matching index",
        "Index of that last match.",
        "const temp = [27, 28, 30, 40, 42, 35, 30];\nlet pos = temp.findLastIndex(x => x > 40);",
        [("pos", "pos")],
        "**4**.",
    ),
    _ref(
        "flat",
        "flat() — concatenate sub-arrays",
        "Flatten one level.",
        "const newArr = [[1,2],[3,4]].flat();",
        [("newArr", "JSON.stringify(newArr)")],
        "**[1,2,3,4]**.",
    ),
    _ref(
        "flatmap",
        "flatMap() — map then flatten",
        "Each `x` becomes `[x, x*10]`.",
        "const newArr = [1, 2].flatMap(x => [x, x * 10]);",
        [("newArr", "JSON.stringify(newArr)")],
        "**[1,10,2,20]**.",
    ),
    _ref(
        "foreach",
        "forEach() — call a function per element",
        "Join values with spaces.",
        FR
        + """
let text = "";
fruits.forEach(function(value){ text += value + " "; });""",
        [("text", "text")],
        "**Banana Orange Apple Mango** (trailing space).",
    ),
    _ref(
        "from",
        "from() — array from an object",
        "`Array.from` on a string.",
        'const letters = Array.from("ABC");',
        [("letters", "JSON.stringify(letters)")],
        '**["A","B","C"]**.',
    ),
    _ref(
        "includes",
        "includes() — contains the element?",
        'Does fruits include **"Mango"**?',
        FR + '\nfruits.includes("Mango");',
        [('fruits.includes("Mango")', 'fruits.includes("Mango")')],
        "**true**.",
    ),
    _ref(
        "indexof",
        "indexOf() — first position",
        'First index of **"Apple"** in a list that has two Apples.',
        'const fruits = ["Apple", "Orange", "Apple", "Mango"];\nlet i = fruits.indexOf("Apple");',
        [("i", "i")],
        "**0**.",
    ),
    _ref(
        "isarray",
        "isArray() — is this an array?",
        "`Array.isArray(fruits)`.",
        FR + "\nArray.isArray(fruits);",
        [("Array.isArray(fruits)", "Array.isArray(fruits)")],
        "**true**.",
    ),
    _ref(
        "join",
        "join() — elements to a string",
        'Join with **" * "**.',
        FR + '\nlet text = fruits.join(" * ");',
        [("text", "text")],
        "**Banana * Orange * Apple * Mango**.",
    ),
    _ref(
        "keys",
        "keys() — iterator of indexes",
        "`Array.from(fruits.keys())`.",
        FR + "\nconst keys = Array.from(fruits.keys());",
        [("keys", "JSON.stringify(keys)")],
        "**[0,1,2,3]**.",
    ),
    _ref(
        "lastindexof",
        "lastIndexOf() — last position",
        'Last index of **"Apple"**.',
        'const fruits = ["Apple", "Orange", "Apple", "Mango"];\nlet i = fruits.lastIndexOf("Apple");',
        [("i", "i")],
        "**2**.",
    ),
    _ref(
        "length",
        "length — number of elements",
        "Read `fruits.length`.",
        FR + "\nlet n = fruits.length;",
        [("n", "n")],
        "**4**.",
    ),
    _ref(
        "map",
        "map() — new array from a function",
        "Double each number.",
        "const doubled = [4, 9, 16].map(v => v * 2);",
        [("doubled", "JSON.stringify(doubled)")],
        "**[8,18,32]**.",
    ),
    _ref(
        "of",
        "of() — array from arguments",
        "`Array.of(7)` is **`[7]`**, not 7 empty slots.",
        "const a = Array.of(7);\nconst b = Array.of(1, 2, 3);",
        [("a", "JSON.stringify(a)"), ("b", "JSON.stringify(b)")],
        "**[7]** and **[1,2,3]**.",
    ),
    _ref(
        "pop",
        "pop() — remove last, return it",
        "Pop mango off fruits.",
        FR + "\nlet fruit = fruits.pop();",
        [("fruit", "fruit"), ("fruits", "JSON.stringify(fruits)")],
        '**Mango**. fruits **["Banana","Orange","Apple"]**.',
    ),
    S(
        "prototype",
        "prototype — add a method (this page only)",
        [
            "`Array.prototype` can add methods. Prefer **not** to ship prototype pollution.",
            "A tiny `last()` helper **in this sandbox file only**.",
        ],
        """Array.prototype.last = function () {
  return this[this.length - 1];
};
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit = fruits.last();""",
        [("fruit", "fruit")],
        '**Mango**. Isolated to this file — do not add this to shared pages.',
    ),
    _ref(
        "push",
        "push() — add at the end, return length",
        'Push **"Kiwi"** and capture the new length.',
        FR + '\nlet n = fruits.push("Kiwi");',
        [("n", "n"), ("fruits", "JSON.stringify(fruits)")],
        'length **5**. **["Banana","Orange","Apple","Mango","Kiwi"]**.',
    ),
    _ref(
        "reduce",
        "reduce() — fold left to right",
        "Sum [45, 4, 9, 16, 25].",
        NUMS + "\nlet sum = numbers.reduce((t, v) => t + v);",
        [("sum", "sum")],
        "**99**.",
    ),
    _ref(
        "reduceright",
        "reduceRight() — fold right to left",
        "Same sum from the other end.",
        NUMS + "\nlet sum = numbers.reduceRight((t, v) => t + v);",
        [("sum", "sum")],
        "**99**.",
    ),
    _ref(
        "reverse",
        "reverse() — reverse in place",
        "Reverse fruits.",
        FR + "\nfruits.reverse();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Mango","Apple","Orange","Banana"]**.',
    ),
    _ref(
        "shift",
        "shift() — remove first, return it",
        "Shift banana off fruits.",
        FR + "\nlet fruit = fruits.shift();",
        [("fruit", "fruit"), ("fruits", "JSON.stringify(fruits)")],
        '**Banana**. fruits **["Orange","Apple","Mango"]**.',
    ),
    _ref(
        "slice",
        "slice() — copy a part",
        "`slice(1, 3)` is up to but not including 3.",
        FR5 + "\nconst citrus = fruits.slice(1, 3);",
        [("citrus", "JSON.stringify(citrus)")],
        '**["Orange","Lemon"]**.',
    ),
    _ref(
        "some",
        "some() — any pass a test?",
        "`some(v => v > 18)` on [4, 9, 16, 25, 29].",
        N18 + "\nlet ok = numbers.some(v => v > 18);",
        [("ok", "ok")],
        "**true**.",
    ),
    _ref(
        "sort",
        "sort() — sort the elements",
        "Default alphabetic sort.",
        FR + "\nfruits.sort();",
        [("fruits", "JSON.stringify(fruits)")],
        '**["Apple","Banana","Mango","Orange"]**.',
    ),
    _ref(
        "splice",
        "splice() — add or remove in place",
        'Insert Lemon and Kiwi at 2, delete 0.',
        FR + '\nfruits.splice(2, 0, "Lemon", "Kiwi");',
        [("fruits", "JSON.stringify(fruits)")],
        '**["Banana","Orange","Lemon","Kiwi","Apple","Mango"]**.',
    ),
    _ref(
        "toreversed",
        "toReversed() — reverse to a new array",
        "Non-mutating reverse.",
        MONTHS + "\nconst reversed = months.toReversed();",
        [
            ("reversed", "JSON.stringify(reversed)"),
            ("months", "JSON.stringify(months)"),
        ],
        '**["Apr","Mar","Feb","Jan"]**. Original unchanged.',
    ),
    _ref(
        "tosorted",
        "toSorted() — sort to a new array",
        "Non-mutating sort.",
        MONTHS + "\nconst sorted = months.toSorted();",
        [
            ("sorted", "JSON.stringify(sorted)"),
            ("months", "JSON.stringify(months)"),
        ],
        '**["Apr","Feb","Jan","Mar"]**. Original unchanged.',
    ),
    _ref(
        "tospliced",
        "toSpliced() — splice to a new array",
        "Non-mutating splice: drop index 0.",
        MONTHS + "\nconst spliced = months.toSpliced(0, 1);",
        [
            ("spliced", "JSON.stringify(spliced)"),
            ("months", "JSON.stringify(months)"),
        ],
        '**["Feb","Mar","Apr"]**. Original unchanged.',
    ),
    _ref(
        "tostring",
        "toString() — array as a string",
        "Comma-separated values.",
        FR + "\nlet text = fruits.toString();",
        [("text", "text")],
        "**Banana,Orange,Apple,Mango**.",
    ),
    _ref(
        "unshift",
        "unshift() — add at the start, return length",
        'Unshift **"Lemon"**.',
        FR + '\nlet n = fruits.unshift("Lemon");',
        [("n", "n"), ("fruits", "JSON.stringify(fruits)")],
        'length **5**. **["Lemon","Banana","Orange","Apple","Mango"]**.',
    ),
    _ref(
        "valueof",
        "valueOf() — primitive value of the array",
        "`valueOf()` returns **the array itself**. Stringifying it matches `toString`.",
        FR + "\nfruits.valueOf() === fruits;\nString(fruits.valueOf());",
        [
            ("fruits.valueOf() === fruits", "fruits.valueOf() === fruits"),
            ("String(fruits.valueOf())", "String(fruits.valueOf())"),
        ],
        "`=== fruits` is **true**. String is **Banana,Orange,Apple,Mango**.",
    ),
    _ref(
        "with",
        "with() — new array with an updated index",
        'Replace index 2 with **"March"** without mutating.',
        'const months = ["Januar", "Februar", "Mar", "April"];\nconst next = months.with(2, "March");',
        [
            ("next", "JSON.stringify(next)"),
            ("months", "JSON.stringify(months)"),
        ],
        '**["Januar","Februar","March","April"]**. Original still **"Mar"**.',
    ),
]


# ---------------------------------------------------------------------------
# 11.8 JS Array const
# ---------------------------------------------------------------------------

CONST = [
    S(
        "const-declare",
        "Declare an array with const",
        [
            "ES6 made **`const`** the usual way to declare arrays.",
        ],
        CARS,
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "const-reassign-error",
        "ERROR cannot reassign a const array",
        [
            "`const` binds the **reference**. Replacing the whole array throws **TypeError**.",
        ],
        'const cars = ["Saab", "Volvo", "BMW"];\ncars = ["Toyota", "Volvo", "Audi"]; // ERROR',
        outcome="**TypeError: Assignment to constant variable.**",
        script=catch_script(
            'const cars = ["Saab", "Volvo", "BMW"];',
            'cars = ["Toyota", "Volvo", "Audi"];',
        ),
    ),
    S(
        "const-mutate-ok",
        "Elements can be changed; push is allowed",
        [
            "`const` is **not** a frozen array. You may change indexes and `push`.",
        ],
        CARS + '\ncars[0] = "Toyota";\ncars.push("Audi");',
        [("cars", "JSON.stringify(cars)")],
        '**["Toyota","Volvo","BMW","Audi"]**.',
    ),
    S(
        "const-no-init",
        "ERROR const without initializer",
        [
            "`const cars;` is a **SyntaxError**. It must be assigned **when declared**.",
            "Caught with **`new Function`** so this page can still load.",
        ],
        "const cars;\ncars = [\"Saab\", \"Volvo\", \"BMW\"];",
        outcome="**SyntaxError: Missing initializer in const declaration** (caught via `new Function`).",
        script=nf_script("const cars;\ncars = [\"Saab\", \"Volvo\", \"BMW\"];"),
    ),
    S(
        "var-hoist-init",
        "var can be used before the declaration",
        [
            "`var` is **hoisted**. Assigning before `var cars` is allowed.",
        ],
        'cars = ["Saab", "Volvo", "BMW"];\nvar cars;',
        [("cars", "JSON.stringify(cars)")],
        '**["Saab","Volvo","BMW"]**.',
    ),
    S(
        "const-block-scope",
        "const has block scope",
        [
            "An inner `const cars` **shadows** the outer one only **inside `{ }`**.",
        ],
        """const cars = ["Saab", "Volvo", "BMW"];
let inside;
{
  const cars = ["Toyota", "Volvo", "BMW"];
  inside = cars[0];
}
let outside = cars[0];""",
        [("inside", "inside"), ("outside", "outside")],
        'Inside the block **"Toyota"**. After the block **"Saab"**.',
    ),
    S(
        "var-no-block-scope",
        "var does not have block scope",
        [
            "Inner `var cars` **overwrites** the outer one.",
        ],
        """var cars = ["Saab", "Volvo", "BMW"];
let inside;
{
  var cars = ["Toyota", "Volvo", "BMW"];
  inside = cars[0];
}
let outside = cars[0];""",
        [("inside", "inside"), ("outside", "outside")],
        'Both inside and after the block: **"Toyota"**.',
    ),
    S(
        "var-redeclare-ok",
        "var may be redeclared and reassigned",
        [
            "Redeclaring `var` in the same scope is **allowed**.",
        ],
        """var cars = ["Volvo", "BMW"];
var cars = ["Toyota", "BMW"];
cars = ["Volvo", "Saab"];""",
        [("cars", "JSON.stringify(cars)")],
        '**["Volvo","Saab"]**.',
    ),
    S(
        "var-then-const-error",
        "ERROR var then const in the same scope",
        [
            "The page’s “Not allowed” block: `const cars` after `var cars` is a **SyntaxError**.",
        ],
        'var cars = ["Volvo", "BMW"];\nconst cars = ["Volvo", "BMW"]; // Not allowed',
        outcome="**SyntaxError: Identifier 'cars' has already been declared** (caught via `new Function`).",
        script=nf_script(
            'var cars = ["Volvo", "BMW"];\nconst cars = ["Volvo", "BMW"];'
        ),
    ),
    S(
        "const-redeclare-error",
        "ERROR redeclare or reassign const in the same scope",
        [
            "Second `const cars` in the same scope is a **SyntaxError**.",
        ],
        'const cars = ["Volvo", "BMW"];\nconst cars = ["Volvo", "BMW"]; // Not allowed',
        outcome="**SyntaxError: Identifier 'cars' has already been declared** (caught via `new Function`).",
        script=nf_script(
            'const cars = ["Volvo", "BMW"];\nconst cars = ["Volvo", "BMW"];'
        ),
    ),
    S(
        "const-other-blocks-ok",
        "const in another block is allowed",
        [
            "Each block may declare its **own** `const cars`.",
        ],
        """const cars = ["Volvo", "BMW"];
let inner1;
let inner2;
{
  const cars = ["Toyota", "BMW"];
  inner1 = JSON.stringify(cars);
}
{
  const cars = ["Saab", "Audi"];
  inner2 = JSON.stringify(cars);
}
let outer = JSON.stringify(cars);""",
        [("inner1", "inner1"), ("inner2", "inner2"), ("outer", "outer")],
        'Inner blocks **["Toyota","BMW"]** and **["Saab","Audi"]**. Outer still **["Volvo","BMW"]**.',
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-arrays",
            "JS Arrays",
            ARRAYS,
            "An array is an ordered, zero-indexed list of elements under one name. Literals use square brackets; you can also start empty and assign by index, or use new Array. Elements are heterogeneous: numbers, strings, objects, functions, and nested arrays can share one list. Arrays are objects (typeof is object), so Array.isArray or instanceof Array is how you recognize them. JavaScript has no associative array — named indexes do not create a list, they just add object properties and leave length at 0.",
            [
                "Prefer an array **literal** `[]`. `const` is the usual declaration.",
                "Indexes start at **0**. `length` is one more than the highest index.",
                "`typeof` an array is **`object`**. Use **`Array.isArray`** (or `instanceof Array`).",
                "Writing a **high index** or using **`delete`** leaves empty holes.",
                "Named indexes do **not** make associative arrays — use an **object** for string keys.",
                "One array may hold **objects, functions, and nested arrays**.",
            ],
            [
                ("How do you create an array?", ["An array literal: `const cars = [\"Saab\", \"Volvo\", \"BMW\"]`.", "`new Array(...)` works but `[]` is preferred."]),
                ("What is cars[0] for that list?", ["**\"Saab\"**. Indexes start at **0**."]),
                ("Does const stop you changing cars[0]?", ["**No.** `cars[0] = \"Opel\"` becomes **[\"Opel\",\"Volvo\",\"BMW\"]**."]),
                ("What does fruits.toString() print?", ["**Banana,Orange,Apple,Mango** (commas, no spaces)."]),
                ("What is typeof fruits?", ["**object**. Arrays are objects."]),
                ("How do you test for an array?", ["**Array.isArray(fruits)** is **true**.", "`fruits instanceof Array` is also **true**."]),
                ("What happens if you set fruits[6] = \"Lemon\" on a 3-item list?", ["length becomes **7**. Indexes 3–5 are **holes**.", "JSON.stringify shows **null** in the holes; `3 in fruits` is **false**."]),
                ("What if you use person[\"firstName\"] on []?", ["length stays **0**. `person[0]` is **undefined**.", "JavaScript does **not** have associative arrays."]),
                ("Can an array hold a function?", ["**Yes.** This demo stores `Date.now`, a function, and a nested cars array."]),
                ("How do you loop?", ["A `for` from 0 to length-1, or `forEach`."]),
                ("How do you append?", ["`push(\"Lemon\")` or `fruits[fruits.length] = \"Lemon\"`."]),
                ("How do you recognize nested car models?", ["Objects inside `cars`, each with a `models` array. Loop both levels."]),
            ],
            "Use [] and numbered indexes. length, push, and loops cover everyday list work. Trust Array.isArray, not typeof. Keep string keys on objects, not on arrays. Holes from high indexes or delete are real empty slots even when JSON prints null.",
            [
                ("JS Arrays (W3Schools)", "https://www.w3schools.com/js/js_arrays.asp"),
                ("MDN: Array", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
                ("MDN: Array.isArray", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray"),
            ],
        ),
        (
            "js-array-constructor",
            "JS Array Constructor",
            CONSTRUCTOR,
            "The Array constructor creates an Array object. new Array() and Array() are the same: if you forget new, the function puts it back. A single numeric argument is a length (empty slots), not an element — that is the dangerous case. A single non-number, or any list of two or more arguments, becomes elements. An array literal avoids the trap: [40] is one number, new Array(40) is forty holes.",
            [
                "`new Array()` and `Array()` are **functionally the same**.",
                "`new Array(n)` for a number `n` makes **n empty slots**, not `[n]`.",
                '`new Array("3")` is **["3"]** — a string is not a length.',
                "Two or more arguments are **elements**: `new Array(40, 100, 1)` is `[40,100,1]`.",
                "Prefer **`[]`**. It is clearer and skips the single-number trap.",
                "`JSON.stringify` shows holes as **null**, but `0 in a` is **false**.",
            ],
            [
                ("Is Array() different from new Array()?", ["**No.** Omitting `new` is corrected internally."]),
                ("What is new Array()?", ["An **empty** array `[]`, length **0**."]),
                ("What is new Array(3)?", ["length **3** with **empty slots**.", "JSON looks like [null,null,null]; `0 in a` is **false**."]),
                ("What is new Array(\"3\")?", ["**[\"3\"]**, length **1**."]),
                ("What is new Array(40, 100, 1)?", ["**[40,100,1]**, three elements."]),
                ("What is new Array(40, 100)?", ["**[40,100]**, two elements."]),
                ("What is new Array(40)?", ["**40 empty slots**, not `[40]`."]),
                ("What is [40]?", ["**One** element, the number 40."]),
                ("Why prefer []?", ["Faster to type, easier to read, no single-number trap."]),
                ("Does new Array(40, 100, 1, 5, 25, 10) match the literal?", ["**Yes.** Both **[40,100,1,5,25,10]**."]),
            ],
            "Use []. Reach for new Array only when you understand the single-number length rule. Array() without new is not a different constructor — it is the same function filling in new for you.",
            [
                ("JS Array Constructor (W3Schools)", "https://www.w3schools.com/js/js_array_constructor.asp"),
                ("MDN: Array() constructor", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array"),
            ],
        ),
        (
            "js-array-methods",
            "JS Array Methods",
            METHODS,
            "Basic array methods cover length, string conversion, indexed reads, join, stack operations at both ends, concat, copyWithin, flattening, and splice versus slice. pop, push, shift, unshift, splice, and copyWithin mutate; concat, slice, flat, flatMap, and toSpliced return new arrays. delete leaves a hole. slice arguments are different Tryits: slice(1), slice(3), slice(1,3), and slice(2) are four examples. at() matches bracket indexing for positive indexes and also supports negatives, which fruits[-1] does not.",
            [
                "`length` can be **read or set**. Setting it truncates.",
                "`at(i)` matches `arr[i]` for **≥ 0**. `at(-1)` is the last item; `arr[-1]` is not.",
                "`pop`/`push` work on the **end**. `shift`/`unshift` work on the **front**. They return the item or the new length.",
                "`concat`, `slice`, `flat`, `flatMap`, `toSpliced` are **non-mutating**.",
                "`splice` and `copyWithin` **mutate**. `delete` leaves a hole — prefer splice.",
                "`slice(start, end)` excludes **end**. Omitting end copies the rest.",
            ],
            [
                ("What is fruits.length on four fruits?", ["**4**. Setting `length = 2` leaves **Banana, Orange**."]),
                ("at(2) vs fruits[2]?", ["Both **Apple** for this list."]),
                ("What is fruits[-1] vs fruits.at(-1)?", ["`[-1]` is **undefined** (property \"-1\").", "`at(-1)` is **Mango**."]),
                ("What does join(\" * \") print?", ["**Banana * Orange * Apple * Mango**."]),
                ("What does pop return?", ["**Mango**, leaving three fruits."]),
                ("What does push(\"Kiwi\") return?", ["The new length **5**."]),
                ("What does shift return?", ["**Banana**."]),
                ("What does unshift(\"Lemon\") return?", ["The new length **5**."]),
                ("What does delete fruits[0] do?", ["A hole: JSON **null** at [0], length still **4**."]),
                ("Does concat change the originals?", ["**No.** It returns a new array."]),
                ("copyWithin(2, 0) on four fruits?", ["**[\"Banana\",\"Orange\",\"Banana\",\"Orange\"]**."]),
                ("slice(1, 3) on Banana, Orange, Lemon, Apple, Mango?", ["**[\"Orange\",\"Lemon\"]**."]),
                ("toSpliced(0, 1) on months?", ["**[\"Feb\",\"Mar\",\"Apr\"]**. Original months stay."]),
                ("flatMap(x => [x, x*10]) on 1..6?", ["**[1,10,2,20,3,30,4,40,5,50,6,60]**."]),
            ],
            "Mutating methods change the same array; slicing, concatenating, flattening, and toSpliced give you a new one. delete is not a real remove. Remember the four slice argument sets and that at() is how you index from the end.",
            [
                ("JS Array Methods (W3Schools)", "https://www.w3schools.com/js/js_array_methods.asp"),
                ("MDN: Array.prototype", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
                ("MDN: Array.prototype.at", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at"),
                ("MDN: Array.prototype.splice", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice"),
            ],
        ),
        (
            "js-array-search",
            "JS Array Search",
            SEARCH,
            "Search methods find a position, a boolean, or the element that passes a test. indexOf and lastIndexOf return indexes (the page adds 1 to show a 1-based position). includes is a boolean and is the way to detect NaN. find / findIndex walk from the start; findLast / findLastIndex walk from the end (ES2023).",
            [
                "`indexOf` / `lastIndexOf` return an **index** or **-1**.",
                "The W3Schools Tryits add **`+ 1`** so the first Apple is position **1**.",
                "`includes` is **true/false** and can see **NaN** (indexOf cannot).",
                "`find` returns a **value**; `findIndex` returns an **index**.",
                "`findLast` / `findLastIndex` start at the **end** (ES2023).",
                "find callbacks receive **value, index, array**.",
            ],
            [
                ("Where is the first Apple, as the page prints it?", ["indexOf is **0**, plus 1 → position **1**."]),
                ("Where is the last Apple, as the page prints it?", ["lastIndexOf is **2**, plus 1 → position **3**."]),
                ("Does fruits include Mango?", ["**true**."]),
                ("indexOf(NaN) vs includes(NaN)?", ["indexOf **−1**. includes **true**."]),
                ("find first number > 18 in [4,9,16,25,29]?", ["**25**."]),
                ("findIndex of that value?", ["**3**."]),
                ("findLast x > 40 in [27,28,30,40,42,35,30]?", ["**42**."]),
                ("findLastIndex of that value?", ["**4**."]),
                ("What if find has no match?", ["**undefined**. findIndex returns **−1**."]),
                ("Does includes need a callback?", ["**No.** It takes the search item. find* take a test function."]),
            ],
            "Use indexOf for a first index, lastIndexOf for a last index, includes for a boolean (including NaN), and the find family when the test is a function. findLast* start from the end.",
            [
                ("JS Array Search (W3Schools)", "https://www.w3schools.com/js/js_array_search.asp"),
                ("MDN: Array.prototype.indexOf", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf"),
                ("MDN: Array.prototype.includes", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes"),
                ("MDN: Array.prototype.find", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find"),
            ],
        ),
        (
            "js-array-sort",
            "JS Array Sort",
            SORT,
            "sort and reverse mutate. toSorted and toReversed (ES2023) return new arrays. Default sort is alphabetic, which orders numbers as strings (1, 10, 100, 25, 40, 5). A compare function return a-b for numeric ascending and b-a for descending. Random compare is a biased shuffle; Fisher–Yates is the fair one. Min and max can come from a sorted end, Math.min.apply, or a homemade loop. Object arrays sort by a property. After ES2019, sort is stable.",
            [
                "Default `sort` is **string** order and **mutates**.",
                "`toSorted` / `toReversed` keep the original (ES2023).",
                "Numeric sort needs `function(a,b){return a-b}` (or `b-a`).",
                "Random `0.5 - Math.random()` is **biased**; use **Fisher–Yates**.",
                "Min/max: sorted ends, `Math.min.apply`, or a loop from `Infinity`.",
                "Object sort compares a **property**. ES2019 `sort` is **stable**.",
            ],
            [
                ("fruits.sort() on Banana, Orange, Apple, Mango?", ["**Apple, Banana, Mango, Orange**."]),
                ("reverse without sort?", ["**Mango, Apple, Orange, Banana**."]),
                ("sort then reverse?", ["**Orange, Mango, Banana, Apple**."]),
                ("toSorted on Jan Feb Mar Apr?", ["**Apr, Feb, Jan, Mar**. months unchanged."]),
                ("Numeric a-b on [40,100,1,5,25,10]?", ["**[1,5,10,25,40,100]**."]),
                ("Default sort of those numbers?", ["**[1,10,100,25,40,5]** — string order."]),
                ("Is the random sort fair?", ["**No.** Fisher–Yates is the fair shuffle. Both still run; the printed order is **random**."]),
                ("Math.min.apply on that list?", ["**1**. Math.max.apply is **100**."]),
                ("Homemade min / max?", ["**1** and **100**, looping from Infinity / -Infinity."]),
                ("Sort cars by year?", ["Saab 2001, BMW 2010, Volvo 2016."]),
                ("Sort cars by type?", ["BMW, Saab, Volvo."]),
                ("Is sort stable?", ["**Yes** since ES2019. X00–X03 stay in order among price 100."]),
            ],
            "Default sort is alphabetic. Pass a-b for numbers. Prefer toSorted when you need a copy. Shuffle with Fisher–Yates, not a random compare. For a single min or max, a loop or Math.min beats sorting the whole array. Object sorts compare a field; equal keys keep their order.",
            [
                ("JS Array Sort (W3Schools)", "https://www.w3schools.com/js/js_array_sort.asp"),
                ("MDN: Array.prototype.sort", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort"),
                ("MDN: Array.prototype.toSorted", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted"),
            ],
        ),
        (
            "js-array-iterations",
            "JS Array Iterations",
            ITERATIONS,
            "Iteration methods walk every item. for...of yields values (recommended). for...in yields indexes and is meant for objects. forEach, map, filter, every, and some take a callback with value, index, and array — extra parameters can be dropped. map/filter return new arrays; reduce/reduceRight fold to one value (optional initial). Array.from builds from an iterable or from a mapped list. keys and entries are iterators. with() updates one index on a copy. Spread expands; rest collects.",
            [
                "`for...of` is for **values**. `for...in` is for **keys** — skip it on arrays.",
                "`map` / `filter` / `flatMap` return **new** arrays. `forEach` returns **undefined**.",
                "`reduce` is left-to-right; `reduceRight` is right-to-left. An initial value is optional.",
                "`every` needs **all** matches; `some` needs **any**.",
                "`Array.from` copies iterables; optional map runs per element.",
                "`...` spread expands; `...` rest in destructuring **collects** leftovers.",
                "ES2023 `with(i, value)` updates one index on a **copy**.",
            ],
            [
                ("for...of on BMW, Volvo, Mini?", ["**BMW,Volvo,Mini,**"]),
                ("for...in on the same array?", ["Indexes **0,1,2,** — not the names."]),
                ("map * 2 on [45,4,9,16,25]?", ["**[90,8,18,32,50]**."]),
                ("filter > 18?", ["**[45,25]**."]),
                ("reduce sum? With initial 100?", ["**99**. With 100: **199**."]),
                ("every > 18? some > 18?", ["every **false**. some **true**."]),
                ("Array.from(\"ABCDEFG\")?", ["**[\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\"]**."]),
                ("Array.from([1,2,3,4], x => x*2)?", ["**[2,4,6,8]**."]),
                ("keys() loop?", ["**0 1 2 3**."]),
                ("entries() stringified in a loop?", ["**0,Banana1,Orange2,Apple3,Mango**."]),
                ("with(2, \"March\") on Januar, Februar, Mar, April?", ["Mar becomes **March** on the copy."]),
                ("Spread [1,2,3] and [4,5,6]?", ["**[1,2,3,4,5,6]**."]),
                ("Math.min(...[23,55,21,87,56])?", ["**21**. max is **87**."]),
                ("[a, ...rest] on 1..8?", ["a **1**, rest **[2,3,4,5,6,7,8]**."]),
                ("[a, b, ...rest]?", ["a **1**, b **2**, rest **[3,4,5,6,7,8]**."]),
            ],
            "Prefer for...of and the dedicated methods. map and filter copy; reduce folds; every/some test. from, keys, entries, with, spread, and rest round out iteration without a C-style index if you do not need one.",
            [
                ("JS Array Iterations (W3Schools)", "https://www.w3schools.com/js/js_array_iteration.asp"),
                ("MDN: Array iteration methods", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods"),
                ("MDN: Array.prototype.map", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map"),
                ("MDN: Spread syntax", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax"),
            ],
        ),
        (
            "js-array-reference",
            "JS Array Reference",
            REFERENCE,
            "The complete Array reference table (revised July 2025) lists every constructor form and instance method on this page. Each row is its own Example. Literals and new Array() both create arrays. at, concat, copyWithin, fill, and the find/filter/map/reduce family do what their tutorial chapters already showed, collected here as one catalog. of(7) is [7], unlike new Array(7). prototype is demonstrated with a tiny last() helper on this sandbox page only. valueOf returns the array itself. toReversed, toSorted, toSpliced, and with are the non-mutating ES2023 copies.",
            [
                "**Every table row is an Example** — 45 rows including `[]` and `new Array()`.",
                "`Array.of(7)` is **[7]**; `new Array(7)` is seven holes.",
                "Mutating: copyWithin, fill, pop, push, reverse, shift, sort, splice, unshift.",
                "Copying: concat, slice, toReversed, toSorted, toSpliced, with, map, filter, flat*.",
                "`valueOf()` is the array itself. `constructor` is **Array**.",
                "`Array.prototype` add-ons belong in a demo file only.",
            ],
            [
                ("How many table rows?", ["**45**, each with its own Example."]),
                ("[] vs new Array()?", ["Both create arrays. `[]` is the empty literal; `new Array()` is the empty constructor."]),
                ("What does constructor print?", ["`function Array() { [native code] }`. `=== Array` is **true**."]),
                ("Array.of(7)?", ["**[7]**, not seven empty slots."]),
                ("fill(\"Kiwi\") on four fruits?", ["**[\"Kiwi\",\"Kiwi\",\"Kiwi\",\"Kiwi\"]**."]),
                ("filter > 18 on [4,9,16,25,29]?", ["**[25,29]**."]),
                ("What does the prototype demo add?", ["`last()` → **Mango** on that page only."]),
                ("valueOf() === fruits?", ["**true**. String(valueOf()) is the comma list."]),
                ("toSorted vs sort?", ["toSorted returns a **new** array. sort mutates."]),
                ("with(2, \"March\")?", ["A copy with index 2 replaced. Original unchanged."]),
                ("entries() as JSON?", ["**[[0,\"Banana\"],[1,\"Orange\"],[2,\"Apple\"],[3,\"Mango\"]]**."]),
                ("reduce sum of [45,4,9,16,25]?", ["**99**."]),
            ],
            "Treat this page as the catalog: construct with [] or Array.of, mutate with splice/push/sort, copy with slice/toSpliced/with, and fold with reduce. Keep prototype experiments in the demo file.",
            [
                ("JS Array Reference (W3Schools)", "https://www.w3schools.com/js/js_array_reference.asp"),
                ("MDN: Array", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
                ("MDN: Array.of", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of"),
            ],
        ),
        (
            "js-array-const",
            "JS Array const",
            CONST,
            "const is the usual way to declare arrays since ES6. It is a constant reference, not a frozen list: you may change elements and push, but you may not assign a new array to that name. const requires an initializer (a parse-time SyntaxError otherwise). const is block-scoped, so an inner const cars does not overwrite the outer one; var does. Redeclaring var is allowed. Redeclaring const, or mixing var and const for the same name in one scope, is a SyntaxError. A const in another block is a different binding.",
            [
                "`const` locks the **binding**, not the **contents**.",
                "Reassigning the array is a **TypeError**. `const cars;` is a **SyntaxError**.",
                "`cars[0] = ...` and `cars.push(...)` are **allowed**.",
                "`const` is **block-scoped**. `var` is not — inner `var` leaks.",
                "`var` may be redeclared. `const` may not, in the same scope.",
                "Parse-time SyntaxErrors are compiled with **`new Function`** so the sandbox can catch them.",
            ],
            [
                ("Can you reassign a const array?", ["**No.** **TypeError: Assignment to constant variable.**"]),
                ("Can you change cars[0] or push?", ["**Yes.** This demo becomes **[\"Toyota\",\"Volvo\",\"BMW\",\"Audi\"]**."]),
                ("What is const cars; then assign?", ["**SyntaxError: Missing initializer in const declaration**."]),
                ("Can var be assigned before the declaration?", ["**Yes.** Hoisting: `cars = [...]; var cars;` works."]),
                ("Does an inner const cars change the outer one?", ["**No.** Inside **Toyota**, outside **Saab**."]),
                ("Does an inner var cars change the outer one?", ["**Yes.** Both read **Toyota**."]),
                ("Can you redeclare var?", ["**Yes.** Last assignment wins: **[\"Volvo\",\"Saab\"]**."]),
                ("var then const in the same scope?", ["**SyntaxError: Identifier 'cars' has already been declared**."]),
                ("Two const cars in one scope?", ["The same **SyntaxError**."]),
                ("Two const cars in different blocks?", ["**Allowed.** Each block has its own binding; the outer array stays."]),
                ("Why new Function for some errors?", ["A raw `<script>` with a SyntaxError **does not parse**, so the page would be blank."]),
            ],
            "Declare arrays with const. Mutate elements freely; never reassign the binding. Initialize at the declaration. Use blocks when you need a second const of the same name. Leave var for the hoisting demos — it is not block-scoped and it lets you redeclare.",
            [
                ("JS Array Const (W3Schools)", "https://www.w3schools.com/js/js_array_const.asp"),
                ("MDN: const", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const"),
                ("MDN: Array", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
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

