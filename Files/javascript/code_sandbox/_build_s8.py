"""S8: JS Objects through JS Object Constructors."""
from __future__ import annotations

from _gen_lib import S, build_and_snap


# ---------------------------------------------------------------------------
# 8.1 JS Objects (study path)
# ---------------------------------------------------------------------------

OBJECTS = [
    S(
        "javascript-objects",
        "JavaScript Objects",
        [
            "An **object** stores **values** (properties) and **functions** (methods) together.",
            "`type` is a property. `start` is a method — call it with `()`.",
        ],
        'const car = {\n  type: "Fiat",\n  start: function () {\n    return "started";\n  }\n};',
        [("car.type", "car.type"), ("car.start()", "car.start()")],
        'car.type is **"Fiat"**. car.start() returns **"started"**.',
    ),
    S(
        "object-properties",
        "Object Properties",
        [
            "Objects are collections of **properties** you can **change**, **add**, and **delete**.",
            "After `delete car.color`, that key is gone (`undefined` if you read it).",
        ],
        'const car = { type: "Fiat", color: "white" };\ncar.type = "Volvo";\ncar.model = "500";\ndelete car.color;',
        [
            ("car.type", "car.type"),
            ("car.model", "car.model"),
            ("car.color", "car.color"),
            ('"color" in car', '"color" in car'),
        ],
        'type is **"Volvo"**, model is **"500"**, color is **undefined**, and `"color" in car` is **false**.',
    ),
    S(
        "object-methods",
        "Object Methods",
        [
            "A **method** is a function stored as a property.",
            "Call it with **parentheses**: `car.start()`.",
        ],
        'const car = {\n  start: function () {\n    return "started";\n  }\n};\nlet msg = car.start();',
        [("msg", "msg"), ("typeof car.start", "typeof car.start")],
        'msg is **"started"**. `typeof car.start` is **"function"**.',
    ),
    S(
        "object-this",
        "Object this",
        [
            "Inside a method, **`this`** is the object that owns the method.",
            "`this.firstName` reads the `firstName` property of that object.",
        ],
        'const person = {\n  firstName: "John",\n  greet: function () {\n    return this.firstName;\n  }\n};',
        [("person.greet()", "person.greet()")],
        'person.greet() is **"John"** because `this` is `person`.',
    ),
    S(
        "object-display",
        "Object Display",
        [
            "Putting an object in a string context shows **[object Object]**.",
            "Show **named properties**, or use **`JSON.stringify`**.",
        ],
        'const person = { name: "John", age: 30 };\nlet asObject = String(person);\nlet named = person.name + ", " + person.age;\nlet json = JSON.stringify(person);',
        [("String(person)", "asObject"), ("named", "named"), ("JSON.stringify", "json")],
        'String(person) is **[object Object]**. Named: **"John, 30"**. JSON: **{"name":"John","age":30}**.',
    ),
    S(
        "object-constructors",
        "Object Constructors",
        [
            "A **constructor** is a function that builds many objects of the same type.",
            "`new Person(\"John\")` creates an object with `this.firstName = first`.",
        ],
        'function Person(first) {\n  this.firstName = first;\n}\nconst p = new Person("John");',
        [("p.firstName", "p.firstName"), ("p instanceof Person", "p instanceof Person")],
        'p.firstName is **"John"**. `p instanceof Person` is **true**.',
    ),
]


# ---------------------------------------------------------------------------
# 8.2 Object Intro
# ---------------------------------------------------------------------------

INTRO = [
    S(
        "car-literal",
        "const car = { type, model, color }",
        [
            "`type`, `model`, and `color` are **properties**.",
            '`"Fiat"`, `"500"`, and `"white"` are the **property values**.',
        ],
        'const car = { type: "Fiat", model: "500", color: "white" };',
        [("car.type", "car.type"), ("car.model", "car.model"), ("car.color", "car.color")],
        'car is a Fiat **500** that is **white**.',
    ),
    S(
        "person-one-line",
        "Example 1: person object on one line",
        [
            "An **object literal** is curly braces with `key: value` pairs.",
            "The page also shows the same `{firstName:\"John\", ...}` literal without a variable — this Example is that object assigned to `person`.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};',
        [
            ("person.firstName", "person.firstName"),
            ("person.lastName", "person.lastName"),
            ("person.age", "person.age"),
            ("person.eyeColor", "person.eyeColor"),
        ],
        'person is **John Doe**, age **50**, eyeColor **blue**.',
    ),
    S(
        "person-multiline",
        "Example 2: person object multiline",
        [
            "Spaces and line breaks do **not** change the object.",
            "The same literal as Example 1, written across several lines.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n};',
        [
            ("person.firstName", "person.firstName"),
            ("person.age", "person.age"),
            ("person.eyeColor", "person.eyeColor"),
        ],
        "Same object as Example 1: **John**, **50**, **blue**.",
    ),
    S(
        "empty-then-add",
        "Example 3: empty object then add properties",
        [
            "You can start with `{}` and **assign** properties afterward.",
            "Declare objects with **`const`** — the binding stays, the contents can change.",
        ],
        'const person = {};\nperson.firstName = "John";\nperson.lastName = "Doe";\nperson.age = 50;\nperson.eyeColor = "blue";',
        [
            ("person.firstName", "person.firstName"),
            ("person.lastName", "person.lastName"),
            ("person.age", "person.age"),
            ("person.eyeColor", "person.eyeColor"),
        ],
        "After adding keys, person is again **John Doe**, **50**, **blue**.",
    ),
    S(
        "new-object",
        "Example 4: new Object({...})",
        [
            "`new Object({...})` can wrap a literal, but you **do not need** `new Object()`.",
            "For readability, simplicity, and speed, **prefer an object literal** `{}`.",
        ],
        'const person = new Object({\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  eyeColor: "blue"\n});',
        [
            ("person.firstName", "person.firstName"),
            ("person instanceof Object", "person instanceof Object"),
        ],
        'Works, and `instanceof Object` is **true** — but a literal is the usual choice.',
    ),
    S(
        "dot-notation",
        "Dot notation: person.firstName",
        [
            "Read a property with **`objectName.propertyName`**.",
            "`person.firstName` is the value of the `firstName` key.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};\nlet name = person.firstName;',
        [("name", "name")],
        'name is **"John"**.',
    ),
    S(
        "bracket-notation",
        "Bracket notation: person[\"firstName\"]",
        [
            "The other way is **`objectName[\"propertyName\"]`**.",
            "Brackets are required when the key is in a **variable** or is not a valid identifier.",
        ],
        'const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};\nlet name = person["firstName"];',
        [("name", "name")],
        'name is **"John"** — same value as the dot form.',
    ),
    S(
        "method-fullname",
        "Method fullName with this",
        [
            "A **method** is a function stored as a property.",
            "Inside the method, **`this`** is the object (`person`).",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  fullName: function () {\n    return this.firstName + " " + this.lastName;\n  }\n};',
        [("person.fullName()", "person.fullName()")],
        'person.fullName() is **"John Doe"**.',
    ),
    S(
        "objects-are-king",
        "Objects are king — typeof primitives vs objects",
        [
            "Almost everything in JavaScript is an object except **primitives**.",
            "There are **7 primitives**: string, number, bigint, boolean, undefined, symbol, null. `typeof null` is the well-known **\"object\"** quirk.",
        ],
        'const primitives = [\n  typeof "John",\n  typeof 3.14,\n  typeof 10n,\n  typeof true,\n  typeof undefined,\n  typeof Symbol("id"),\n  typeof null\n];\nconst objects = [\n  typeof {x: 1},\n  typeof [1, 2],\n  typeof new Date(),\n  typeof Math,\n  typeof new Map(),\n  typeof new Set(),\n  typeof /()/,\n  typeof new Error("e"),\n  typeof function () {}\n];',
        [
            ("primitives", 'primitives.join(", ")'),
            ("objects", 'objects.join(", ")'),
        ],
        'Primitives: **string, number, bigint, boolean, undefined, symbol, object** (`null`). Objects (and **function**): **object** except a function, whose typeof is **"function"**.',
    ),
]


# ---------------------------------------------------------------------------
# 8.3 Object Properties
# ---------------------------------------------------------------------------

PROPERTIES = [
    S(
        "dot-access",
        "Dot: person.firstName + age",
        [
            "Dot notation: `person.firstName` and `person.age`.",
            "The W3Schools Tryit writes `person.firstname` (lowercase **n**). This object uses **`firstName`**, so that page spelling would be **undefined** — we use `firstName`.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nlet text = person.firstName + " is " + person.age;',
        [("text", "text")],
        'text is **"John is 50"**.',
    ),
    S(
        "bracket-access",
        "Bracket: person[\"firstName\"] + age",
        [
            '`person["firstName"]` is the same value as `person.firstName`.',
            "The page again uses `firstname` in the Tryit — we keep **`firstName`** so the result is not undefined.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nlet text = person["firstName"] + " is " + person["age"];',
        [("text", "text")],
        'text is **"John is 50"**.',
    ),
    S(
        "variable-names",
        "Property names in variables (page typo + fix)",
        [
            "Brackets can take a **variable** that holds the key name.",
            "The page runs `person[n2] + \" \" + person[n2]` (both **n2**) — that prints **Doe Doe**. The clarifying row uses `n1` then `n2`.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nlet n1 = "firstName";\nlet n2 = "lastName";\nlet name = person[n2] + " " + person[n2];\nlet clarified = person[n1] + " " + person[n2];',
        [("page: person[n2] + person[n2]", "name"), ("clarifying: person[n1] + person[n2]", "clarified")],
        'Page code is **"Doe Doe"**. Clarifying example is **"John Doe"**.',
    ),
    S(
        "expression-access",
        "Expression access: person[x]",
        [
            "The third access form is **`objectName[expression]`**.",
            "If `x` holds `\"age\"`, then `person[x]` is `person.age`. This is the named construct from the page (not the n1/n2 Tryit).",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nlet x = "age";\nlet age = person[x];',
        [("x", "x"), ("age", "age")],
        'x is **"age"**; age is **50**.',
    ),
    S(
        "change-age",
        "person.age = 10",
        [
            "Assign a new value to **change** a property.",
            "`person.age = 10` overwrites **50**.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nperson.age = 10;',
        [("person.age", "person.age")],
        "person.age is **10**.",
    ),
    S(
        "add-nationality",
        "person.nationality = \"English\"",
        [
            "Assigning a **new name** adds a property.",
            "`nationality` did not exist before this line.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nperson.nationality = "English";',
        [("person.nationality", "person.nationality")],
        'person.nationality is **"English"**.',
    ),
    S(
        "delete-dot",
        "delete person.age",
        [
            "`delete` removes **both** the value and the property.",
            "Reading it afterward is **undefined**. `\"age\" in person` is **false**.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\ndelete person.age;',
        [("person.age", "person.age"), ('"age" in person', '"age" in person')],
        "person.age is **undefined**. `\"age\" in person` is **false**.",
    ),
    S(
        "delete-bracket",
        "delete person[\"age\"]",
        [
            "The same delete with **bracket** notation.",
            "The page repeats delete with `person[\"age\"]` — same outcome as the dot form.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\ndelete person["age"];',
        [("person.age", "person.age"), ('"age" in person', '"age" in person')],
        "person.age is **undefined**. `\"age\" in person` is **false**.",
    ),
    S(
        "in-operator",
        '"firstName" in person',
        [
            "The **`in`** operator is **true** if the property exists (own or inherited).",
            "This Tryit’s person has `firstName` and `lastName` only — no `age`.",
        ],
        'const person = { firstName: "John", lastName: "Doe" };\nlet hasFirst = ("firstName" in person);\nlet hasAge = ("age" in person);',
        [("firstName in person", "hasFirst"), ("age in person", "hasAge")],
        '`"firstName" in person` is **true**. `"age" in person` is **false**.',
    ),
    S(
        "nested-dot",
        "Nested: myObj.myCars.car2",
        [
            "A property value can be **another object**.",
            "Chain dots: `myObj.myCars.car2`.",
        ],
        'const myObj = {\n  name: "John",\n  age: 30,\n  myCars: {\n    car1: "Ford",\n    car2: "BMW",\n    car3: "Fiat"\n  }\n};',
        [("myObj.myCars.car2", "myObj.myCars.car2")],
        'myObj.myCars.car2 is **"BMW"**.',
    ),
    S(
        "nested-dot-bracket",
        "Nested: myObj.myCars[\"car2\"]",
        [
            "Mix **dot** on the outer object with **brackets** on the inner key.",
            "Useful when the inner name is not a valid identifier.",
        ],
        'const myObj = {\n  name: "John",\n  age: 30,\n  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" }\n};',
        [('myObj.myCars["car2"]', 'myObj.myCars["car2"]')],
        'Still **"BMW"**.',
    ),
    S(
        "nested-brackets",
        "Nested: myObj[\"myCars\"][\"car2\"]",
        [
            "Both levels can use **brackets**.",
            "Equivalent to the mixed form above.",
        ],
        'const myObj = {\n  name: "John",\n  age: 30,\n  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" }\n};',
        [('myObj["myCars"]["car2"]', 'myObj["myCars"]["car2"]')],
        'Still **"BMW"**.',
    ),
    S(
        "nested-variables",
        "Nested: myObj[p1][p2]",
        [
            "Store each key in a variable, then chain **bracket** access.",
            "`p1` is `\"myCars\"`, `p2` is `\"car2\"`.",
        ],
        'const myObj = {\n  name: "John",\n  age: 30,\n  myCars: { car1: "Ford", car2: "BMW", car3: "Fiat" }\n};\nlet p1 = "myCars";\nlet p2 = "car2";\nlet car = myObj[p1][p2];',
        [("car", "car")],
        'car is **"BMW"**.',
    ),
]


# ---------------------------------------------------------------------------
# 8.4 Object Methods
# ---------------------------------------------------------------------------

METHODS = [
    S(
        "person-fullname",
        "person with fullName method",
        [
            "Methods are **functions stored as property values**.",
            "The page repeats this same `fullName` object later as Example 2 under The this Keyword — shown once here.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  fullName: function () {\n    return this.firstName + " " + this.lastName;\n  }\n};',
        [("person.fullName()", "person.fullName()")],
        'person.fullName() is **"John Doe"**.',
    ),
    S(
        "getid-this",
        "getId using this.id",
        [
            "In the method, **`this`** is `person`.",
            "`this.id` means the `id` property of that object.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  id: 5566,\n  getId: function () {\n    return this.id;\n  }\n};\nlet number = person.getId();',
        [("number", "number")],
        "number is **5566**.",
    ),
    S(
        "call-with-parens",
        "person.fullName() call",
        [
            "Call a method with **parentheses**: `objectName.methodName()`.",
            "Parentheses **execute** the function.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  fullName: function () {\n    return this.firstName + " " + this.lastName;\n  }\n};\nlet name = person.fullName();',
        [("name", "name")],
        'name is **"John Doe"**.',
    ),
    S(
        "without-parens",
        "person.fullName without ()",
        [
            "Without `()` you get the **function itself**, not the return value.",
            "`String(person.fullName)` shows the function text.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  fullName: function () {\n    return this.firstName + " " + this.lastName;\n  }\n};\nlet name = person.fullName;',
        [("typeof name", "typeof name"), ("String(name)", "String(name)")],
        '`typeof name` is **"function"**. The string form is the function source, not **"John Doe"**.',
    ),
    S(
        "add-method",
        "Add method: person.name = function () {...}",
        [
            "Assign a function to a property to **add a method**.",
            "`person.name` then behaves like any other method.",
        ],
        'const person = { firstName: "John", lastName: "Doe", age: 50 };\nperson.name = function () {\n  return this.firstName + " " + this.lastName;\n};',
        [("person.name()", "person.name()")],
        'person.name() is **"John Doe"**.',
    ),
    S(
        "touppercase-method",
        "toUpperCase inside a method",
        [
            "A method body can call **other** methods, such as `toUpperCase()`.",
            "The full name is built, then converted to uppercase.",
        ],
        'const person = { firstName: "John", lastName: "Doe" };\nperson.name = function () {\n  return (this.firstName + " " + this.lastName).toUpperCase();\n};',
        [("person.name()", "person.name()")],
        'person.name() is **"JOHN DOE"**.',
    ),
]


# ---------------------------------------------------------------------------
# 8.5 Object this
# ---------------------------------------------------------------------------

THIS = [
    S(
        "fullname-this",
        "fullName with this",
        [
            "`this.firstName` is the `firstName` of the **owner object**.",
            "`this.lastName` is that object’s `lastName`.",
        ],
        'const person = {\n  firstName: "John",\n  lastName: "Doe",\n  age: 50,\n  fullName: function () {\n    return this.firstName + " " + this.lastName;\n  }\n};',
        [("person.fullName()", "person.fullName()")],
        'person.fullName() is **"John Doe"**.',
    ),
    S(
        "hello-two-people",
        "person1.hello() vs person2.hello()",
        [
            "`this` lets the **same method pattern** work on different objects.",
            "The page only prints `person1.hello()`. This demo shows **both** greetings.",
        ],
        'const person1 = {\n  name: "John",\n  hello: function () {\n    return "Hello " + this.name;\n  }\n};\nconst person2 = {\n  name: "Anna",\n  hello: function () {\n    return "Hello " + this.name;\n  }\n};',
        [("person1.hello()", "person1.hello()"), ("person2.hello()", "person2.hello()")],
        'person1.hello() is **"Hello John"**. person2.hello() is **"Hello Anna"**.',
    ),
    S(
        "this-alone",
        "this alone (global / window)",
        [
            "Used **alone**, `this` is the **global object**.",
            "In a browser that object is **`window`**. The page assigns `let x = this` and displays it.",
        ],
        "let x = this;",
        outcome="`String(this)` is **[object Window]**. `this === window` is **true** in this non-strict classic script.",
        script="""      let x = this;
      document.getElementById("demo").innerText =
        "String(this) -> " + String(x) + "\\n" +
        "this === window -> " + (x === window);""",
    ),
    S(
        "this-in-function",
        "this in a regular function (non-strict)",
        [
            "In a **regular function** (not a method), `this` is also the global object when you are **not** in strict mode.",
            "`myFunction()` therefore returns **`window`** here.",
        ],
        "function myFunction() {\n  return this;\n}\nlet x = myFunction();",
        outcome="`String(this)` is **[object Window]**. `this === window` is **true** (non-strict).",
        script="""      function myFunction() {
        return this;
      }
      let x = myFunction();
      document.getElementById("demo").innerText =
        "String(this) -> " + String(x) + "\\n" +
        "this === window -> " + (x === window);""",
    ),
    S(
        "strict-this",
        '"use strict" function: this is undefined',
        [
            "Clarifying extra: the page notes that in **strict mode**, `this` used alone is **undefined**.",
            'A function that starts with `"use strict"` does **not** get `window` as `this`.',
        ],
        'function strictThis() {\n  "use strict";\n  return this;\n}\nlet x = strictThis();',
        outcome="`strictThis()` is **undefined**. `typeof this` is **undefined**.",
        script="""      function strictThis() {
        "use strict";
        return this;
      }
      let x = strictThis();
      document.getElementById("demo").innerText =
        "strict this -> " + String(x) + "\\n" +
        "typeof this -> " + typeof x;""",
    ),
]


# ---------------------------------------------------------------------------
# 8.6 Object Display
# ---------------------------------------------------------------------------

DISPLAY = [
    S(
        "object-object",
        "let text = person → [object Object]",
        [
            "Displaying an object as a string yields **[object Object]**.",
            "That is JavaScript’s default `toString` for a plain object.",
        ],
        'const person = { name: "John", age: 30, city: "New York" };\nlet text = person;',
        [("String(text)", "String(text)")],
        "String(text) is **[object Object]**.",
    ),
    S(
        "named-properties",
        "person.name + age + city",
        [
            "Build a string from **named** properties.",
            "You pick each key yourself.",
        ],
        'const person = { name: "John", age: 30, city: "New York" };\nlet text = person.name + "," + person.age + "," + person.city;',
        [("text", "text")],
        'text is **"John,30,New York"**.',
    ),
    S(
        "for-in-loop",
        "for..in loop: person[x] (not person.x)",
        [
            "`for (let x in person)` walks **keys**. You must use **`person[x]`**.",
            "`person.x` looks up a property literally named `x` — it is **undefined** each time. Clarifying row shows that mistake.",
        ],
        'const person = { name: "John", age: 30, city: "New York" };\nlet text = "";\nfor (let x in person) {\n  text += person[x] + " ";\n}\nlet wrong = "";\nfor (let x in person) {\n  wrong += person.x + " ";\n}',
        [("person[x]", "text"), ("person.x (wrong)", "wrong")],
        'Correct loop: **"John 30 New York "**. `person.x` yields **"undefined undefined undefined "**.',
    ),
    S(
        "object-values",
        "Object.values(person).toString()",
        [
            "`Object.values(person)` is an **array** of the values.",
            "`.toString()` joins them with commas.",
        ],
        'const person = { name: "John", age: 30, city: "New York" };\nconst myArray = Object.values(person);\nlet text = myArray.toString();',
        [("myArray", "JSON.stringify(myArray)"), ("text", "text")],
        'myArray is **["John",30,"New York"]**. text is **"John,30,New York"**.',
    ),
    S(
        "object-entries",
        "Object.entries fruits loop",
        [
            "`Object.entries(fruits)` gives `[key, value]` pairs.",
            "Destructure as `for (let [fruit, value] of ...)`.",
        ],
        'const fruits = { Bananas: 300, Oranges: 200, Apples: 500 };\nlet text = "";\nfor (let [fruit, value] of Object.entries(fruits)) {\n  text += fruit + ": " + value + " ";\n}',
        [("text", "text")],
        'text is **"Bananas: 300 Oranges: 200 Apples: 500 "**.',
    ),
    S(
        "json-stringify",
        "JSON.stringify(person)",
        [
            "`JSON.stringify` turns the object into a **JSON string**.",
            "Functions are omitted; this person has only data properties.",
        ],
        'const person = { name: "John", age: 30, city: "New York" };\nlet text = JSON.stringify(person);',
        [("text", "text")],
        'text is **{"name":"John","age":30,"city":"New York"}**.',
    ),
]


# ---------------------------------------------------------------------------
# 8.7 Object Constructors
# ---------------------------------------------------------------------------

_CTOR = (
    "function Person(first, last, age, eye) {\n"
    "  this.firstName = first;\n"
    "  this.lastName = last;\n"
    "  this.age = age;\n"
    "  this.eyeColor = eye;\n"
    "}"
)

CONSTRUCTORS = [
    S(
        "person-constructor",
        "function Person(...) { this.firstName = ... }",
        [
            "A constructor is an ordinary function. Name it with an **uppercase** first letter by convention.",
            "`this` has **no value** until you call it with **`new`** — then `this` is the new object.",
        ],
        _CTOR + '\nconst sample = new Person("John", "Doe", 50, "blue");',
        [
            ("typeof Person", "typeof Person"),
            ("sample.firstName", "sample.firstName"),
            ("sample.eyeColor", "sample.eyeColor"),
        ],
        '`typeof Person` is **"function"**. sample is **John** with **blue** eyes.',
    ),
    S(
        "many-persons",
        "new Person: myFather / myMother / mySister / mySelf",
        [
            "`new Person(...)` creates **many** objects of the same type.",
            "Each instance has its own `firstName`, `lastName`, `age`, and `eyeColor`.",
        ],
        _CTOR
        + "\nconst myFather = new Person(\"John\", \"Doe\", 50, \"blue\");\n"
        + "const myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "const mySister = new Person(\"Anna\", \"Rally\", 18, \"green\");\n"
        + "const mySelf = new Person(\"Johnny\", \"Rally\", 22, \"green\");",
        [
            ("myFather.firstName", "myFather.firstName"),
            ("myMother.firstName", "myMother.firstName"),
            ("mySister.firstName", "mySister.firstName"),
            ("mySelf.firstName", "mySelf.firstName"),
        ],
        "**John**, **Sally**, **Anna**, and **Johnny** — four Person objects.",
    ),
    S(
        "default-nationality",
        "Default nationality = \"English\" in the constructor",
        [
            "A value assigned in the constructor is a **default** on every new object.",
            "You do not pass `nationality` as a parameter.",
        ],
        'function Person(first, last, age, eyecolor) {\n  this.firstName = first;\n  this.lastName = last;\n  this.age = age;\n  this.eyeColor = eyecolor;\n  this.nationality = "English";\n}\nconst myFather = new Person("John", "Doe", 50, "blue");\nconst myMother = new Person("Sally", "Rally", 48, "green");',
        [
            ("myFather.nationality", "myFather.nationality"),
            ("myMother.nationality", "myMother.nationality"),
        ],
        'Both myFather and myMother have nationality **"English"**.',
    ),
    S(
        "add-property-one",
        "Add property to one object: myFather.nationality",
        [
            "Adding a property on **one instance** does not add it to the others.",
            "`myFather.nationality` is set; `myMother.nationality` stays **undefined**.",
        ],
        _CTOR
        + "\nconst myFather = new Person(\"John\", \"Doe\", 50, \"blue\");\n"
        + "const myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "myFather.nationality = \"English\";",
        [
            ("myFather.nationality", "myFather.nationality"),
            ("myMother.nationality", "myMother.nationality"),
        ],
        'myFather.nationality is **"English"**. myMother.nationality is **undefined**.',
    ),
    S(
        "person-nationality-fails",
        "Person.nationality does not add to instances",
        [
            "You **cannot** add a property to instances by assigning `Person.nationality`.",
            "That sets a property on the **function object**, not on `myFather`.",
        ],
        _CTOR
        + "\nconst myFather = new Person(\"John\", \"Doe\", 50, \"blue\");\n"
        + "Person.nationality = \"English\";",
        [
            ("Person.nationality", "Person.nationality"),
            ("myFather.nationality", "myFather.nationality"),
        ],
        'Person.nationality is **"English"**. myFather.nationality is **undefined**.',
    ),
    S(
        "prototype-nationality",
        "Person.prototype.nationality = \"English\"",
        [
            "Add a shared property on **`Person.prototype`**.",
            "Instances then **inherit** `nationality`.",
        ],
        _CTOR
        + "\nconst myFather = new Person(\"John\", \"Doe\", 50, \"blue\");\n"
        + "const myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "Person.prototype.nationality = \"English\";",
        [
            ("myFather.nationality", "myFather.nationality"),
            ("myMother.nationality", "myMother.nationality"),
        ],
        'Both instances read **"English"** from the prototype.',
    ),
    S(
        "constructor-method",
        "Constructor method: fullName",
        [
            "A constructor can assign **methods** to `this` as well as data.",
            "Each new Person gets its own `fullName` function.",
        ],
        'function Person(first, last, age, eyecolor) {\n  this.firstName = first;\n  this.lastName = last;\n  this.age = age;\n  this.eyeColor = eyecolor;\n  this.fullName = function () {\n    return this.firstName + " " + this.lastName;\n  };\n}\nconst myFather = new Person("John", "Doe", 50, "blue");',
        [("myFather.fullName()", "myFather.fullName()")],
        'myFather.fullName() is **"John Doe"**.',
    ),
    S(
        "add-method-one",
        "Add method to one object: myMother.changeName",
        [
            "Assigning a method on **one object** does not add it to the others.",
            "`myMother.changeName(\"Doe\")` changes only her `lastName`.",
        ],
        _CTOR
        + "\nconst myFather = new Person(\"John\", \"Doe\", 50, \"blue\");\n"
        + "const myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "myMother.changeName = function (name) {\n  this.lastName = name;\n};\n"
        + "myMother.changeName(\"Doe\");",
        [
            ("myMother.lastName", "myMother.lastName"),
            ("typeof myFather.changeName", "typeof myFather.changeName"),
            ("myFather.lastName", "myFather.lastName"),
        ],
        'myMother.lastName is **"Doe"**. `typeof myFather.changeName` is **"undefined"**. myFather.lastName is still **"Doe"** (his original name).',
    ),
    S(
        "person-changename-typeerror",
        "Person.changeName then myMother.changeName → TypeError",
        [
            "Assigning `Person.changeName` does **not** put the method on instances.",
            "`myMother.changeName(\"Doe\")` throws **TypeError**. Caught here so the sandbox can show the message.",
        ],
        _CTOR
        + "\nconst myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "Person.changeName = function (name) {\n  this.lastName = name;\n};\n"
        + 'myMother.changeName("Doe");',
        outcome='**TypeError: myMother.changeName is not a function** (caught). myMother.lastName stays **"Rally"**.',
        script="""      function Person(first, last, age, eye) {
        this.firstName = first;
        this.lastName = last;
        this.age = age;
        this.eyeColor = eye;
      }
      const myMother = new Person("Sally", "Rally", 48, "green");
      Person.changeName = function (name) {
        this.lastName = name;
      };
      let err;
      try {
        myMother.changeName("Doe");
      } catch (e) {
        err = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "myMother.changeName(\\"Doe\\") -> " + err + "\\n" +
        "myMother.lastName -> " + myMother.lastName;""",
    ),
    S(
        "prototype-changename",
        "Person.prototype.changeName then myMother.changeName works",
        [
            "Put the method on **`Person.prototype`** so every instance can call it.",
            "`this` inside `changeName` is `myMother` for that call.",
        ],
        _CTOR
        + "\nconst myMother = new Person(\"Sally\", \"Rally\", 48, \"green\");\n"
        + "Person.prototype.changeName = function (name) {\n  this.lastName = name;\n};\n"
        + 'myMother.changeName("Doe");',
        [("myMother.lastName", "myMother.lastName")],
        'myMother.lastName is **"Doe"** after the prototype method runs.',
    ),
    S(
        "builtin-constructors",
        "Built-in constructors (Math cannot use new)",
        [
            "JavaScript has built-in constructors: **Object, Array, Map, Set, Date, RegExp, Function**.",
            "`Math` is a global object, **not** a constructor — `new Math()` throws **TypeError** (caught).",
        ],
        "const o = new Object();\nconst a = new Array();\nconst m = new Map();\nconst s = new Set();\nconst d = new Date();\nconst r = new RegExp();\nconst f = new Function();\nnew Math();",
        outcome="Object/Array/Map/Set/Date/RegExp/Function all construct. **`new Math()` → TypeError: Math is not a constructor**.",
        script="""      const o = new Object();
      const a = new Array();
      const m = new Map();
      const s = new Set();
      const d = new Date();
      const r = new RegExp();
      const f = new Function();
      let mathErr;
      try {
        new Math();
      } catch (e) {
        mathErr = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "new Object -> " + typeof o + "\\n" +
        "new Array -> " + (a instanceof Array) + " length " + a.length + "\\n" +
        "new Map -> " + (m instanceof Map) + "\\n" +
        "new Set -> " + (s instanceof Set) + "\\n" +
        "new Date -> " + (d instanceof Date) + "\\n" +
        "new RegExp -> " + String(r) + "\\n" +
        "new Function -> " + (typeof f) + "\\n" +
        "new Math() -> " + mathErr;""",
    ),
    S(
        "literals-vs-new",
        "Literals vs new (working function expression)",
        [
            "Prefer **literals**: `{}`, `[]`, `/()/`, and a **function expression**.",
            "The page listed `function(){};` as a statement — that is a **SyntaxError**. A bare `{}` is also an empty **block**, not an object. This demo uses `const` bindings (current correct syntax).",
        ],
        'const primStr = "";\nconst primNum = 0;\nconst primBool = false;\nconst obj = {};\nconst arr = [];\nconst re = /()/;\nconst f = function () {};',
        [
            ("typeof primStr", "typeof primStr"),
            ("typeof primNum", "typeof primNum"),
            ("typeof primBool", "typeof primBool"),
            ("typeof obj", "typeof obj"),
            ("typeof arr", "typeof arr"),
            ("typeof re", "typeof re"),
            ("typeof f", "typeof f"),
        ],
        'Primitives: **string, number, boolean**. `{}` / `[]` / `/()/` are **object**. `const f = function () {}` is **"function"**.',
    ),
]


def run_all() -> None:
    sections: list[tuple] = [
        (
            "js-objects",
            "JS Objects",
            OBJECTS,
            "This study-path page is the map for JavaScript objects: what they store, how properties and methods work, what this means, how to display an object, and how constructors build many objects of one type. Each beginner step below is a small runnable demo of that idea.",
            [
                "An object holds **properties** (values) and **methods** (functions) together.",
                "You can **change, add, and delete** properties. Call methods with `()`. In a method, **`this`** is the owner object.",
                "Default display is **[object Object]** — use named properties or **`JSON.stringify`**. **`new Constructor()`** builds many similar objects.",
                "The **Advanced Objects** path (definitions, iterations, get/set, management, protection, prototypes, reference) is a later track — those chapters are not duplicated here.",
            ],
            [
                ("What does a JavaScript object store?", ["**Values** (properties) and **functions** (methods) together."]),
                ("What is `car.start()` if `start` returns `\"started\"`?", ["**\"started\"**.", "The parentheses call the method."]),
                ("How do you change, add, and delete a property?", ["Change: `car.type = \"Volvo\"`.", "Add: `car.model = \"500\"`.", "Delete: `delete car.color`."]),
                ("What is a method?", ["A **function stored as a property**.", "Call it with `()`."]),
                ("What is `this` inside a method?", ["The **object that owns** the method.", "`this.firstName` reads that object’s `firstName`."]),
                ("Why does `String(person)` show [object Object]?", ["That is the default string form of a plain object.", "Use named properties or **`JSON.stringify`** instead."]),
                ("What does `new Person(\"John\")` do if the constructor sets `this.firstName = first`?", ["Creates a Person whose `firstName` is **\"John\"**."]),
                ("Should you use `new Object()` for a simple object?", ["**No.** Prefer an object **literal** `{}` — later pages cover this."]),
                ("Why is there an Advanced Objects path?", ["For later topics: definitions, iterations, getters/setters, protection, prototypes.", "This page only introduces the beginner steps."]),
                ("Are objects important in JavaScript?", ["**Yes.** If you understand objects, you understand a large part of JavaScript."]),
            ],
            "Objects store properties and methods. Change, add, or delete keys; call methods with parentheses; use this inside methods; display with named keys or JSON; and use constructors when you need many objects of the same type. Advanced object topics are a separate path.",
            [
                ("JS Objects (W3Schools)", "https://www.w3schools.com/js/js_objects.asp"),
                ("MDN: Working with objects", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects"),
                ("MDN: Object", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"),
            ],
            4000,
        ),
        (
            "js-object-intro",
            "JS Object Intro",
            INTRO,
            "Objects are variables that store values as properties and functions as methods. The usual way to create one is an object literal: curly braces with key:value pairs. You can write that literal on one line or many, start empty and add keys, or (unnecessarily) use new Object(). Read keys with dots or brackets. Methods use this to reach the owner object. Almost everything except primitives is an object.",
            [
                "An object literal is `{ key: value, ... }` inside curly braces. Prefer **`const`** and prefer literals over **`new Object()`**.",
                "**Dot** `person.firstName` and **bracket** `person[\"firstName\"]` read the same property.",
                "A **method** is a function property. Inside it, **`this`** is the object.",
                "Seven **primitives** are not objects (except the `typeof null === \"object\"` quirk). Dates, arrays, maps, sets, regexp, errors, and Math are objects; functions have typeof **function**.",
            ],
            [
                ("What are `type`, `model`, and `color` on the car object?", ["**Properties.** Their values are **\"Fiat\"**, **\"500\"**, and **\"white\"**."]),
                ("Do one-line and multiline person literals create different objects?", ["**No.** Spaces and line breaks are not important. Both are John Doe, 50, blue."]),
                ("Can you start with `{}` and add properties later?", ["**Yes.** `person.firstName = \"John\"` adds the key."]),
                ("Do you need `new Object({...})`?", ["**No.** Use an object literal for readability, simplicity, and speed."]),
                ("How do you read `firstName` with dots vs brackets?", ["`person.firstName` and `person[\"firstName\"]` — both **\"John\"**."]),
                ("What does `person.fullName()` return?", ["**\"John Doe\"** — `this` is `person`."]),
                ("Should you declare objects with const?", ["**Yes.** The page says to declare objects with **`const`**."]),
                ("How many primitive types does JavaScript define?", ["**7:** string, number, bigint, boolean, undefined, symbol, null."]),
                ("What is `typeof null`?", ["**\"object\"** — a long-standing language quirk. `null` is still a primitive."]),
                ("What is `typeof function () {}`?", ["**\"function\"** — functions are callable objects."]),
                ("Are arrays and dates objects?", ["**Yes.** `typeof []` and `typeof new Date()` are **\"object\"**."]),
                ("What is an object method vs a property?", ["A property stores a **value**. A method stores a **function** you call with `()`."]),
            ],
            "Create objects with literals (one line, many lines, or empty then add). Skip new Object(). Read keys with dots or brackets. Methods use this. Primitives are the exception to “objects are king”; typeof null is the odd “object” among them.",
            [
                ("JS Objects intro (W3Schools)", "https://www.w3schools.com/js/js_object_intro.asp"),
                ("MDN: Object", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"),
                ("MDN: Working with objects", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects"),
                ("MDN: typeof", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof"),
            ],
            4000,
        ),
        (
            "js-object-properties",
            "JS Object Properties",
            PROPERTIES,
            "A JavaScript object is a collection of properties you can read, change, add, and delete. Access a key with a dot, with brackets, or with an expression in brackets. Nested objects chain those same forms. The in operator checks whether a key exists. Assume a person with firstName John, lastName Doe, and age 50 unless an example defines something else.",
            [
                "**Dot** `person.firstName` is preferred when the name is a valid identifier.",
                "**Brackets** `person[\"firstName\"]` or `person[x]` are required for variables and unusual names.",
                "`delete` removes the property. **`in`** tests whether it exists.",
                "The W3Schools Tryits use `person.firstname` (lowercase n). The object key is **`firstName`** — we use that so the demos are not undefined.",
            ],
            [
                ("What is `person.firstName + \" is \" + person.age`?", ["**\"John is 50\"**.", "Use `firstName` (capital N). The page’s `firstname` would be undefined."]),
                ("What is `person[\"firstName\"] + \" is \" + person[\"age\"]`?", ["**\"John is 50\"** — same as the dot form."]),
                ("What does the page’s `person[n2] + \" \" + person[n2]` print?", ["**\"Doe Doe\"** — both lookups use **n2** (`lastName`).", "Clarifying: `person[n1] + \" \" + person[n2]` is **\"John Doe\"**."]),
                ("What is `person[x]` if `x` is `\"age\"`?", ["**50** — expression access."]),
                ("What is `person.age` after `person.age = 10`?", ["**10**."]),
                ("What does `person.nationality = \"English\"` do?", ["It **adds** a new property. Value **\"English\"**."]),
                ("What is `person.age` after `delete person.age`?", ["**undefined**. `\"age\" in person` is **false**."]),
                ("Is `delete person[\"age\"]` different from `delete person.age`?", ["**No.** Same deletion; the page shows both Tryits."]),
                ("What is `\"firstName\" in person`?", ["**true** if the object has that key (this Tryit person has firstName and lastName only)."]),
                ("What is `myObj.myCars.car2`?", ["**\"BMW\"**."]),
                ("What are `myObj.myCars[\"car2\"]` and `myObj[\"myCars\"][\"car2\"]`?", ["Both **\"BMW\"**."]),
                ("What is `myObj[p1][p2]` with p1 `myCars` and p2 `car2`?", ["**\"BMW\"**."]),
                ("When must you use brackets instead of dots?", ["When the name is in a **variable**, or is not a valid identifier (for example `\"last-name\"`)."]),
                ("Does delete remove the property or only the value?", ["**Both.** The key is gone afterward."]),
            ],
            "Read properties with dots, brackets, or an expression in brackets. Change by assigning, add by assigning a new name, remove with delete, and test with in. Nested objects chain the same access forms. Watch firstName vs firstname, and the page’s n2/n2 typo.",
            [
                ("JS Object Properties (W3Schools)", "https://www.w3schools.com/js/js_object_properties.asp"),
                ("MDN: Property accessors", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors"),
                ("MDN: delete", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete"),
                ("MDN: in", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in"),
            ],
            4000,
        ),
        (
            "js-object-methods",
            "JS Object Methods",
            METHODS,
            "Methods are actions stored as functions on an object. Call them with parentheses. Skip the parentheses and you get the function itself. Inside a method, this is the owner object. You can add a method later by assigning a function to a property, and the method body can call other functions such as toUpperCase.",
            [
                "A method is a **function stored as a property**. Call it with **`()`**.",
                "Without `()` you get the **function object** (its source text if you stringify it).",
                "In a method, **`this`** is the owner — `this.id`, `this.firstName`, `this.lastName`.",
                "Add a method with `object.fn = function () { ... }`. The page’s second fullName Tryit is the same object as the first — shown once.",
            ],
            [
                ("What is `person.fullName()`?", ["**\"John Doe\"**."]),
                ("What is `person.getId()` if `id` is 5566?", ["**5566** — `this.id` is `person.id`."]),
                ("What does `this` refer to in an object method?", ["The **object** that owns the method."]),
                ("What is `let name = person.fullName()`?", ["**\"John Doe\"** — parentheses execute the method."]),
                ("What is `let name = person.fullName` (no parentheses)?", ["The **function itself**.", "`typeof name` is **\"function\"**, not the string John Doe."]),
                ("How do you add a method to an existing object?", ["Assign a function: `person.name = function () { ... }`."]),
                ("What is `person.name()` if the method uses `toUpperCase()`?", ["**\"JOHN DOE\"**."]),
                ("Are methods different from properties?", ["Methods **are** properties whose values are **functions**."]),
                ("Does the page show fullName twice?", ["**Yes.** The first Tryit and Example 2 under this are the same object — this section keeps one demo."]),
                ("What is the call syntax?", ["**`objectName.methodName()`**."]),
            ],
            "Store functions as properties and call them with parentheses. this is the owner object. Without parentheses you get the function, not the result. You can add methods later, including ones that call toUpperCase.",
            [
                ("JS Object Methods (W3Schools)", "https://www.w3schools.com/js/js_object_methods.asp"),
                ("MDN: Working with objects", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects"),
                ("MDN: this", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this"),
                ("MDN: String.prototype.toUpperCase", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase"),
            ],
            4000,
        ),
        (
            "js-object-this",
            "JS Object this",
            THIS,
            "The this keyword refers to an object. In a method it is the owner, which is why the same method pattern can greet John and Anna. Used alone, or in a regular non-strict function, this is the global object (window in a browser). In a strict-mode function, this is undefined.",
            [
                "In a **method**, `this` is the **owner object**.",
                "That is why `hello` can return **Hello John** and **Hello Anna** from two objects.",
                "Used **alone** or in a **regular non-strict function**, `this` is **`window`** in a browser.",
                'In a function with **`"use strict"`**, `this` is **undefined** (clarifying extra the page mentions).',
            ],
            [
                ("What is `person.fullName()` with this.firstName / this.lastName?", ["**\"John Doe\"**."]),
                ("What do `person1.hello()` and `person2.hello()` return?", ["**\"Hello John\"** and **\"Hello Anna\"**.", "`this.name` is each object’s own name."]),
                ("Why use this instead of writing person.name inside the method?", ["So the **same method pattern** works on **different** objects."]),
                ("What is `this` used alone in a browser script?", ["The **global object** — **`window`**.", "`String(this)` is **[object Window]**."]),
                ("Is `this === window` true at the top level of this sandbox?", ["**Yes** — the example script is not in strict mode."]),
                ("What is `this` inside `function myFunction() { return this; }` (non-strict)?", ["Also **`window`**. `myFunction() === window` is **true**."]),
                ("What is `this` in a `\"use strict\"` function?", ["**undefined**."]),
                ("Does this in a method mean the function?", ["**No.** It means the **object** that is calling the method."]),
                ("What does the page display for `let x = this`?", ["The window object, which stringifies to **[object Window]**."]),
                ("When is this not window?", ["In an **object method** (the owner), in **strict** functions (**undefined**), and in other later cases (bind, arrows) covered on advanced pages."]),
            ],
            "In a method, this is the owner object, so one method pattern can serve many objects. Alone or in a non-strict function, this is window. In a strict function, this is undefined.",
            [
                ("JS this in Objects (W3Schools)", "https://www.w3schools.com/js/js_object_this.asp"),
                ("MDN: this", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this"),
                ("MDN: Strict mode", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode"),
                ("MDN: window", "https://developer.mozilla.org/en-US/docs/Web/API/Window"),
            ],
            4000,
        ),
        (
            "js-object-display",
            "JS Object Display",
            DISPLAY,
            "If you treat an object as a string you get [object Object]. To show the contents, name the properties, loop with for..in using bracket access, convert values with Object.values, loop pairs with Object.entries, or serialize with JSON.stringify.",
            [
                "`String(person)` is **[object Object]** — the default `toString`.",
                "Name properties (`person.name`), or loop **`person[x]`** (not `person.x`).",
                "`Object.values` → array of values. `Object.entries` → `[key, value]` pairs.",
                "`JSON.stringify(person)` is a **JSON** string. Methods are not included.",
            ],
            [
                ("What is `let text = person` as a string?", ["**[object Object]**."]),
                ("What is `person.name + \",\" + person.age + \",\" + person.city`?", ["**\"John,30,New York\"**."]),
                ("In `for (let x in person)`, should you use `person.x` or `person[x]`?", ["**`person[x]`**.", "`person.x` looks up a key named `x` and is **undefined**."]),
                ("What is `Object.values(person).toString()`?", ["**\"John,30,New York\"**."]),
                ("What does the fruits `Object.entries` loop build?", ["**\"Bananas: 300 Oranges: 200 Apples: 500 \"**."]),
                ("What is `JSON.stringify(person)` for name/age/city?", ["**{\"name\":\"John\",\"age\":30,\"city\":\"New York\"}**."]),
                ("Why do you see [object Object]?", ["The object was coerced to a string, and the default `toString` does not list keys."]),
                ("Does JSON.stringify include methods?", ["**No.** Function properties are omitted."]),
                ("What does Object.values return?", ["An **array** of the object’s own enumerable **values**."]),
                ("What does Object.entries return?", ["An array of **`[key, value]`** pairs, handy in `for...of`."]),
            ],
            "Do not stringify an object directly unless you want [object Object]. Name the keys, loop with person[x], use Object.values or Object.entries, or call JSON.stringify.",
            [
                ("JS Display Objects (W3Schools)", "https://www.w3schools.com/js/js_object_display.asp"),
                ("MDN: JSON.stringify", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify"),
                ("MDN: Object.values", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values"),
                ("MDN: Object.entries", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries"),
                ("MDN: for...in", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in"),
            ],
            4000,
        ),
        (
            "js-object-constructors",
            "JS Object Constructors",
            CONSTRUCTORS,
            "When you need many objects of the same type, write a constructor function and call it with new. Defaults go in the constructor. A property or method added to one instance stays on that instance. Assigning to the constructor function itself does not add anything to instances and calling a missing method is a TypeError. Shared features belong on the prototype. Prefer literals over new Object, new Array, and friends. Math is not a constructor.",
            [
                "Name constructors with an **uppercase** first letter. Call them with **`new`** so `this` becomes the new object.",
                "A value set in the constructor is a **default** on every instance. A value set on **one object** is only for that object.",
                "`Person.nationality = ...` or `Person.changeName = ...` does **not** add to instances. Use **`Person.prototype`**. Otherwise **TypeError**.",
                "Built-ins: `new Object/Array/Map/Set/Date/RegExp/Function`. **`new Math()`** throws. Prefer `{}`, `[]`, `/()/`, and `const f = function () {}` — the page’s `function(){};` statement is a **SyntaxError**.",
            ],
            [
                ("What is `new Person(\"John\", \"Doe\", 50, \"blue\").firstName`?", ["**\"John\"**. `this` in the constructor is the new object."]),
                ("Can one constructor make myFather, myMother, mySister, and mySelf?", ["**Yes.** Each `new Person(...)` is a separate object."]),
                ("What is `nationality` if the constructor sets `this.nationality = \"English\"`?", ["**\"English\"** on every new Person — a default value."]),
                ("If only `myFather.nationality = \"English\"`, what is `myMother.nationality`?", ["**undefined**. The new property is only on myFather."]),
                ("Does `Person.nationality = \"English\"` set `myFather.nationality`?", ["**No.** That property is on the **function**, not on instances. myFather.nationality is **undefined**."]),
                ("How do all instances get nationality?", ["`Person.prototype.nationality = \"English\"` — instances inherit it."]),
                ("What is `myFather.fullName()` if the constructor defines that method?", ["**\"John Doe\"**."]),
                ("If only `myMother.changeName` is assigned, can `myFather.changeName` run?", ["**No.** `typeof myFather.changeName` is **\"undefined\"**."]),
                ("What happens if you set `Person.changeName` then call `myMother.changeName(\"Doe\")`?", ["**TypeError: myMother.changeName is not a function**."]),
                ("What happens after `Person.prototype.changeName` then `myMother.changeName(\"Doe\")`?", ["It **works**. myMother.lastName becomes **\"Doe\"**."]),
                ("Which built-ins can you call with `new`?", ["**Object, Array, Map, Set, Date, RegExp, Function**.", "`new Math()` is **TypeError: Math is not a constructor**."]),
                ("Why not write `function(){};` as a statement like the page listed?", ["It is a **SyntaxError**. Use `const f = function () {};`.", "A bare `{}` as a statement is an empty **block**, not an object — assign it: `const obj = {}`."]),
                ("When does `this` get a value in a constructor?", ["When you call the function with **`new`**. Until then it has no instance value."]),
                ("Should you prefer `{}` over `new Object()`?", ["**Yes.** Also prefer `[]` over `new Array()` and `/()/` over `new RegExp()`."]),
            ],
            "Use a constructor plus new to stamp out many similar objects. Defaults belong in the constructor; shared methods and properties belong on the prototype. Assigning to the function does not update instances and calling a missing method throws TypeError. Prefer literals, and never new Math(). The page’s function(){}; list item needs a const function expression to run.",
            [
                ("JS Object Constructors (W3Schools)", "https://www.w3schools.com/js/js_object_constructors.asp"),
                ("MDN: new", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new"),
                ("MDN: Object.prototype", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype"),
                ("MDN: Inheritance and the prototype chain", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain"),
                ("MDN: Function", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function"),
            ],
            4000,
        ),
    ]
    for slug, title, recs, intro, concepts, qa, summary, refs, wait in sections:
        print("building", slug, "examples", len(recs), "wait", wait)
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs, wait=wait)
        print("done", slug)


if __name__ == "__main__":
    run_all()
