"""S7: JS Functions through JS Timers."""
from __future__ import annotations

from _gen_lib import S, build_and_snap


def _myd(body: str) -> str:
    return f"""      function myDisplayer(t) {{
        document.getElementById("demo").innerText = t;
      }}
{body}"""


# ---------------------------------------------------------------------------
# 7.1 JS Functions (study path)
# ---------------------------------------------------------------------------

FUNCTIONS = [
    S(
        "what-are-functions",
        "What are Functions?",
        [
            "A **function** is a reusable block of code for a particular task.",
            "Nothing inside the function runs until you **call** (invoke) it.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet text = sayHello();',
        [("text", "text")],
        'text is **"Hello World"** after the call.',
    ),
    S(
        "calling-functions",
        "Calling Functions",
        [
            "Call a function by writing its name plus **parentheses**: `sayHello()`.",
            "The `()` means **execute now**.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nsayHello();',
        [("sayHello()", "sayHello()")],
        "The call returns **Hello World**.",
    ),
    S(
        "function-parameters",
        "Function Parameters",
        [
            "**Parameters** are the names listed in the function definition.",
            "`multiply(a, b)` receives two inputs and returns their product.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [("result", "result")],
        "result is **20**.",
    ),
    S(
        "function-return-values",
        "Function Return Values",
        [
            "`return` sends a value **back** to the caller.",
            "Store that value in a variable to use it later.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet message = sayHello();',
        [("message", "message")],
        'message is **"Hello World"**.',
    ),
    S(
        "function-arguments",
        "Function Arguments",
        [
            "**Parameters** are names (`a`, `b`). **Arguments** are the values passed in (`4`, `5`).",
            "Argument `4` is assigned to `a`; `5` is assigned to `b`.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [
            ("parameters", '"a, b"'),
            ("arguments", '"4, 5"'),
            ("result", "result"),
        ],
        "**a, b** are parameters; **4, 5** are arguments. result is **20**.",
    ),
    S(
        "function-expressions",
        "Function Expressions",
        [
            "A **function expression** stores a function in a variable.",
            "Call it with the **variable name** plus `()`.",
        ],
        "const multiply = function(a, b) {\n  return a * b;\n};\nlet z = multiply(4, 3);",
        [("z", "z"), ("typeof multiply", "typeof multiply")],
        "z is **12**. `multiply` is a **function**.",
    ),
    S(
        "arrow-functions",
        "Arrow Functions",
        [
            "Arrow functions are a **short syntax** for function expressions.",
            "You can skip `function`, `return`, and `{}` when the body is one expression.",
        ],
        "const multiply = (a, b) => a * b;\nlet z = multiply(4, 5);",
        [("z", "z")],
        "z is **20**.",
    ),
    S(
        "function-quiz-teaser",
        "Function Quiz teaser",
        [
            "The quiz reuses the same `sayHello` example.",
            '`let text = sayHello()` stores the **returned string**, not the function name.',
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet text = sayHello();',
        [("text", "text")],
        'text is **"Hello World"** (quiz question 1, answer **B**).',
    ),
]


# ---------------------------------------------------------------------------
# 7.2 Function Intro
# ---------------------------------------------------------------------------

INTRO = [
    S(
        "defined-not-called",
        "Function defined but not called",
        [
            "A function definition is **not** an executable statement by itself.",
            "The function **exists**, but its body does not run until you call it.",
        ],
        'function sayHello() {\n  return "Hello World";\n}',
        [
            ("typeof sayHello", "typeof sayHello"),
            ("called yet?", '"no — definition only"'),
        ],
        '`typeof sayHello` is **"function"**. Nothing printed Hello World because it was never called.',
    ),
    S(
        "call-and-store",
        "Call sayHello() and store the message",
        [
            "`sayHello()` runs the body and **returns** a string.",
            "`()` means execute now. Store the result in a variable to use it.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet message = sayHello();',
        [("message", "message")],
        'message is **"Hello World"**.',
    ),
    S(
        "multiply",
        "multiply(a, b)",
        [
            "Parameters `a` and `b` sit in the parentheses of the **definition**.",
            "Function declarations usually **do not** end with a semicolon.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [("result", "result")],
        "result is **20**.",
    ),
    S(
        "add-twice",
        "add called twice (sum1, sum2)",
        [
            "The same function can run **many times** with different inputs.",
            "Returned values can be stored in different variables.",
        ],
        "function add(a, b) {\n  return a + b;\n}\nlet sum1 = add(5, 5);\nlet sum2 = add(50, 50);",
        [("sum1", "sum1"), ("sum2", "sum2")],
        "sum1 is **10**; sum2 is **100**.",
    ),
    S(
        "local-carname",
        "Local variable carName",
        [
            "Variables declared **inside** a function are **local** to that function.",
            "Outside the function, `carName` throws **ReferenceError**.",
        ],
        '// code here can NOT use carName\nfunction myFunction() {\n  let carName = "Volvo";\n  return carName;  // code here CAN use carName\n}\n// code here can NOT use carName',
        outcome="Inside the function, carName is **Volvo**. Outside, reading it throws **ReferenceError**.",
        script="""      function myFunction() {
        let carName = "Volvo";
        return carName;
      }
      let inside = myFunction();
      let outside;
      try {
        outside = carName;
      } catch (e) {
        outside = e.name + ": " + e.message;
      }
      document.getElementById("demo").innerText =
        "inside myFunction -> " + inside + "\\n" +
        "outside -> " + outside;""",
    ),
    S(
        "tocelsius-inline",
        "toCelsius used inline as a variable value",
        [
            "You can store `toCelsius(77)` in `x`, then build a string.",
            "Or use the **call itself** as a value in the expression.",
        ],
        'function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet x = toCelsius(77);\nlet text1 = "The temperature is " + x + " Celsius";\nlet text2 = "The temperature is " + toCelsius(77) + " Celsius";',
        [("text1", "text1"), ("text2", "text2"), ("toCelsius(77)", "toCelsius(77)")],
        'Both strings are **"The temperature is 25 Celsius"**. 77°F is **25**°C.',
    ),
]


# ---------------------------------------------------------------------------
# 7.3 Function Invocation
# ---------------------------------------------------------------------------

INVOCATION = [
    S(
        "defined-not-run",
        "Function defined, not run",
        [
            "The code inside a function does **not** run when it is defined.",
            "It runs when something **invokes** it (a call, an event, or an IIFE).",
        ],
        'function sayHello() {\n  return "Hello World";\n}',
        [
            ("typeof sayHello", "typeof sayHello"),
            ("body ran?", '"not yet"'),
        ],
        "The function object exists, but **Hello World** has not been produced yet.",
    ),
    S(
        "called-unused",
        "sayHello() called unused",
        [
            "This call **does** run the function.",
            "The return value is **thrown away** unless you store or display it.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nsayHello();',
        [
            ("call happened", '"yes"'),
            ("stored?", '"no"'),
            ("sayHello() again", "sayHello()"),
        ],
        "The function ran, but the first return value was unused. Calling again still returns **Hello World**.",
    ),
    S(
        "store-greeting",
        "Store the greeting",
        [
            "To **use** a returned value, assign it to a variable.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet greeting = sayHello();',
        [("greeting", "greeting")],
        'greeting is **"Hello World"**.',
    ),
    S(
        "console-log",
        "console.log(sayHello())",
        [
            "`console.log` prints the return value to the **console**.",
            "This sandbox also writes it to **#demo** so the screenshot can show it.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nconsole.log(sayHello());',
        outcome='console.log prints **"Hello World"**; #demo shows the same string.',
        script="""      function sayHello() {
        return "Hello World";
      }
      let out = sayHello();
      console.log(out);
      document.getElementById("demo").innerText = out;""",
    ),
    S(
        "innerhtml",
        "innerHTML = sayHello()",
        [
            "You can put the return value into an HTML element.",
            "`innerHTML` (or `innerText`) displays it on the page.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\ndocument.getElementById("demo").innerHTML = sayHello();',
        outcome='#demo shows **Hello World**.',
        script="""      function sayHello() {
        return "Hello World";
      }
      document.getElementById("demo").innerHTML = sayHello();""",
    ),
    S(
        "call-many-times",
        "Call many times: a, b, c",
        [
            "You can invoke the same function **whenever** you need it.",
            "Each call returns a fresh value.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet a = sayHello();\nlet b = sayHello();\nlet c = sayHello();',
        [("a", "a"), ("b", "b"), ("c", "c")],
        "a, b, and c are each **Hello World**.",
    ),
    S(
        "tocelsius-77",
        "toCelsius(77) invokes the function",
        [
            "The `()` operator **invokes** the function.",
            "`toCelsius(77)` is the **result**; `toCelsius` without `()` is the function itself.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet value = toCelsius(77);",
        [("value", "value")],
        "value is **25**.",
    ),
    S(
        "access-without-parens",
        "Access without () — the function object",
        [
            "`toCelsius` (no parentheses) returns the **function itself**, not 25.",
            "`typeof` is **function**. `String(value)` is the source text.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet value = toCelsius;",
        [
            ("typeof value", "typeof value"),
            ("String(value).slice(0, 60)", "String(value).replace(/\\s+/g, ' ').slice(0, 60)"),
            ("value === toCelsius", "value === toCelsius"),
        ],
        '`typeof value` is **"function"**. The string starts with `function toCelsius`.',
    ),
    S(
        "text-is-reference",
        "let text = sayHello (reference)",
        [
            "`sayHello` refers to the **function**. `sayHello()` refers to the **result**.",
            "`let text = sayHello` copies the function reference, not \"Hello World\".",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet text = sayHello;',
        [
            ("typeof text", "typeof text"),
            ("text()", "text()"),
            ("text === sayHello", "text === sayHello"),
        ],
        '`text` is the function. `text()` returns **"Hello World"**.',
    ),
    S(
        "showhello-wraps",
        "showHello() wrapping sayHello",
        [
            "You can call functions from **other functions**.",
            "`showHello` writes `sayHello()` into #demo.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nfunction showHello() {\n  document.getElementById("demo").innerHTML = sayHello();\n}\nshowHello();',
        outcome="#demo shows **Hello World** after `showHello()` runs.",
        script="""      function sayHello() {
        return "Hello World";
      }
      function showHello() {
        document.getElementById("demo").innerHTML = sayHello();
      }
      showHello();""",
    ),
    S(
        "button-click",
        "Button click invoking showHello",
        [
            "A function can run when an **event** occurs (a button click).",
            "This page auto-calls `showHello()` on load so the screenshot shows the result after a “click”.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nfunction showHello() {\n  document.getElementById("demo").innerHTML = sayHello();\n}',
        outcome="The button is present, and #demo shows **Hello World**.",
        script="""      function sayHello() {
        return "Hello World";
      }
      function showHello() {
        document.getElementById("demo").innerHTML = sayHello();
      }
      showHello();""",
        buttons='<p><button type="button" onclick="showHello()">Click Me</button></p>',
    ),
    S(
        "mistake-no-return",
        "Common mistake: no return",
        [
            "Some functions do **not** return a value.",
            "Storing the call then yields **undefined**.",
        ],
        'function sayHello() {\n  let msg = "Hello World";\n}\nlet text = sayHello();',
        [("text", "text")],
        "text is **undefined** because there is no `return`.",
    ),
    S(
        "mistake-no-display",
        "Common mistake: no display",
        [
            "Even with a return value, the page stays blank unless you **display** it.",
            "Store it, `console.log` it, or write it into an element.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet hidden = sayHello();\n// nothing writes hidden to the page in the original mistake',
        [
            ("hidden (if you look)", "hidden"),
            ("shown on page?", '"only because this demo prints it"'),
        ],
        "The value **Hello World** exists in `hidden`, but a page that never displays it looks empty.",
    ),
]


# ---------------------------------------------------------------------------
# 7.4 Function Parameters
# ---------------------------------------------------------------------------

PARAMS = [
    S(
        "multiply-4-5",
        "multiply(4, 5)",
        [
            "Parameters `a` and `b` receive the arguments **4** and **5**.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [("result", "result")],
        "result is **20**.",
    ),
    S(
        "sayhello-john",
        'sayHello("John") — one parameter',
        [
            "A function can have **one** parameter.",
            "The argument `\"John\"` is assigned to `name`.",
        ],
        'function sayHello(name) {\n  return "Hello " + name;\n}\nlet greeting = sayHello("John");',
        [("greeting", "greeting")],
        'greeting is **"Hello John"**.',
    ),
    S(
        "tocelsius-77",
        "toCelsius(77) — one parameter",
        [
            "`fahrenheit` is the parameter; **77** is the argument.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet value = toCelsius(77);",
        [("value", "value")],
        "value is **25**.",
    ),
    S(
        "fullname",
        'fullName("John", "Doe") — multiple parameters',
        [
            "List multiple parameters **separated by commas**.",
        ],
        'function fullName(firstName, lastName) {\n  return firstName + " " + lastName;\n}\nlet name = fullName("John", "Doe");',
        [("name", "name")],
        'name is **"John Doe"**.',
    ),
    S(
        "missing-arg-nan",
        "toCelsius() missing argument → NaN",
        [
            "JavaScript does **not** check the number of arguments.",
            "A missing parameter is **undefined**. `(5/9) * (undefined - 32)` is **NaN**.",
        ],
        "function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet value = toCelsius();",
        [("value", "value"), ("typeof fahrenheit inside", "String(value)")],
        "value is **NaN**.",
    ),
    S(
        "default-param",
        "Default parameter y = 10",
        [
            "ES2015 default parameters: if `y` is omitted or `undefined`, use **10**.",
            "`myFunction(5)` is `5 + 10`.",
        ],
        "function myFunction(x, y = 10) {\n  return x + y;\n}\nlet a = myFunction(5);\nlet b = myFunction(5, 3);",
        [("myFunction(5)", "a"), ("myFunction(5, 3)", "b")],
        "`myFunction(5)` is **15**. `myFunction(5, 3)` is **8**.",
    ),
]


# ---------------------------------------------------------------------------
# 7.5 Function Returns
# ---------------------------------------------------------------------------

RETURNS = [
    S(
        "sayhello-stored",
        "sayHello return stored",
        [
            "`return` sends a value out of the function.",
            "After the call, `message` holds that value.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet message = sayHello();',
        [("message", "message")],
        'message is **"Hello World"**.',
    ),
    S(
        "multiply-20",
        "multiply(4, 5) = 20",
        [
            "Most functions return a **calculated** value.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [("result", "result")],
        "result is **20**.",
    ),
    S(
        "multiply-in-expression",
        "multiply(2, 3) * 10 = 60",
        [
            "A function call can sit **inside another expression**.",
            "`multiply(2, 3)` returns 6, then `6 * 10` is 60.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet total = multiply(2, 3) * 10;",
        [("total", "total")],
        "total is **60**.",
    ),
    S(
        "fullname-return",
        "fullName returns a string",
        [
            "A function can return **any** type, not only numbers.",
        ],
        'function fullName(firstName, lastName) {\n  return firstName + " " + lastName;\n}\nlet name = fullName("John", "Doe");',
        [("name", "name")],
        'name is **"John Doe"**.',
    ),
    S(
        "early-return-done",
        'Early return "Done" skips a * b',
        [
            "When JavaScript hits `return`, the function **stops**.",
            "Code after `return` never runs.",
        ],
        'function multiply(a, b) {\n  return "Done";\n  return a * b;\n}\nlet result = multiply(4, 3);',
        [("result", "result")],
        'result is **"Done"**, not 12.',
    ),
    S(
        "no-return-undefined",
        "No return → undefined",
        [
            "If a function has no `return`, the result is **undefined**.",
            "Computing `a * b` inside is not enough — you must return it.",
        ],
        "function multiply(a, b) {\n  let x = a * b;\n}\nlet result = multiply(4, 3);",
        [("result", "String(result)"), ("result === undefined", "result === undefined")],
        "result is **undefined**.",
    ),
    S(
        "checkage-early",
        "checkAge early return",
        [
            "Use `return` to **leave early** on a condition.",
            "Younger than 18 gets **Too young**; otherwise **Access granted**.",
        ],
        'function checkAge(age) {\n  if (age < 18) {\n    return "Too young";\n  }\n  return "Access granted";\n}\nlet a = checkAge(15);\nlet b = checkAge(21);',
        [("checkAge(15)", "a"), ("checkAge(21)", "b")],
        '15 → **"Too young"**. 21 → **"Access granted"**.',
    ),
    S(
        "tocelsius-innerhtml",
        "toCelsius innerHTML 77",
        [
            "Returned values are often used to **update HTML**.",
        ],
        "function toCelsius(farenheit) {\n  return (5 / 9) * (farenheit - 32);\n}\ndocument.getElementById(\"demo\").innerHTML = toCelsius(77);",
        outcome="#demo shows **25**.",
        script="""      function toCelsius(farenheit) {
        return (5 / 9) * (farenheit - 32);
      }
      document.getElementById("demo").innerHTML = toCelsius(77);""",
    ),
    S(
        "console-vs-return",
        "console.log vs return",
        [
            "`console.log()` **shows** a value; it does **not** return it to the caller.",
            "A function that only logs returns **undefined** if you store the call.",
        ],
        'function onlyLog() {\n  console.log("Hello");\n}\nfunction withReturn() {\n  return "Hello";\n}\nlet x = onlyLog();\nlet y = withReturn();',
        outcome='`onlyLog()` returns **undefined**. `withReturn()` returns **"Hello"**.',
        script="""      function onlyLog() {
        console.log("Hello");
      }
      function withReturn() {
        return "Hello";
      }
      let x = onlyLog();
      let y = withReturn();
      document.getElementById("demo").innerText =
        "onlyLog() -> " + String(x) + "\\n" +
        "withReturn() -> " + y;""",
    ),
]


# ---------------------------------------------------------------------------
# 7.6 Function Arguments
# ---------------------------------------------------------------------------

ARGS = [
    S(
        "params-vs-args",
        "multiply: parameters vs arguments",
        [
            "**Parameters** are the names (`a`, `b`) in the definition.",
            "**Arguments** are the values (`4`, `5`) in the call.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [
            ("parameters", '"a, b"'),
            ("arguments", '"4, 5"'),
            ("result", "result"),
        ],
        "4 maps to `a`, 5 maps to `b`. result is **20**.",
    ),
    S(
        "findmax-arguments",
        "findMax using the arguments object",
        [
            "Every non-arrow function has a built-in **`arguments`** object.",
            "It is array-like: `arguments.length` and `arguments[i]`.",
        ],
        "function findMax() {\n  let max = -Infinity;\n  for (let i = 0; i < arguments.length; i++) {\n    if (arguments[i] > max) {\n      max = arguments[i];\n    }\n  }\n  return max;\n}\nlet x = findMax(1, 123, 500, 115, 44, 88);",
        [("x", "x")],
        "x is **500**.",
    ),
    S(
        "sumall-arguments",
        "sumAll using arguments",
        [
            "Too many arguments are still reachable via **`arguments`**.",
        ],
        "function sumAll() {\n  let sum = 0;\n  for (let i = 0; i < arguments.length; i++) {\n    sum += arguments[i];\n  }\n  return sum;\n}\nlet x = sumAll(1, 123, 500, 115, 44, 88);",
        [("x", "x")],
        "x is **871**.",
    ),
    S(
        "subtract-order",
        "subtract: order matters",
        [
            "Arguments are assigned to parameters **in order**.",
            "`subtract(10, 5)` is not `subtract(5, 10)`.",
        ],
        "function subtract(a, b) {\n  return a - b;\n}\nlet x1 = subtract(10, 5);\nlet x2 = subtract(5, 10);",
        [("subtract(10, 5)", "x1"), ("subtract(5, 10)", "x2")],
        "x1 is **5**; x2 is **-5**.",
    ),
    S(
        "variables-as-args",
        "multiply(x, y) — variables as arguments",
        [
            "Arguments do not have to be literals. They can be **variables**.",
            "The **values** of `x` and `y` are passed, not the names.",
        ],
        "let x = 5;\nlet y = 6;\nfunction multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(x, y);",
        [("result", "result")],
        "result is **30**.",
    ),
    S(
        "wrong-type-nan",
        'toCelsius("John") → NaN',
        [
            "JavaScript does **not** type-check arguments.",
            '`"John" - 32` is **NaN**, so the whole formula is NaN.',
        ],
        'function toCelsius(fahrenheit) {\n  return (5 / 9) * (fahrenheit - 32);\n}\nlet value = toCelsius("John");',
        [("value", "value")],
        "value is **NaN**.",
    ),
    S(
        "missing-arg",
        "multiply(4) missing argument → NaN",
        [
            "Fewer arguments than parameters: the rest are **undefined**.",
            "`4 * undefined` is **NaN**.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4);",
        [("result", "result"), ("b", '"undefined (missing)"')],
        "result is **NaN**.",
    ),
    S(
        "old-default",
        "Old-style default if y is undefined",
        [
            "Before default parameters, people assigned a fallback **inside** the function.",
            "If `y === undefined`, set `y = 2`.",
        ],
        "function myFunction(x, y) {\n  if (y === undefined) {\n    y = 2;\n  }\n  return x + y;\n}\nlet a = myFunction(5);\nlet b = myFunction(5, 3);",
        [("myFunction(5)", "a"), ("myFunction(5, 3)", "b")],
        "`myFunction(5)` is **7**. `myFunction(5, 3)` is **8**.",
    ),
    S(
        "default-param-y10",
        "Default parameter y = 10",
        [
            "ES2015: `y = 10` in the parameter list.",
            "Used when the argument is omitted or **undefined**.",
        ],
        "function myFunction(x, y = 10) {\n  return x + y;\n}\nlet a = myFunction(5);\nlet b = myFunction(5, undefined);\nlet c = myFunction(5, 1);",
        [("myFunction(5)", "a"), ("myFunction(5, undefined)", "b"), ("myFunction(5, 1)", "c")],
        "**15**, **15**, and **6**.",
    ),
    S(
        "rest-sum",
        "Rest parameter ...args sum",
        [
            "`...args` gathers remaining arguments into a **real array**.",
            "Prefer rest over `arguments` in new code (and rest works in arrows).",
        ],
        "function sum(...args) {\n  let total = 0;\n  for (let arg of args) total += arg;\n  return total;\n}\nlet x = sum(4, 9, 16, 25, 29, 100, 66, 77);",
        [("x", "x")],
        "x is **326**.",
    ),
    S(
        "pass-by-value",
        "Pass-by-value (number not changed outside)",
        [
            "Primitives are passed **by value**. The function gets a copy.",
            "Changing the parameter does **not** change the original variable.",
        ],
        "function addOne(n) {\n  n = n + 1;\n  return n;\n}\nlet x = 10;\nlet y = addOne(x);",
        [("x (outside)", "x"), ("y (returned)", "y")],
        "x is still **10**. y is **11**.",
    ),
    S(
        "pass-by-reference",
        "Object passed by reference (property changes outside)",
        [
            "Object **references** are values, so objects behave as pass-by-reference.",
            "Changing a **property** inside the function changes the original object.",
        ],
        'function changeName(obj) {\n  obj.name = "Jane";\n}\nlet person = {name: "John"};\nchangeName(person);',
        [("person.name", "person.name")],
        'person.name is **"Jane"** outside the function too.',
    ),
]


# ---------------------------------------------------------------------------
# 7.7 Function Expressions
# ---------------------------------------------------------------------------

EXPRS = [
    S(
        "const-multiply",
        "const multiply = function(a, b)",
        [
            "A **function expression** stores a function in a variable.",
            "The function can be **anonymous** (no name after `function`) — the variable is the name you call.",
        ],
        "const multiply = function(a, b) {\n  return a * b;\n};",
        [("typeof multiply", "typeof multiply"), ("multiply(4, 3)", "multiply(4, 3)")],
        '`typeof multiply` is **"function"**. `multiply(4, 3)` is **12**.',
    ),
    S(
        "let-z-multiply",
        "let z = multiply(4, 3)",
        [
            "After the expression is stored, the **variable** is used as the function.",
            "Named form is also allowed: `const add = function add(a, b) { ... };` — still called via the variable.",
        ],
        "const multiply = function(a, b) {\n  return a * b;\n};\nlet z = multiply(4, 3);",
        [("z", "z")],
        "z is **12**.",
    ),
    S(
        "semicolon-after",
        "Semicolon after a function expression",
        [
            "A function **declaration** is not typically ended with `;`.",
            "A function **expression** is a statement, so it **usually ends with a semicolon**.",
        ],
        "const add = function(a, b) {\n  return a + b;\n};",
        [("add(2, 3)", "add(2, 3)")],
        "add(2, 3) is **5**. Note the `;` after the closing `}`.",
    ),
    S(
        "callback-run",
        "Callback: run(fn)",
        [
            "Because an expression is a **value**, you can pass it to another function.",
            "`run(sayHello)` passes the function; `run` calls `fn()`.",
        ],
        'function run(fn) {\n  return fn();\n}\nconst sayHello = function() {\n  return "Hello";\n};\nlet result = run(sayHello);',
        [("result", "result")],
        'result is **"Hello"**.',
    ),
    S(
        "sayhello-expression",
        "sayHello expression called",
        [
            "Store the function in `sayHello`, then call **`sayHello()`**.",
            "`sayHello` is the function; `sayHello()` is the result.",
        ],
        'const sayHello = function() {\n  return "Hello World";\n};\nsayHello();',
        [("sayHello()", "sayHello()")],
        'The call returns **"Hello World"**.',
    ),
    S(
        "declaration-hoisted",
        "Function declaration is hoisted",
        [
            "A **function declaration** can be called **before** it appears in the code.",
            "Declarations are **hoisted** to the top of their scope.",
        ],
        "let sum = add(2, 3);\nfunction add(a, b) {\n  return a + b;\n}",
        [("sum", "sum")],
        "sum is **5**. The call before `function add` works.",
    ),
    S(
        "expression-not-hoisted",
        "Function expression is not hoisted",
        [
            "A `const` function expression lives in the **temporal dead zone** until that line runs.",
            "Calling `add(2, 3)` **before** `const add = function...` throws **ReferenceError**.",
        ],
        "let sum = add(2, 3);  // error\nconst add = function(a, b) {\n  return a + b;\n};",
        outcome="The early call throws **ReferenceError** (add is not initialized). After the `const` line, `add(2, 3)` would be **5**.",
        script="""      let early;
      try {
        early = add(2, 3);
      } catch (e) {
        early = e.name + ": " + e.message;
      }
      const add = function(a, b) {
        return a + b;
      };
      document.getElementById("demo").innerText =
        "before const add -> " + early + "\\n" +
        "after const add -> " + add(2, 3);""",
    ),
]


# ---------------------------------------------------------------------------
# 7.8 Arrow Functions
# ---------------------------------------------------------------------------

ARROW = [
    S(
        "multiply-arrow",
        "const multiply = (a, b) => a * b",
        [
            "Skip `function`, `return`, and `{}` when the body is one expression.",
            "The W3Schools page repeats this same Tryit under **Shorter Syntax / With Arrow** — included once.",
        ],
        "const multiply = (a, b) => a * b;\nlet z = multiply(4, 5);",
        [("z", "z")],
        "z is **20**.",
    ),
    S(
        "before-arrow",
        "Before arrow: function expression multiply",
        [
            "This is the longer **function expression** that the arrow replaces.",
        ],
        "const multiply = function(a, b) {\n  return a * b;\n};\nlet z = multiply(4, 5);",
        [("z", "z")],
        "z is also **20**.",
    ),
    S(
        "hello-no-params",
        "hello arrow with no parameters",
        [
            "Zero parameters still need **empty parentheses**: `() =>`.",
            "The page repeats this Tryit (return-by-default and no-params sections). Included once.",
        ],
        'const hello = () => "Hello World!";\nlet text = hello();',
        [("text", "text")],
        'text is **"Hello World!"**.',
    ),
    S(
        "hello-expression",
        "hello as a function expression",
        [
            "Same result without arrow syntax.",
        ],
        'const hello = function() {\n  return "Hello World!";\n};\nlet text = hello();',
        [("text", "text")],
        'text is **"Hello World!"**.',
    ),
    S(
        "square-parens",
        "square (x) => with parentheses",
        [
            "One parameter **may** keep the parentheses.",
        ],
        "const square = (x) => x * x;\nlet z = square(5);",
        [("z", "z")],
        "z is **25**.",
    ),
    S(
        "square-no-parens",
        "square x => without parentheses",
        [
            "With **exactly one** parameter, parentheses are optional.",
        ],
        "const square = x => x * x;\nlet z = square(5);",
        [("z", "z")],
        "z is **25**.",
    ),
    S(
        "hello-val-parens",
        "hello (val) => one parameter",
        [
            "`(val)` is one parameter with parentheses.",
            "The page repeats this Tryit later; included once.",
        ],
        'const hello = (val) => "Hello " + val;\nlet text = hello("World");',
        [("text", "text")],
        'text is **"Hello World"**.',
    ),
    S(
        "hello-val-no-parens",
        "hello val => one parameter, no parens",
        [
            "One parameter: you can skip `()`.",
            "The page has a stray **this** Tryit with the same code — included once.",
        ],
        'const hello = val => "Hello " + val;\nlet text = hello("World");',
        [("text", "text")],
        'text is **"Hello World"**.',
    ),
    S(
        "braces-return-variants",
        "Braces without return → undefined",
        [
            "`{ x * y }` is a **block**, not an implicit return — result is **undefined**.",
            "`=> return x * y` is a **SyntaxError** (`return` is a statement, not an expression).",
            "`{ return x * y }` works. Keep `return` when you use `{ }`.",
        ],
        "const a = (x, y) => { x * y };\n// const b = (x, y) => return x * y;  // SyntaxError\nconst c = (x, y) => { return x * y };",
        outcome="`{ x * y }` → **undefined**. `=> return` → **SyntaxError**. `{ return x * y }` → **20**.",
        script="""      let r1, r2, r3;
      try {
        r1 = String(((x, y) => { x * y })(4, 5));
      } catch (e) {
        r1 = e.name;
      }
      try {
        eval("(x, y) => return x * y");
        r2 = "parsed";
      } catch (e) {
        r2 = e.name;
      }
      try {
        r3 = String(((x, y) => { return x * y })(4, 5));
      } catch (e) {
        r3 = e.name;
      }
      document.getElementById("demo").innerText =
        "{ x * y } -> " + r1 + "\\n" +
        "=> return x * y -> " + r2 + "\\n" +
        "{ return x * y } -> " + r3;""",
    ),
    S(
        "call-before-define",
        "Calling an arrow before it is defined",
        [
            "Arrows are **expressions**, not declarations. They are **not hoisted**.",
            "`hello()` before `const hello = () => ...` throws **ReferenceError**.",
        ],
        'hello();  // Error\nconst hello = () => "Hello";',
        outcome="**ReferenceError** — cannot access `hello` before initialization. After the `const`, `hello()` is **Hello**.",
        script="""      let early;
      try {
        early = hello();
      } catch (e) {
        early = e.name + ": " + e.message;
      }
      const hello = () => "Hello";
      document.getElementById("demo").innerText =
        "before const -> " + early + "\\n" +
        "after const -> " + hello();""",
    ),
    S(
        "method-this-function",
        'Method this with function() → "John"',
        [
            "A regular method has its own **`this`**: the object that owns the call.",
            "`person.greet()` sets `this` to `person`.",
        ],
        'const person = {\n  name: "John",\n  greet: function() {\n    return this.name;\n  }\n};\nlet text = person.greet();',
        [("text", "text")],
        'text is **"John"**.',
    ),
    S(
        "method-this-arrow",
        "Method this with arrow → not John",
        [
            "Arrow functions do **not** have their own `this`.",
            "They inherit `this` from the surrounding scope (here, the window/global), so `this.name` is **not** `\"John\"`.",
        ],
        'const person = {\n  name: "John",\n  greet: () => {\n    return this.name;\n  }\n};\nlet text = person.greet();',
        [
            ("text", "String(text)"),
            ("text === 'John'", "text === 'John'"),
            ("typeof text", "typeof text"),
        ],
        '`person.greet()` is **not** `"John"` (empty string or undefined on the global `this`). Do not use arrows as methods.',
    ),
]


# ---------------------------------------------------------------------------
# 7.9 Function Quiz
# ---------------------------------------------------------------------------

QUIZ = [
    S(
        "q1-hello-world",
        "Q1: What is returned in text? → B Hello World",
        [
            "**Answer B.** `sayHello()` runs and returns the string.",
            "A would be the function itself (`sayHello` without `()`). C would mean no return.",
        ],
        'function sayHello() {\n  return "Hello World";\n}\nlet text = sayHello();',
        [("text", "text"), ("answer", '"B"')],
        'text is **"Hello World"**. Correct choice: **B**.',
    ),
    S(
        "q2-which-line-calls",
        "Q2: Which line calls the function? → C let y = test()",
        [
            "**Answer C.** Parentheses **execute** the function.",
            "`let x = test` only copies the function reference.",
        ],
        "function test() {\n  return 5;\n}\nlet x = test;\nlet y = test();",
        [
            ("typeof x", "typeof x"),
            ("y", "y"),
            ("answer", '"C"'),
        ],
        '`x` is a **function**; `y` is **5**. Correct choice: **C**.',
    ),
    S(
        "q3-parameters",
        "Q3: What are a and b? → B Parameters",
        [
            "**Answer B.** Parameters are the **names** in the definition.",
            "Arguments would be the values in a call such as `multiply(4, 5)`.",
        ],
        "function multiply(a, b) {\n  return a * b;\n}\nlet result = multiply(4, 5);",
        [
            ("a and b are", '"parameters"'),
            ("4 and 5 are", '"arguments"'),
            ("result", "result"),
            ("answer", '"B"'),
        ],
        "a and b are **parameters**. Correct choice: **B**.",
    ),
    S(
        "q4-fifty",
        "Q4: What is x? → C 50",
        [
            "**Answer C.** `add(2, 3)` returns **5**, then `5 * 10` is **50**.",
        ],
        "function add(a, b) {\n  return a + b;\n}\nlet x = add(2, 3) * 10;",
        [("x", "x"), ("answer", '"C"')],
        "x is **50**. Correct choice: **C**.",
    ),
    S(
        "q5-undefined",
        "Q5: No return statement → C undefined",
        [
            "**Answer C.** A function without `return` yields **undefined**.",
            "Not `null`, not `false`.",
        ],
        "function multiply(a, b) {\n  let x = a * b;\n}\nlet result = multiply(4, 3);",
        [
            ("result", "String(result)"),
            ("answer", '"C"'),
        ],
        "result is **undefined**. Correct choice: **C**.",
    ),
    S(
        "q6-declaration-hoisted",
        "Q6: Called before defined? → A Function declaration",
        [
            "**Answer A.** Only **function declarations** are hoisted as callable functions.",
            "Expressions and arrows cannot be called before their `const`/`let` line.",
        ],
        "let fromDecl = add(2, 3);\nfunction add(a, b) {\n  return a + b;\n}",
        outcome="Declaration call works: **5**. Expression call before `const` is **ReferenceError**. Correct choice: **A**.",
        script="""      let fromDecl = add(2, 3);
      function add(a, b) {
        return a + b;
      }
      let fromExpr;
      try {
        fromExpr = extra(2, 3);
      } catch (e) {
        fromExpr = e.name;
      }
      const extra = function(a, b) {
        return a + b;
      };
      document.getElementById("demo").innerText =
        "declaration add(2, 3) -> " + fromDecl + "\\n" +
        "expression before const -> " + fromExpr + "\\n" +
        "answer -> A";""",
    ),
    S(
        "q7-arrow-correct",
        "Q7: Which arrow is correct? → C const add = (a, b) => a + b",
        [
            "**Answer C.** A single expression after `=>` is the implicit return.",
            "A is a SyntaxError (`return` in an expression body). B is missing parentheses around two params.",
        ],
        "const add = (a, b) => a + b;\nlet x = add(2, 3);",
        outcome="C runs: **5**. A is **SyntaxError**. B is **SyntaxError**. Correct choice: **C**.",
        script="""      let a, b, c;
      try {
        eval("const add = (a, b) => return a + b");
        a = "parsed";
      } catch (e) {
        a = e.name;
      }
      try {
        eval("const add = a, b => a + b");
        b = "parsed";
      } catch (e) {
        b = e.name;
      }
      const add = (a, b) => a + b;
      c = add(2, 3);
      document.getElementById("demo").innerText =
        "A (=> return) -> " + a + "\\n" +
        "B (a, b =>) -> " + b + "\\n" +
        "C add(2, 3) -> " + c + "\\n" +
        "answer -> C";""",
    ),
    S(
        "q8-this-owner",
        "Q8: What does this refer to in a method? → C The object that owns the method",
        [
            "**Answer C.** In `person.getName`, `this` is **person**.",
            "Not the function itself, and not (for a method call) the global object.",
        ],
        'const person = {\n  name: "John",\n  getName: function() {\n    return this.name;\n  }\n};\nlet text = person.getName();',
        [("text", "text"), ("answer", '"C"')],
        'text is **"John"**. Correct choice: **C**.',
    ),
    S(
        "q9-arrow-this",
        "Q9: Why does the arrow method fail? → B Arrow functions do not have their own this",
        [
            "**Answer B.** Arrows inherit `this` from the surrounding scope.",
            "They **can** return values, and the object syntax is fine.",
        ],
        'const person = {\n  name: "John",\n  greet: () => this.name\n};\nlet text = person.greet();',
        [
            ("text", "String(text)"),
            ("is John?", "text === 'John'"),
            ("answer", '"B"'),
        ],
        '`greet()` is **not** `"John"`. Correct choice: **B**.',
    ),
]


# ---------------------------------------------------------------------------
# 7.10 JS Timers
# ---------------------------------------------------------------------------

TIMERS = [
    S(
        "four-timer-functions",
        "The four timer functions",
        [
            "`setTimeout()` runs a function **once** after a delay.",
            "`setInterval()` runs a function **repeatedly**.",
            "`clearTimeout()` / `clearInterval()` cancel those timers.",
        ],
        "setTimeout(fn, ms);\nsetInterval(fn, ms);\nclearTimeout(id);\nclearInterval(id);",
        outcome="The table is listed. A 0 ms timeout then writes **ready** to show setTimeout works.",
        script=_myd("""      let lines = [
        "setTimeout() — run once after a delay",
        "setInterval() — run repeatedly",
        "clearTimeout() — cancel a timeout",
        "clearInterval() — stop an interval"
      ];
      myDisplayer(lines.join("\\n"));
      setTimeout(function() {
        lines.push("setTimeout(0) fired — ready");
        myDisplayer(lines.join("\\n"));
      }, 0);
"""),
        wait_ms=2000,
    ),
    S(
        "settimeout-hello",
        "setTimeout myFunction 3000 → Hello!",
        [
            "`setTimeout(myFunction, 3000)` runs **once** after **3000** ms (3 seconds).",
            "Pass the **function name**, not `myFunction()`.",
        ],
        'setTimeout(myFunction, 3000);\nfunction myFunction() {\n  myDisplayer("Hello!");\n}',
        outcome='#demo shows **Hello!** after the delay.',
        script=_myd("""      setTimeout(myFunction, 3000);
      function myFunction() {
        myDisplayer("Hello!");
      }
"""),
        wait_ms=7000,
    ),
    S(
        "pass-name-vs-call",
        "Correct vs incorrect: pass the name, not myFunction()",
        [
            "**Correct:** `setTimeout(myFunction, 3000)` — the engine calls it later.",
            "**Incorrect:** `setTimeout(myFunction(), 3000)` — it runs **immediately**, and `undefined` is passed as the callback.",
        ],
        "setTimeout(myFunction, 3000);     // correct\nsetTimeout(myFunction(), 3000);   // incorrect — runs now",
        outcome="The incorrect call runs **immediately**. The correct call would wait.",
        script=_myd("""      let lines = [];
      function myFunction() {
        lines.push("myFunction ran");
        myDisplayer(lines.join("\\n"));
      }
      lines.push("incorrect: setTimeout(myFunction(), 3000)");
      setTimeout(myFunction(), 3000);
      lines.push("already ran (return value passed to setTimeout was undefined)");
      lines.push("correct form: setTimeout(myFunction, 3000)");
      myDisplayer(lines.join("\\n"));
"""),
        wait_ms=2000,
    ),
    S(
        "anonymous-timeout",
        "Anonymous setTimeout 3000",
        [
            "You can pass an **anonymous** function as the callback.",
        ],
        'setTimeout(function() {\n  myDisplayer("Hello!");\n}, 3000);',
        outcome='#demo shows **Hello!**.',
        script=_myd("""      setTimeout(function() {
        myDisplayer("Hello!");
      }, 3000);
"""),
        wait_ms=7000,
    ),
    S(
        "start-end-timer",
        "Start / End / Timer order",
        [
            "`setTimeout` does **not** pause JavaScript.",
            "The next statement runs immediately, so the order is **Start End Timer**.",
        ],
        'myDisplayer("Start");\nsetTimeout(function() { myDisplayer("Timer"); }, 3000);\nmyDisplayer("End");',
        outcome="Final accumulated order: **Start End Timer**.",
        script=_myd("""      let order = [];
      function show(msg) {
        order.push(msg);
        myDisplayer(order.join(" "));
      }
      show("Start");
      setTimeout(function() { show("Timer"); }, 3000);
      show("End");
"""),
        wait_ms=7000,
    ),
    S(
        "zero-delay",
        "Zero delay still Start End Timer",
        [
            "A delay of **0** does not mean “run now”.",
            "The callback waits until the **current task** finishes, so you still get **Start End Timer**.",
        ],
        'myDisplayer("Start");\nsetTimeout(function() { myDisplayer("Timer"); }, 0);\nmyDisplayer("End");',
        outcome="Order is still **Start End Timer**.",
        script=_myd("""      let order = [];
      function show(msg) {
        order.push(msg);
        myDisplayer(order.join(" "));
      }
      show("Start");
      setTimeout(function() { show("Timer"); }, 0);
      show("End");
"""),
        wait_ms=2000,
    ),
    S(
        "delay-is-minimum",
        "Delay is a minimum (busy loop)",
        [
            "The delay is the **earliest** the callback may run.",
            "The W3Schools page uses `let i = 4e9` (too slow for a screenshot). This demo uses **`4e7`** so the snap can finish.",
        ],
        "setTimeout(function() {\n  myDisplayer(\"Timer finished\");\n}, 1000);\nlet i = 4e7;  // page used 4e9\nwhile (--i > 0);",
        outcome="After the loop, #demo shows **Timer finished**. The callback waited for the busy loop, not just 1000 ms.",
        script=_myd("""      let t0 = Date.now();
      setTimeout(function() {
        myDisplayer("Timer finished (" + (Date.now() - t0) + " ms real; loop was 4e7, page used 4e9)");
      }, 1000);
      let i = 4e7;
      while (--i > 0);
"""),
        wait_ms=6000,
    ),
    S(
        "cleartimeout",
        "clearTimeout — Timer stopped",
        [
            "`setTimeout` returns an **id**. Pass it to `clearTimeout` to cancel.",
            "This demo auto-starts then auto-stops so the snap shows **Timer stopped**.",
        ],
        'let timer;\nfunction startTimer() {\n  timer = setTimeout(function() {\n    document.getElementById("demo").innerHTML = "Finished";\n  }, 5000);\n}\nfunction stopTimer() {\n  clearTimeout(timer);\n  document.getElementById("demo").innerHTML = "Timer stopped";\n}',
        outcome='#demo shows **Timer stopped** (the 5 s timeout never finished).',
        script="""      let timer;
      function startTimer() {
        timer = setTimeout(function() {
          document.getElementById("demo").innerText = "Finished";
        }, 5000);
      }
      function stopTimer() {
        clearTimeout(timer);
        document.getElementById("demo").innerText = "Timer stopped";
      }
      startTimer();
      stopTimer();
""",
        buttons='<p><button type="button" onclick="startTimer()">Start Timer</button> <button type="button" onclick="stopTimer()">Stop Timer</button></p>',
        wait_ms=2000,
    ),
    S(
        "setinterval-showtime",
        "setInterval showTime",
        [
            "`setInterval(showTime, 1000)` runs **every second**.",
            "Unlike `setTimeout`, it keeps repeating until you clear it.",
        ],
        "setInterval(showTime, 1000);\nfunction showTime() {\n  const date = new Date();\n  myDisplayer(date.toLocaleTimeString());\n}",
        outcome="A clock time appears in #demo.",
        script=_myd("""      setInterval(showTime, 1000);
      function showTime() {
        const date = new Date();
        myDisplayer(date.toLocaleTimeString());
      }
      showTime();
"""),
        wait_ms=2500,
    ),
    S(
        "start-stop-clock",
        "Start / stop clock (clearInterval)",
        [
            "`setInterval` returns an id. `clearInterval` **stops** it.",
            "Guard with `if (!timer)` so you do not start **multiple** intervals.",
            "Auto-started so the snap shows a time.",
        ],
        'let timer;\nfunction startClock() {\n  if (!timer) {\n    timer = setInterval(showTime, 1000);\n  }\n}\nfunction showTime() {\n  const date = new Date();\n  document.getElementById("demo").innerHTML = date.toLocaleTimeString();\n}\nfunction stopClock() {\n  clearInterval(timer);\n  timer = undefined;\n}',
        outcome="The clock is running; Stop Clock would call `clearInterval`.",
        script="""      let timer;
      function showTime() {
        const date = new Date();
        document.getElementById("demo").innerText = date.toLocaleTimeString();
      }
      function startClock() {
        if (!timer) {
          timer = setInterval(showTime, 1000);
        }
      }
      function stopClock() {
        clearInterval(timer);
        timer = undefined;
      }
      startClock();
      showTime();
""",
        buttons='<p><button type="button" onclick="startClock()">Start Clock</button> <button type="button" onclick="stopClock()">Stop Clock</button></p>',
        wait_ms=2500,
    ),
    S(
        "passing-extra-args",
        'Passing extra args: setTimeout(showMessage, 2000, "Hello", "John")',
        [
            "Extra arguments after the delay are passed **into the callback**.",
            '`setTimeout(showMessage, 2000, "Hello", "John")` → greeting and name.',
        ],
        'setTimeout(showMessage, 2000, "Hello", "John");\nfunction showMessage(greeting, name) {\n  document.getElementById("demo").innerHTML = greeting + " " + name;\n}',
        outcome='#demo shows **Hello John**.',
        script="""      function showMessage(greeting, name) {
        document.getElementById("demo").innerText = greeting + " " + name;
      }
      setTimeout(showMessage, 2000, "Hello", "John");
""",
        wait_ms=3500,
    ),
    S(
        "repeated-settimeout",
        "Repeated setTimeout (two ticks then stop)",
        [
            "Call `setTimeout` again from the callback to **repeat after the work finishes**.",
            "This demo runs **2 ticks** then stops so the screenshot does not loop forever.",
        ],
        'function repeat() {\n  myDisplayer("Hello");\n  setTimeout(repeat, 1000);\n}\nrepeat();',
        outcome="#demo shows **Hello (tick 2)** after two runs, then stops.",
        script=_myd("""      let n = 0;
      function repeat() {
        n++;
        myDisplayer("Hello (tick " + n + ")");
        if (n < 2) setTimeout(repeat, 1000);
      }
      repeat();
"""),
        wait_ms=3500,
    ),
    S(
        "countdown",
        "Countdown (auto start)",
        [
            "A countdown uses `setInterval`, then `clearInterval` at **0**.",
            "Auto-started so the snap shows a **decreased** count.",
        ],
        'let timer;\nfunction startCountdown() {\n  clearInterval(timer);\n  let count = 10;\n  myDisplayer(count);\n  timer = setInterval(function() {\n    count--;\n    myDisplayer(count);\n    if (count === 0) {\n      clearInterval(timer);\n      myDisplayer("Finished!");\n    }\n  }, 1000);\n}',
        outcome="Count has decreased from 10 (about 6 after ~4 s of virtual time).",
        script=_myd("""      let timer;
      function startCountdown() {
        clearInterval(timer);
        let count = 10;
        myDisplayer(String(count));
        timer = setInterval(function() {
          count--;
          myDisplayer(String(count));
          if (count === 0) {
            clearInterval(timer);
            myDisplayer("Finished!");
          }
        }, 1000);
      }
      startCountdown();
"""),
        buttons='<p><button type="button" onclick="startCountdown()">Start Countdown</button></p>',
        wait_ms=4000,
    ),
    S(
        "avoid-strings",
        "Avoid strings as timer code",
        [
            "**Not recommended:** `setTimeout(\"myFunction()\", 1000)` — the engine `eval`s a string.",
            "**Recommended:** `setTimeout(myFunction, 1000)` — pass the function. Safer, clearer, easier to debug (and CSP-friendly).",
            "Both forms can run the function; the string form is still a bad habit.",
        ],
        'setTimeout("myFunction()", 1000);  // not recommended\nsetTimeout(myFunction, 1000);     // recommended',
        outcome="Both callbacks run `myFunction`. Prefer the function reference.",
        script=_myd("""      let log = [];
      function myFunction(tag) {
        log.push("myFunction ran" + (tag ? " (" + tag + ")" : ""));
        myDisplayer(log.join("\\n"));
      }
      setTimeout("myFunction('string')", 200);
      setTimeout(function() { myFunction("function"); }, 400);
"""),
        wait_ms=2000,
    ),
    S(
        "long-callback-blocks",
        "Long callback still blocks the page",
        [
            "The delay only postpones **when** the callback starts.",
            "Once it starts, a long loop still **freezes** the page. Demo uses **`4e7`**, not the page's `4e9`.",
        ],
        'setTimeout(function() {\n  let i = 4e7;  // page used 4e9\n  while (--i > 0);\n  document.getElementById("demo").innerHTML = "Finished";\n}, 1000);',
        outcome='#demo shows **Finished** after the delayed (smaller) loop.',
        script="""      setTimeout(function() {
        let i = 4e7;
        while (--i > 0);
        document.getElementById("demo").innerText = "Finished (loop 4e7; page used 4e9)";
      }, 1000);
""",
        wait_ms=6000,
    ),
    S(
        "mistake-call-with-parens",
        "Common mistake: calling with ()",
        [
            "`setTimeout(myFunction(), 1000)` invokes the function **now**.",
            "Remove the parentheses: `setTimeout(myFunction, 1000)`.",
        ],
        "setTimeout(myFunction(), 1000);  // wrong\nsetTimeout(myFunction, 1000);    // right",
        outcome="Wrong form: **ran immediately**. Right form waits.",
        script=_myd("""      let log = [];
      function myFunction(tag) {
        log.push(tag);
        myDisplayer(log.join("\\n"));
      }
      log.push("wrong: setTimeout(myFunction(), 1000)");
      setTimeout(myFunction("immediate"), 1000);
      log.push("right form scheduled: setTimeout(myFunction, 1000)");
      setTimeout(function() { myFunction("later"); }, 300);
"""),
        wait_ms=2000,
    ),
    S(
        "slideshow-text",
        "Slideshow with text labels (nature / snow / mountains)",
        [
            "W3Schools cycles images every 3 s. This demo cycles **text labels** — no external images.",
            "Auto-started. `%` wraps the index after the last slide. `if (!timer)` prevents duplicate intervals.",
        ],
        'const images = ["nature", "snow", "mountains"];\nlet index = 0;\nlet timer;\nfunction showNextSlide() {\n  index = (index + 1) % images.length;\n  document.getElementById("slide").textContent = images[index];\n}\nfunction startSlides() {\n  if (!timer) {\n    timer = setInterval(showNextSlide, 1000);\n  }\n}',
        outcome="The label cycles **nature → snow → mountains**. Interval here is **1000** ms so the snap shows a change (the page used **3000** ms).",
        body='<p id="slide" style="font-size:28px;font-weight:bold;padding:12px 18px;border:3px solid #04aa6d;display:inline-block;">nature</p>',
        buttons='<p><button type="button" onclick="startSlides()">Start</button> <button type="button" onclick="stopSlides()">Stop</button></p>',
        script="""      const images = ["nature", "snow", "mountains"];
      let index = 0;
      let timer;
      function showNextSlide() {
        index = (index + 1) % images.length;
        document.getElementById("slide").textContent = images[index];
        document.getElementById("demo").innerText = "slide " + images[index];
      }
      function startSlides() {
        if (!timer) {
          timer = setInterval(showNextSlide, 1000);
        }
      }
      function stopSlides() {
        clearInterval(timer);
        timer = undefined;
      }
      startSlides();
""",
        wait_ms=4000,
    ),
]


def run_all() -> None:
    sections: list[tuple] = [
        (
            "js-functions",
            "JS Functions",
            FUNCTIONS,
            "This study-path page is the map for JavaScript functions: what they are, how you call them, how parameters and return values work, then expressions, arrows, and a quiz. Each beginner step below is a small runnable demo of that idea. Advanced topics (callbacks, this, call/apply/bind, IIFE, closures) belong on later pages and are only named in the concepts list.",
            [
                "A function is a **reusable code block**. It runs when it is **called** with `()`.",
                "**Parameters** are names in the definition; **arguments** are values in the call; **return** sends a value back.",
                "A **function expression** stores a function in a variable; an **arrow** is a short expression syntax.",
                "The **Advanced Functions** path (definitions, callbacks, `this`, `call`/`apply`/`bind`, IIFE, closures) is a later track — do not duplicate those chapters here.",
            ],
            [
                ("What is a function?", ["A **reusable block** of code for a particular task.", "It runs when it is **called** (invoked)."]),
                ("How do you call `sayHello`?", ["Write **`sayHello()`** — the parentheses mean execute now."]),
                ("What does `function multiply(a, b)` use `a` and `b` for?", ["They are **parameters** — names that receive incoming values."]),
                ("What does `return` do?", ["It sends a value **back** to the caller and **stops** the function."]),
                ("What is the difference between parameters and arguments?", ["**Parameters** are names (`a`, `b`).", "**Arguments** are values (`4`, `5`)."]),
                ("What is `const multiply = function(a, b) { return a * b; }`?", ["A **function expression** stored in `multiply`.", "Call it with `multiply(4, 3)`."]),
                ("What is `(a, b) => a * b`?", ["An **arrow function** — short syntax for a function expression.", "`multiply(4, 5)` is **20**."]),
                ("What is `let text = sayHello()` if `sayHello` returns `\"Hello World\"`?", ["**\"Hello World\"** — the quiz answer is **B**."]),
                ("Does defining a function run its body?", ["**No.** Definition only creates the function. A call runs it."]),
                ("Why is there an Advanced Functions path?", ["For later topics: callbacks, `this`, `call`/`apply`/`bind`, IIFE, closures.", "This page only introduces the beginner/intermediate steps."]),
            ],
            "Functions are reusable blocks you call with parentheses. Parameters receive arguments, return sends a value back, expressions store functions in variables, and arrows shorten that syntax. The quiz reuses these same examples. Advanced function features are a separate path.",
            [
                ("JS Functions (W3Schools)", "https://www.w3schools.com/js/js_functions.asp"),
                ("MDN: Functions guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),
                ("MDN: Functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions"),
            ],
            4000,
        ),
        (
            "js-function-intro",
            "JS Function Intro",
            INTRO,
            "Functions are reusable code blocks. This page shows the shape of a function, why you call it, how to pass parameters, how local variables stay inside the function, and how a call can be used as a value in a larger expression.",
            [
                "Write `function name(params) { ... }` — name, parentheses, then a **block**.",
                "Nothing runs until you **call** `name()`. Returned values can be stored or used inline.",
                "**Local** variables exist only inside the function; they throw **ReferenceError** outside.",
                "Call the same function **many times** with different inputs for different results.",
            ],
            [
                ("Does `function sayHello() { return \"Hello World\"; }` print anything by itself?", ["**No.** `typeof sayHello` is **function**, but the body has not run."]),
                ("What is `let message = sayHello()`?", ["**\"Hello World\"** stored in `message`.", "`()` means execute now."]),
                ("What is `multiply(4, 5)` if the function returns `a * b`?", ["**20**."]),
                ("What are `sum1` and `sum2` after `add(5, 5)` and `add(50, 50)`?", ["**10** and **100**.", "The same function ran twice."]),
                ("Can code outside `myFunction` read `let carName` declared inside it?", ["**No.** That is a **ReferenceError**.", "Local variables are created when the function starts and deleted when it finishes."]),
                ("What is `toCelsius(77)`?", ["**25**.", "You can store it in `x` or drop the call into a string."]),
                ("Should a function declaration end with a semicolon?", ["Usually **no**. Semicolons separate executable statements, not declarations."]),
                ("Why use functions?", ["**Reuse** code, **organize** it, and make it easier to **read** and maintain."]),
                ("What is the usual input/output pattern?", ["Parameters in, work in the body, **return** a value out."]),
                ("What string does inline `toCelsius(77)` build?", ["**\"The temperature is 25 Celsius\"**."]),
            ],
            "Define a function, then call it. Parameters take input, return gives output, local variables stay inside, and you can reuse the same function with different arguments — even inline inside a string.",
            [
                ("JS Functions intro (W3Schools)", "https://www.w3schools.com/js/js_function_intro.asp"),
                ("MDN: Functions guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),
                ("MDN: return", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return"),
            ],
            4000,
        ),
        (
            "js-function-invocation",
            "JS Function Invocation",
            INVOCATION,
            "A function runs when something invokes it: a call in your code, an event such as a button click, or a self-invoked function. Parentheses invoke. Without them you get the function object itself, not the result. You must store, log, or display a return value if you want to see it.",
            [
                "**Invoke** means run the function — by a call, an event, or automatically.",
                "`name()` is the **result**. `name` (no `()`) is the **function object**.",
                "A return value is unused unless you **store** or **display** it.",
                "Functions can call other functions, and buttons can call functions.",
            ],
            [
                ("Does defining `sayHello` run it?", ["**No.** The body waits for an invocation."]),
                ("What happens if you write `sayHello();` and ignore the result?", ["The function **runs**, but the return value is **discarded**."]),
                ("How do you keep the greeting?", ["`let greeting = sayHello();` — greeting is **\"Hello World\"**."]),
                ("What does `console.log(sayHello())` print?", ["**Hello World** (in the console).", "This sandbox also shows it in #demo."]),
                ("What does `innerHTML = sayHello()` show?", ["**Hello World** in the element."]),
                ("What are `a`, `b`, and `c` after three `sayHello()` calls?", ["Each is **\"Hello World\"**."]),
                ("What is `toCelsius(77)`?", ["**25** — the function **result**."]),
                ("What is `let value = toCelsius` (no parentheses)?", ['`typeof value` is **"function"** — the function object, not 25.']),
                ("What is `let text = sayHello`?", ["`text` is a **reference** to the function.", "`text()` then returns **Hello World**."]),
                ("How can `showHello` display a greeting?", ["It calls `sayHello()` and writes the string into **#demo**."]),
                ("What is a common event that invokes a function?", ["A **button click** (`onclick`)."]),
                ("What if the function has no `return`?", ["The call evaluates to **undefined**."]),
                ("Why might the page look empty after a call?", ["You returned a value but **never displayed** it."]),
            ],
            "Parentheses invoke a function. Skip them and you get the function itself. Store or display the return value, call from other functions or events, and remember that no return means undefined.",
            [
                ("JS Function Invocation (W3Schools)", "https://www.w3schools.com/js/js_function_invocation.asp"),
                ("MDN: Functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions"),
                ("MDN: Function.prototype.call", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call"),
            ],
            4000,
        ),
        (
            "js-function-parameters",
            "JS Function Parameters",
            PARAMS,
            "Parameters are the names in a function definition. They receive the arguments you pass when you call the function. JavaScript does not type-check, does not require a matching argument count, and since ES2015 you can give a parameter a default.",
            [
                "Parameters are listed in `function name(p1, p2)` — **comma-separated**.",
                "JS does **not** specify types, type-check, or count arguments.",
                "A missing argument is **undefined** (often producing **NaN** in math).",
                "**Default parameters** (`y = 10`) fill in omitted or undefined arguments.",
            ],
            [
                ("What is `multiply(4, 5)`?", ["**20**. Parameters `a` and `b` received 4 and 5."]),
                ("What is `sayHello(\"John\")`?", ["**\"Hello John\"**."]),
                ("What is `toCelsius(77)`?", ["**25**."]),
                ("What is `fullName(\"John\", \"Doe\")`?", ["**\"John Doe\"**."]),
                ("What is `toCelsius()` with no argument?", ["**NaN** — `fahrenheit` is undefined."]),
                ("What is `myFunction(5)` if `y = 10`?", ["**15**.", "`myFunction(5, 3)` is **8**."]),
                ("Does JavaScript check argument types?", ["**No.**"]),
                ("Does JavaScript check how many arguments you passed?", ["**No.** Extra args are ignored unless you read `arguments` or rest. Missing ones are **undefined**."]),
                ("When is a default parameter used?", ["When the argument is **omitted** or **undefined**."]),
                ("What is the difference between a parameter and an argument?", ["Parameter = **name** in the definition.", "Argument = **value** in the call."]),
            ],
            "List parameters in the definition and pass arguments in the call. JavaScript will not type-check or count them for you. Missing values are undefined (NaN in math) unless you set a default.",
            [
                ("JS Function Parameters (W3Schools)", "https://www.w3schools.com/js/js_function_parameters.asp"),
                ("MDN: Default parameters", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters"),
                ("MDN: Functions guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),
            ],
            4000,
        ),
        (
            "js-function-return",
            "JS Function Returns",
            RETURNS,
            "return sends a value out of a function and stops the function immediately. You can return any type, use the call inside a larger expression, leave early on a condition, or update HTML with the result. A function with no return yields undefined. console.log is not the same as return.",
            [
                "`return value;` sends **value** to the caller and **exits** the function.",
                "Code **after** `return` never runs.",
                "No `return` means the result is **undefined**.",
                "`console.log` displays; it does **not** return a value to assign.",
            ],
            [
                ("What is `let message = sayHello()`?", ["**\"Hello World\"**."]),
                ("What is `multiply(4, 5)`?", ["**20**."]),
                ("What is `multiply(2, 3) * 10`?", ["**60** — 6 times 10."]),
                ("What is `fullName(\"John\", \"Doe\")`?", ["**\"John Doe\"**."]),
                ("What if the first line is `return \"Done\"` before `return a * b`?", ["The result is **\"Done\"**. The multiply never runs."]),
                ("What is the result if you compute `a * b` but never return it?", ["**undefined**."]),
                ("What does `checkAge(15)` vs `checkAge(21)` return?", ["**\"Too young\"** vs **\"Access granted\"**."]),
                ("What does `innerHTML = toCelsius(77)` show?", ["**25**."]),
                ("Is `console.log(\"Hello\")` a return value?", ["**No.** Logging is a side effect.", "A function that only logs returns **undefined**."]),
                ("Can a function return a string, not just a number?", ["**Yes.** `return` works with any type."]),
                ("Does `return` stop the rest of the function?", ["**Yes.** That is why early returns work."]),
            ],
            "Use return to send a value back and to stop the function. Expressions can use that value immediately. Skip return and you get undefined. Logging to the console is not returning.",
            [
                ("JS Function Return (W3Schools)", "https://www.w3schools.com/js/js_function_return.asp"),
                ("MDN: return", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return"),
                ("MDN: Functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions"),
            ],
            4000,
        ),
        (
            "js-function-arguments",
            "JS Function Arguments",
            ARGS,
            "Arguments are the real values passed into a call. They map to parameters by position. Extra values are available on the arguments object or with rest parameters. Missing values are undefined unless you default them. Primitives are copied; object properties can change outside the function.",
            [
                "**Parameters** = names. **Arguments** = values, assigned **in order**.",
                "The **`arguments`** object is array-like (not in arrows). **Rest** `...args` is a real array.",
                "No type or count checking. Missing args are **undefined** (often **NaN**).",
                "Primitives are **pass-by-value**. Object **properties** change in place.",
            ],
            [
                ("In `multiply(4, 5)`, what are parameters vs arguments?", ["Parameters: **a, b**.", "Arguments: **4, 5**."]),
                ("What is `findMax(1, 123, 500, 115, 44, 88)`?", ["**500** — uses the `arguments` object."]),
                ("What is `sumAll(1, 123, 500, 115, 44, 88)`?", ["**871**."]),
                ("What is `subtract(10, 5)` vs `subtract(5, 10)`?", ["**5** vs **-5**. Order matters."]),
                ("Can arguments be variables?", ["**Yes.** `multiply(x, y)` passes the **values** of x and y."]),
                ("What is `toCelsius(\"John\")`?", ["**NaN** — no type check."]),
                ("What is `multiply(4)` with two parameters?", ["**NaN** — `b` is undefined."]),
                ("How did people default `y` before ES2015?", ["`if (y === undefined) { y = 2; }` inside the function."]),
                ("What is `myFunction(5)` with `y = 10`?", ["**15**."]),
                ("What is `sum(4, 9, 16, 25, 29, 100, 66, 77)` with rest?", ["**326**."]),
                ("If `addOne` does `n = n + 1` on a number `x = 10`, is `x` changed?", ["**No.** `x` stays **10**. The function got a copy."]),
                ("If a function sets `obj.name = \"Jane\"`, does the original object change?", ["**Yes.** Object properties are visible outside."]),
            ],
            "Arguments fill parameters by position. Use arguments or rest for a variable number of values, defaults for missing ones, and remember that numbers are copied while object properties are not.",
            [
                ("JS Function Arguments (W3Schools)", "https://www.w3schools.com/js/js_function_arguments.asp"),
                ("MDN: arguments", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments"),
                ("MDN: Rest parameters", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters"),
                ("MDN: Default parameters", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters"),
            ],
            4000,
        ),
        (
            "js-function-expressions",
            "JS Function Expressions",
            EXPRS,
            "A function expression stores a function in a variable. The variable is how you call it. Expressions are usually anonymous (or optionally named) and end with a semicolon. They are not hoisted like declarations, which makes them useful as callbacks you pass around as values.",
            [
                "A function expression is a **function stored in a variable**.",
                "It is often **anonymous**; a **named** expression is allowed but you still call the variable.",
                "Treat it as a **statement** — end with **`;`**.",
                "**Declarations** are hoisted; **expressions** are not (TDZ / ReferenceError if called too early).",
            ],
            [
                ("What is `const multiply = function(a, b) { return a * b; }`?", ["A **function expression**.", "`multiply(4, 3)` is **12**."]),
                ("How do you call that function?", ["Use the **variable**: `multiply(4, 3)`."]),
                ("Should the expression end with a semicolon?", ["**Yes.** It is a statement."]),
                ("What is `run(sayHello)` if `run` does `return fn()`?", ["It **calls** the function you passed. Result **\"Hello\"**."]),
                ("What is `sayHello()` for `const sayHello = function() { return \"Hello World\"; }`?", ["**\"Hello World\"**."]),
                ("Can you call a declaration before its line?", ["**Yes.** `let sum = add(2, 3)` then `function add` yields **5**."]),
                ("Can you call a `const` expression before its line?", ["**No.** **ReferenceError** (temporal dead zone)."]),
                ("What is an anonymous function?", ["A function **without a name** after `function`. The variable is the name you use."]),
                ("When are expressions a good choice?", ["Callbacks, event handlers, and any time the function is a **value**."]),
                ("What is `sayHello` vs `sayHello()`?", ["`sayHello` is the **function**. `sayHello()` is the **result**."]),
            ],
            "Store a function in a variable, end the statement with a semicolon, and call the variable. Declarations hoist; expressions do not. Pass expressions as callbacks because they are values.",
            [
                ("JS Function Expressions (W3Schools)", "https://www.w3schools.com/js/js_function_expressions.asp"),
                ("MDN: Functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions"),
                ("MDN: Hoisting", "https://developer.mozilla.org/en-US/docs/Glossary/Hoisting"),
            ],
            4000,
        ),
        (
            "js-function-arrow",
            "JS Function Arrow",
            ARROW,
            "Arrow functions are a short syntax for function expressions. You can omit function, return, and braces for a single expression, and omit parentheses around a single parameter. They are not hoisted, they do not have their own this, and braces without return yield undefined. Duplicate Tryits on the W3Schools page are shown once.",
            [
                "`(a, b) => a * b` skips `function`, `return`, and `{}` for one expression.",
                "Parentheses: required for **zero or 2+** parameters; optional for **one**.",
                "A `{ }` body needs an explicit **`return`**. `=> return` is a **SyntaxError**.",
                "Arrows are **not hoisted** and do **not** bind their own **`this`** — skip them as object methods.",
            ],
            [
                ("What is `(a, b) => a * b` for 4 and 5?", ["**20**."]),
                ("What is the longer equivalent?", ["`const multiply = function(a, b) { return a * b; }`."]),
                ("What is `const hello = () => \"Hello World!\"`?", ["**\"Hello World!\"** when called.", "Empty `()` is required with no parameters."]),
                ("Are `(x) => x * x` and `x => x * x` the same?", ["**Yes** for one parameter. `square(5)` is **25**."]),
                ("What is `(val) => \"Hello \" + val` with `\"World\"`?", ["**\"Hello World\"**."]),
                ("What does `{ x * y }` return?", ["**undefined** — a block with no `return`."]),
                ("What does `=> return x * y` do?", ["**SyntaxError** — `return` is not an expression."]),
                ("What does `{ return x * y }` return for 4 and 5?", ["**20**."]),
                ("Can you call an arrow before its `const` line?", ["**No.** **ReferenceError**."]),
                ("What is `this.name` in `greet: function() { return this.name; }` on `{name: \"John\"}`?", ["**\"John\"**."]),
                ("What is `this.name` if `greet` is an arrow on that object?", ["**Not** `\"John\"`. The arrow uses surrounding `this` (often the global object)."]),
                ("When should you not use arrows?", ["As **object methods**, when you need your own `this`, or when you want a hoisted declaration."]),
            ],
            "Arrows shorten function expressions. Keep parentheses for 0 or 2+ parameters, use return inside braces, define them before you call them, and do not use them as methods that need this.",
            [
                ("JS Arrow Function (W3Schools)", "https://www.w3schools.com/js/js_arrow_function.asp"),
                ("MDN: Arrow functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"),
                ("MDN: this", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this"),
            ],
            4000,
        ),
        (
            "js-function-quiz",
            "JS Function Quiz",
            QUIZ,
            "Nine quiz questions from the functions track, each run as a live example. The sandbox prints the computed result and the correct letter so you can check yourself against the same snippets the tutorial used.",
            [
                "`()` **calls** a function; without `()` you have a **reference**.",
                "**Parameters** are names; no `return` means **undefined**.",
                "Only **declarations** hoist. Correct arrow: `(a, b) => a + b`.",
                "In a method, `this` is the **owner object**. Arrows do **not** have their own `this`.",
            ],
            [
                ("Q1: `let text = sayHello()` — what is text?", ["**B. Hello World**.", "The function returns that string."]),
                ("Q2: Which line calls `test`?", ["**C. `let y = test()`**.", "`let x = test` only copies the function."]),
                ("Q3: In `function multiply(a, b)`, what are a and b?", ["**B. Parameters**."]),
                ("Q4: `x = add(2, 3) * 10` — what is x?", ["**C. 50**.", "add returns 5, then 5 × 10."]),
                ("Q5: No return statement — what is returned?", ["**C. undefined**."]),
                ("Q6: Which kind can be called before it is defined?", ["**A. Function declaration**.", "Expressions and arrows are not hoisted that way."]),
                ("Q7: Which arrow is correct?", ["**C. `const add = (a, b) => a + b`**.", "A is a SyntaxError; B is missing parentheses around two params."]),
                ("Q8: What does `this` refer to in `person.getName`?", ["**C. The object that owns the method**.", "`getName()` returns **John**."]),
                ("Q9: Why does `greet: () => this.name` fail?", ["**B. Arrow functions do not have their own this**.", "They inherit `this` from the surrounding scope."]),
                ("What is `typeof` of `let x = test`?", ["**\"function\"**."]),
            ],
            "The quiz answers are B, C, B, C, C, A, C, C, B. Calling needs parentheses, parameters are names, missing return is undefined, declarations hoist, the short arrow is `(a, b) => a + b`, and this in a method is the owner — arrows do not get their own this.",
            [
                ("JS Function Quiz (W3Schools)", "https://www.w3schools.com/js/js_function_quiz.asp"),
                ("MDN: Functions guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),
                ("MDN: Arrow functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"),
            ],
            4000,
        ),
        (
            "js-timers",
            "JS Timers",
            TIMERS,
            "Timers schedule a function for later: setTimeout once, setInterval repeatedly, and clearTimeout / clearInterval to cancel. They do not pause JavaScript. The delay is a minimum, callbacks still run on the main thread, and you must pass the function name — not a call with parentheses. Extra arguments after the delay go to the callback. This section avoids infinite loops and oversized busy-waits so screenshots can finish.",
            [
                "`setTimeout(fn, ms)` once; `setInterval(fn, ms)` repeat; `clear*` cancel using the returned **id**.",
                "Timers **do not pause** the rest of the script. Order is **Start End Timer**, even with delay 0.",
                "Pass **`fn`**, not **`fn()`**. Do not pass a **string** of code.",
                "The delay is a **minimum**. A busy loop or a long callback still **blocks** the page.",
            ],
            [
                ("What does `setTimeout(myFunction, 3000)` show after 3 s?", ["**Hello!**"]),
                ("Why is `setTimeout(myFunction(), 3000)` wrong?", ["It **calls immediately**. `undefined` is scheduled as the callback."]),
                ("What is the order of Start, setTimeout 3000, End?", ["**Start End Timer** — timeout does not pause the script."]),
                ("What if the delay is 0?", ["Still **Start End Timer**. Zero means “as soon as this task finishes”, not “now”."]),
                ("Is the delay exact?", ["It is a **minimum**. A busy loop can make the callback late.", "This demo used **4e7**, not the page’s **4e9**."]),
                ("How do you cancel a timeout?", ["Save the id, then **`clearTimeout(id)`**. This snap shows **Timer stopped**."]),
                ("What does `setInterval(showTime, 1000)` do?", ["Updates a clock about **every second** until cleared."]),
                ("How do you stop an interval?", ["**`clearInterval(id)`**. Guard `if (!timer)` so you do not start two of them."]),
                ("What does `setTimeout(showMessage, 2000, \"Hello\", \"John\")` show?", ["**Hello John** — extra args are passed to the callback."]),
                ("Repeated `setTimeout` vs `setInterval`?", ["Repeated timeout waits until the **callback finishes** before scheduling the next delay.", "Interval keeps a fixed schedule."]),
                ("Why avoid `setTimeout(\"myFunction()\", 1000)`?", ["It **eval**s a string: harder to debug, worse for CSP, no closure of locals.", "Pass the **function** instead."]),
                ("Does a timer run the callback off the main thread?", ["**No.** Waiting is outside JS; the callback still **blocks** the page when it runs."]),
                ("What wraps a slideshow index?", ["**`index = (index + 1) % images.length`**.", "This demo cycles **nature / snow / mountains** as text, not remote images."]),
                ("What are the four timer functions?", ["**setTimeout**, **setInterval**, **clearTimeout**, **clearInterval**."]),
            ],
            "Schedule work with setTimeout and setInterval, cancel with the matching clear function, pass the function rather than calling it, and treat delays as minimums. Extra arguments after the delay go to the callback. Keep callbacks short so the page stays responsive.",
            [
                ("JS Timers (W3Schools)", "https://www.w3schools.com/js/js_timers.asp"),
                ("MDN: setTimeout", "https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout"),
                ("MDN: setInterval", "https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval"),
                ("MDN: clearTimeout", "https://developer.mozilla.org/en-US/docs/Web/API/Window/clearTimeout"),
                ("MDN: clearInterval", "https://developer.mozilla.org/en-US/docs/Web/API/Window/clearInterval"),
            ],
            8000,
        ),
    ]
    for slug, title, recs, intro, concepts, qa, summary, refs, wait in sections:
        print("building", slug, "examples", len(recs), "wait", wait)
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs, wait=wait)
        print("done", slug)


if __name__ == "__main__":
    run_all()

