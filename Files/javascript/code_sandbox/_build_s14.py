"""S14 JS Iterations + S15 JS Math (W3Schools tutorial pages)."""
from __future__ import annotations

from _gen_lib import S, build_and_snap

# ---------------------------------------------------------------------------
# 14.1 JS Iterations (js_looping.asp)
# ---------------------------------------------------------------------------

ITERATIONS = [
    S(
        "for-loop",
        "for (let i = 0; i < 5; i++)",
        [
            "`for` has **init**, **condition**, and **increment**: `for (exp1; exp2; exp3)`.",
            "Use it when the number of trips is **known** (here: `i` from **0** to **4**).",
        ],
        'let text = "";\nfor (let i = 0; i < 5; i++) {\n  text += "The number is " + i + "\\n";\n}',
        [("text", "text")],
        "text is five lines: **The number is 0** through **The number is 4**.",
    ),
    S(
        "while-loop",
        "while (i < 10)",
        [
            "`while` repeats **as long as** the condition is true.",
            "**Increment inside** the body. Forgetting that makes an **infinite loop**.",
        ],
        'let text = "";\nlet i = 0;\nwhile (i < 10) {\n  text += "The number is " + i + "\\n";\n  i++;\n}',
        [("text", "text"), ("i after loop", "i")],
        "Lines **The number is 0** through **The number is 9**. After the loop, `i` is **10**.",
    ),
    S(
        "do-while-loop",
        "do...while (i < 10)",
        [
            "`do...while` runs the body **once before** testing the condition.",
            "Even a false condition still produces **one** trip. Still increment, or it never ends.",
        ],
        'let text = "";\nlet i = 0;\ndo {\n  text += "The number is " + i + "\\n";\n  i++;\n} while (i < 10);',
        [("text", "text"), ("i after loop", "i")],
        "Same ten lines **0** through **9**. `i` is **10**. The body ran **before** the first test.",
    ),
    S(
        "for-in-person",
        "for...in over a person object",
        [
            "`for...in` walks **enumerable keys** of an object (typically **plain objects**).",
            "`x` is the **key**. `person[x]` is the **value**.",
        ],
        'const person = {fname:"John", lname:"Doe", age:25};\nlet txt = "";\nfor (let x in person) {\n  txt += person[x] + " ";\n}',
        [("txt", "txt")],
        'txt is **"John Doe 25 "** (keys `fname`, `lname`, `age` in that order here).',
    ),
    S(
        "for-of-array",
        "for...of over an array (table row; no Tryit)",
        [
            "`for...of` walks **values** of an **iterable** (arrays, strings, Maps, Sets).",
            "No Tryit on this page — the next chapter is **JS Iterables**. Still run one array loop.",
        ],
        'const cars = ["BMW", "Volvo", "Saab", "Ford"];\nlet text = "";\nfor (const car of cars) {\n  text += car + "\\n";\n}',
        [("text", "text")],
        "text is **BMW**, **Volvo**, **Saab**, **Ford** (one per line) — the **values**, not indexes.",
    ),
    S(
        "foreach-array",
        "array.forEach() (table row; no Tryit)",
        [
            "`forEach()` is an **Array** method: one callback per element.",
            "Listed under **Other Methods** with `map` / `filter` / `reduce`. No Tryit on this page.",
        ],
        'const numbers = [45, 4, 9, 16, 25];\nlet text = "";\nnumbers.forEach(function (value) {\n  text += value + "\\n";\n});',
        [("text", "text")],
        "text is **45**, **4**, **9**, **16**, **25** (one per line).",
    ),
]


# ---------------------------------------------------------------------------
# 14.2 JS Iterables
# ---------------------------------------------------------------------------

ITERABLES = [
    S(
        "for-of-string",
        'for...of over "W3Schools"',
        [
            "A **string** is iterable. `for...of` yields each **code unit** (here: each character).",
            "`const x of name` — `x` is the **character**, not an index.",
        ],
        'const name = "W3Schools";\nlet text = "";\nfor (const x of name) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Nine lines: **W**, **3**, **S**, **c**, **h**, **o**, **o**, **l**, **s**.",
    ),
    S(
        "for-of-letters",
        'for...of over ["a","b","c"]',
        [
            "An **Array** is iterable. `for...of` yields each **element**.",
        ],
        'const letters = ["a","b","c"];\nlet text = "";\nfor (const x of letters) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **a**, **b**, **c**.",
    ),
    S(
        "for-of-numbers",
        "for...of over [2, 4, 6, 8]",
        [
            "Same loop over a **numbers** array.",
        ],
        "const numbers = [2,4,6,8];\nlet text = \"\";\nfor (const x of numbers) {\n  text += x + \"\\n\";\n}",
        [("text", "text")],
        "Lines **2**, **4**, **6**, **8**.",
    ),
    S(
        "for-of-set",
        'for...of over Set(["a","b","c"])',
        [
            "A **Set** is iterable. Values appear **once**, in insertion order.",
        ],
        'const letters = new Set(["a","b","c"]);\nlet text = "";\nfor (const x of letters) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **a**, **b**, **c**.",
    ),
    S(
        "for-of-map",
        "for...of over a Map of fruits",
        [
            "A **Map** is iterable. Each step yields a **`[key, value]` pair** (an Array).",
            "`String([\"apples\", 500])` is **`apples,500`** (Array `toString`).",
        ],
        'const fruits = new Map([\n  ["apples", 500],\n  ["bananas", 300],\n  ["oranges", 200]\n]);\nlet text = "";\nfor (const x of fruits) {\n  text += x + "\\n";\n}',
        [("text", "text"), ("first pair JSON", "JSON.stringify([...fruits][0])")],
        "text is **apples,500**, **bananas,300**, **oranges,200**. The first pair JSON is "
        '**["apples",500]**.',
    ),
    S(
        "homemade-next",
        "Home-made iterator: next() never done",
        [
            "An object is an **iterator** when it has **`next()`** returning `{value, done}`.",
            "This factory returns `{value: n, done: false}` forever (**10, 20, 30, …**).",
            "It is **not** iterable: there is no `Symbol.iterator`, so **`for...of` will not work**.",
        ],
        """function myNumbers() {
  let n = 0;
  return {
    next: function() {
      n += 10;
      return {value:n, done:false};
    }
  };
}
const n = myNumbers();
const a = n.next();
const b = n.next();
const c = n.next();
const d = n.next();""",
        [
            ("a", "JSON.stringify(a)"),
            ("b", "JSON.stringify(b)"),
            ("c", "JSON.stringify(c)"),
            ("d.value (Tryit display)", "d.value"),
        ],
        "a/b/c are **{\"value\":10,\"done\":false}**, **20**, **30**. The Tryit then prints "
        "`n.next().value` → **40**. `done` stays **false**.",
    ),
    S(
        "symbol-iterator-for-of",
        "Symbol.iterator homemade iterable + for...of",
        [
            "A true **iterable** has **`obj[Symbol.iterator]`** — a function that returns an iterator.",
            "`for...of` calls that method automatically.",
            "This demo sets `done: true` when `n == 100`. **`for...of` does not yield the done value.**",
        ],
        """const myNumbers = {};
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  let done = false;
  return {
    next() {
      n += 10;
      if (n == 100) { done = true; }
      return {value:n, done:done};
    }
  };
};
let text = "";
for (const num of myNumbers) {
  text += num + "\\n";
}""",
        [("text", "text")],
        "Lines **10** through **90**. When `n` hits **100**, `done` is **true**, so **100 is omitted**. "
        "(The page assigns `done` as a sloppy global; this sandbox uses `let done`.)",
    ),
    S(
        "symbol-iterator-manual",
        "Manual iterator.next() until done",
        [
            "You can call **`obj[Symbol.iterator]()`** yourself and loop on **`next()`**.",
            "`if (result.done) break` skips the completion `{value, done:true}` — same as `for...of`.",
        ],
        """const myNumbers = {};
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  let done = false;
  return {
    next() {
      n += 10;
      if (n == 100) { done = true; }
      return {value:n, done:done};
    }
  };
};
let iterator = myNumbers[Symbol.iterator]();
let text = "";
while (true) {
  const result = iterator.next();
  if (result.done) break;
  text += result.value + "\\n";
}""",
        [("text", "text")],
        "Same as `for...of`: **10** through **90**. The `{value:100, done:true}` step is not printed.",
    ),
]


# ---------------------------------------------------------------------------
# 14.3 JS Iterators (ES2025 helpers)
# ---------------------------------------------------------------------------

ITERATORS = [
    S(
        "array-iterator-next",
        "Array iterator: Symbol.iterator + next()",
        [
            "Built-in iterables (arrays, strings, Maps, Sets) store **`Symbol.iterator`** on the prototype.",
            "`arr[Symbol.iterator]()` returns an iterator. **`next()`** is `{value, done}`.",
            "No Tryit for the protocol itself on this page — still run it.",
        ],
        'const arr = ["a", "b"];\nconst it = arr[Symbol.iterator]();\nconst first = it.next();\nconst second = it.next();\nconst third = it.next();',
        [
            ("first", "JSON.stringify(first)"),
            ("second", "JSON.stringify(second)"),
            ("third", "JSON.stringify(third)"),
        ],
        'first **{"value":"a","done":false}**, second **{"value":"b","done":false}**, '
        'third **{"done":true}** (`value` is **undefined**).',
    ),
    S(
        "iterator-from",
        "Iterator.from([1, 2, 3])",
        [
            "`Iterator.from(iterable)` wraps an iterable as an **Iterator** helper object.",
            "Then `for...of` (or helper methods) can consume it.",
        ],
        'const myIterator = Iterator.from([1, 2, 3]);\nlet text = "";\nfor (const x of myIterator) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **1**, **2**, **3**.",
    ),
    S(
        "iterator-drop",
        "drop(5) on [1, 2, 3, 4, 5, 6]",
        [
            "`drop(n)` returns an iterator that **skips** the first **n** values.",
            "The remaining values are still yielded one by one (not an Array until you collect them).",
        ],
        'const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);\nconst rest = myIterator.drop(5);\nlet text = "";\nfor (const x of rest) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Only **6** remains (the first five values were dropped).",
    ),
    S(
        "iterator-every",
        'every(x => x > 7) on "123456789"',
        [
            "`every(fn)` is **true** only if **every** element passes `fn`.",
            "String digits coerce: `\"1\" > 7` is **false** (numeric compare), so the answer is false.",
        ],
        'const myIterator = Iterator.from("123456789");\nlet result = myIterator.every(x => x > 7);',
        [("result", "result")],
        "**false** — `'1'` is not greater than 7. (`every` stops at the first failure.)",
    ),
    S(
        "iterator-filter",
        "filter(x => x > 18) on [32, 33, 16, 40]",
        [
            "`filter(fn)` yields only elements for which `fn` is **truthy**.",
        ],
        'const myIterator = Iterator.from([32, 33, 16, 40]);\nconst filteredIterator = myIterator.filter(x => x > 18);\nlet text = "";\nfor (const x of filteredIterator) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **32**, **33**, **40**. **16** is dropped.",
    ),
    S(
        "iterator-find",
        "find(x => x > 18) on [3, 10, 18, 30, 20]",
        [
            "`find(fn)` returns the **first** matching **value** (not an iterator).",
            "**18** is not `> 18`. The first hit is **30**.",
        ],
        "const myIterator = Iterator.from([3, 10, 18, 30, 20]);\nlet result = myIterator.find(x => x > 18);",
        [("result", "result")],
        "result is **30**.",
    ),
    S(
        "iterator-flatmap",
        "flatMap(x => [x, x * 10])",
        [
            "`flatMap(fn)` maps each element to an **iterable** and **flattens one level**.",
            "`[x, x * 10]` becomes two yielded numbers per input.",
        ],
        'const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);\nconst mappedIterator = myIterator.flatMap(x => [x, x * 10]);\nlet text = "";\nfor (const x of mappedIterator) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60**.",
    ),
    S(
        "iterator-foreach",
        'forEach on Iterator.from("123456789")',
        [
            "`forEach(fn)` runs `fn` once per remaining element (consumed; returns **undefined**).",
        ],
        'const myIterator = Iterator.from("123456789");\nlet text = "";\nmyIterator.forEach(x => text += x);',
        [("text", "text")],
        'text is **"123456789"** (the nine digit characters concatenated).',
    ),
    S(
        "iterator-map",
        'map(x => x * 2) on "123456789"',
        [
            "`map(fn)` yields `fn(element)` for each element.",
            "Digit characters coerce: `'1' * 2` is **2** (number).",
        ],
        'const myIterator = Iterator.from("123456789");\nconst mappedIterator = myIterator.map(x => x * 2);\nlet text = "";\nfor (const x of mappedIterator) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **2, 4, 6, 8, 10, 12, 14, 16, 18**.",
    ),
    S(
        "iterator-reduce",
        "reduce sum of [175, 50, 25]",
        [
            "`reduce(fn)` folds the iterator to **one value**.",
            "With no initial value, the first element is the start accumulator.",
        ],
        "function myFunc(total, num) {\n  return total + num;\n}\nconst myIterator = Iterator.from([175, 50, 25]);\nlet result = myIterator.reduce(myFunc);",
        [("result", "result")],
        "result is **250** (`175 + 50 + 25`).",
    ),
    S(
        "iterator-some",
        'some(x => x > 7) on "123456789"',
        [
            "`some(fn)` is **true** if **at least one** element passes `fn`.",
            "`'8' > 7` and `'9' > 7` are true after numeric coercion.",
        ],
        'const myIterator = Iterator.from("123456789");\nlet result = myIterator.some(x => x > 7);',
        [("result", "result")],
        "**true**.",
    ),
    S(
        "iterator-take",
        "take(5) on [1, 2, 3, 4, 5, 6]",
        [
            "`take(n)` yields **at most n** elements, then stops.",
        ],
        'const myIterator = Iterator.from([1, 2, 3, 4, 5, 6]);\nconst firstFive = myIterator.take(5);\nlet text = "";\nfor (const x of firstFive) {\n  text += x + "\\n";\n}',
        [("text", "text")],
        "Lines **1, 2, 3, 4, 5**. **6** is not taken.",
    ),
]


# ---------------------------------------------------------------------------
# 14.4 JS Generators
# ---------------------------------------------------------------------------

GENERATORS = [
    S(
        "yield-then-return",
        "function* with yield 1, yield 2, return 3",
        [
            "`function*` returns a **Generator** object (iterable **and** iterator).",
            "`yield` pauses and produces `{value, done:false}`. **`return`** finishes with `{done:true}`.",
            "`for...of` **stops at done:true** and does **not** include the return value.",
        ],
        """function* myStream() {
  yield 1;
  yield 2;
  return 3;
}
let myGenerator = myStream();
let text = "";
for (let value of myGenerator) {
  text += value + "\\n";
}""",
        [("text", "text")],
        "text is **1** then **2**. **3 is omitted** because `return 3` sets **done: true**.",
    ),
    S(
        "three-yields",
        "function* with three yield values",
        [
            "To have `for...of` print a value, **`yield` it** — do not `return` it as the last step.",
            "The page’s prose had a `yeald` typo; the Tryit correctly uses **`yield 3`**.",
        ],
        """function* myStream() {
  yield 1;
  yield 2;
  yield 3;
}
let myGenerator = myStream();
let text = "";
for (let value of myGenerator) {
  text += value + "\\n";
}""",
        [("text", "text")],
        "text is **1**, **2**, **3**.",
    ),
    S(
        "next-done-return-value",
        "next() objects: value and done (including return)",
        [
            "`generator.next()` resumes until the next `yield` or `return`.",
            "The object is always **`{value, done}`**. A `return` value is in **`value` with done:true**.",
            "Table row **next()** — no Tryit on the page. Still run it.",
        ],
        """function* myStream() {
  yield 1;
  yield 2;
  return 3;
}
let g = myStream();
const a = g.next();
const b = g.next();
const c = g.next();
const d = g.next();""",
        [
            ("a", "JSON.stringify(a)"),
            ("b", "JSON.stringify(b)"),
            ("c", "JSON.stringify(c)"),
            ("d", "JSON.stringify(d)"),
        ],
        'a **{"value":1,"done":false}**, b **{"value":2,"done":false}**, '
        'c **{"value":3,"done":true}** (the **return** value), '
        'd **{"done":true}** (`value` **undefined**).',
    ),
    S(
        "generator-return-method",
        "generator.return(99)",
        [
            "`return(v)` **finishes** the generator now and yields **`{value:v, done:true}`**.",
            "Later `next()` stays done. Table row **return()** — no Tryit.",
        ],
        """function* myStream() {
  yield 1;
  yield 2;
  yield 3;
}
let g = myStream();
const a = g.next();
const b = g.return(99);
const c = g.next();""",
        [
            ("a", "JSON.stringify(a)"),
            ("b", "JSON.stringify(b)"),
            ("c", "JSON.stringify(c)"),
        ],
        'a **{"value":1,"done":false}**, b **{"value":99,"done":true}**, '
        'c **{"done":true}** (no more yields).',
    ),
    S(
        "generator-throw-method",
        "generator.throw() caught inside the generator",
        [
            "`throw(err)` injects an exception **at the pause point**.",
            "If the generator **catches** it, it can `yield` again. Table row **throw()** — no Tryit.",
        ],
        """function* myStream() {
  try {
    yield 1;
    yield 2;
  } catch (e) {
    yield "caught:" + e;
  }
  yield 3;
}
let g = myStream();
const a = g.next();
const b = g.throw("boom");
const c = g.next();""",
        [
            ("a", "JSON.stringify(a)"),
            ("b", "JSON.stringify(b)"),
            ("c", "JSON.stringify(c)"),
        ],
        'a **{"value":1,"done":false}**, b **{"value":"caught:boom","done":false}**, '
        'c **{"value":3,"done":false}**.',
    ),
]


# ---------------------------------------------------------------------------
# 15.1 JS Math
# ---------------------------------------------------------------------------

MATH = [
    S(
        "math-pi",
        "Math.PI",
        [
            "`Math` is **static** — you never `new Math()`. Call properties on **`Math` itself**.",
            "`Math.PI` is the circle constant **π**.",
        ],
        "Math.PI;",
        [("Math.PI", "Math.PI")],
        "`Math.PI` is **3.141592653589793**.",
    ),
    S(
        "math-constants",
        "Eight Math constant properties",
        [
            "JavaScript exposes **8** constants: `E`, `PI`, `SQRT2`, `SQRT1_2`, `LN2`, `LN10`, `LOG2E`, `LOG10E`.",
            "One Tryit prints all eight — keep them together (the **reference** page splits them per row).",
        ],
        "Math.E;\nMath.PI;\nMath.SQRT2;\nMath.SQRT1_2;\nMath.LN2;\nMath.LN10;\nMath.LOG2E;\nMath.LOG10E;",
        [
            ("Math.E", "Math.E"),
            ("Math.PI", "Math.PI"),
            ("Math.SQRT2", "Math.SQRT2"),
            ("Math.SQRT1_2", "Math.SQRT1_2"),
            ("Math.LN2", "Math.LN2"),
            ("Math.LN10", "Math.LN10"),
            ("Math.LOG2E", "Math.LOG2E"),
            ("Math.LOG10E", "Math.LOG10E"),
        ],
        "**E** 2.718281828459045, **PI** 3.141592653589793, **SQRT2** 1.4142135623730951, "
        "**SQRT1_2** 0.7071067811865476, **LN2** 0.6931471805599453, **LN10** 2.302585092994046, "
        "**LOG2E** 1.4426950408889634, **LOG10E** 0.4342944819032518.",
    ),
    S(
        "round-4-6",
        "Math.round(4.6)",
        [
            "`Math.round(x)` is the **nearest** integer (half rounds **away from 0** toward **+∞** for positives).",
        ],
        "Math.round(4.6);",
        [("Math.round(4.6)", "Math.round(4.6)")],
        "**5**.",
    ),
    S(
        "round-4-5",
        "Math.round(4.5)",
        [
            "**4.5** is exactly halfway. Positive halves round **up** to **5**.",
        ],
        "Math.round(4.5);",
        [("Math.round(4.5)", "Math.round(4.5)")],
        "**5**.",
    ),
    S(
        "round-4-4",
        "Math.round(4.4)",
        [
            "4.4 is closer to **4** than to 5.",
        ],
        "Math.round(4.4);",
        [("Math.round(4.4)", "Math.round(4.4)")],
        "**4**.",
    ),
    S(
        "ceil",
        "Math.ceil — round toward +∞",
        [
            "`Math.ceil(x)` rounds **up** (toward **+∞**). Negative values move toward zero’s less-negative integer.",
            "Tryit uses `4.4`; the Example listing also has 4.9, 4.7, 4.2, and −4.2.",
        ],
        "Math.ceil(4.4);",
        [
            ("Math.ceil(4.4)", "Math.ceil(4.4)"),
            ("Math.ceil(4.9)", "Math.ceil(4.9)"),
            ("Math.ceil(4.7)", "Math.ceil(4.7)"),
            ("Math.ceil(4.2)", "Math.ceil(4.2)"),
            ("Math.ceil(-4.2)", "Math.ceil(-4.2)"),
        ],
        "4.4 / 4.9 / 4.7 / 4.2 → **5**. **−4.2 → −4** (up toward +∞, not away from zero).",
    ),
    S(
        "floor",
        "Math.floor — round toward −∞",
        [
            "`Math.floor(x)` rounds **down** (toward **−∞**).",
            "Tryit uses `4.7`; the listing also has 4.9, 4.4, 4.2, and −4.2.",
        ],
        "Math.floor(4.7);",
        [
            ("Math.floor(4.7)", "Math.floor(4.7)"),
            ("Math.floor(4.9)", "Math.floor(4.9)"),
            ("Math.floor(4.4)", "Math.floor(4.4)"),
            ("Math.floor(4.2)", "Math.floor(4.2)"),
            ("Math.floor(-4.2)", "Math.floor(-4.2)"),
        ],
        "Positive values → **4**. **−4.2 → −5** (down, more negative).",
    ),
    S(
        "trunc",
        "Math.trunc — integer part",
        [
            "`Math.trunc(x)` drops the fraction (**toward 0**). ES6.",
            "Unlike `floor`, **−4.2** becomes **−4**, not −5.",
        ],
        "Math.trunc(4.7);",
        [
            ("Math.trunc(4.7)", "Math.trunc(4.7)"),
            ("Math.trunc(4.9)", "Math.trunc(4.9)"),
            ("Math.trunc(4.4)", "Math.trunc(4.4)"),
            ("Math.trunc(4.2)", "Math.trunc(4.2)"),
            ("Math.trunc(-4.2)", "Math.trunc(-4.2)"),
        ],
        "Positives → **4**. **−4.2 → −4**.",
    ),
    S(
        "sign",
        "Math.sign — −1 / 0 / 1",
        [
            "`Math.sign(x)` is **1** (positive), **−1** (negative), or **0** (zero). ES6.",
            "Tryit uses `Math.sign(4)`; the listing also has −4 and 0.",
        ],
        "Math.sign(4);",
        [
            ("Math.sign(4)", "Math.sign(4)"),
            ("Math.sign(-4)", "Math.sign(-4)"),
            ("Math.sign(0)", "Math.sign(0)"),
        ],
        "**1**, **−1**, and **0**.",
    ),
    S(
        "pow",
        "Math.pow(8, 2)",
        [
            "`Math.pow(x, y)` is **x to the power y**. Same idea as `x ** y`.",
        ],
        "Math.pow(8, 2);",
        [("Math.pow(8, 2)", "Math.pow(8, 2)")],
        "**64**.",
    ),
    S(
        "sqrt",
        "Math.sqrt(64)",
        [
            "`Math.sqrt(x)` is the **square root**.",
        ],
        "Math.sqrt(64);",
        [("Math.sqrt(64)", "Math.sqrt(64)")],
        "**8**.",
    ),
    S(
        "abs",
        "Math.abs(-4.7)",
        [
            "`Math.abs(x)` is the **absolute** (non-negative) value.",
        ],
        "Math.abs(-4.7);",
        [("Math.abs(-4.7)", "Math.abs(-4.7)")],
        "**4.7**.",
    ),
    S(
        "sin-90deg",
        "Math.sin(90°) via radians",
        [
            "`Math.sin(x)` uses **radians**, not degrees.",
            "Degrees → radians: **`degrees * Math.PI / 180`**.",
        ],
        "Math.sin(90 * Math.PI / 180);",
        [("Math.sin(90 * Math.PI / 180)", "Math.sin(90 * Math.PI / 180)")],
        "**1** (sine of 90°).",
    ),
    S(
        "cos-0deg",
        "Math.cos(0°) via radians",
        [
            "`Math.cos(x)` is also in **radians**. 0° is **0** radians.",
        ],
        "Math.cos(0 * Math.PI / 180);",
        [("Math.cos(0 * Math.PI / 180)", "Math.cos(0 * Math.PI / 180)")],
        "**1** (cosine of 0°).",
    ),
    S(
        "min",
        "Math.min(0, 150, 30, 20, -8, -200)",
        [
            "`Math.min(...)` is the **lowest** argument (not an array — pass a list).",
        ],
        "Math.min(0, 150, 30, 20, -8, -200);",
        [("Math.min(0, 150, 30, 20, -8, -200)", "Math.min(0, 150, 30, 20, -8, -200)")],
        "**-200**.",
    ),
    S(
        "max",
        "Math.max(0, 150, 30, 20, -8, -200)",
        [
            "`Math.max(...)` is the **highest** argument.",
        ],
        "Math.max(0, 150, 30, 20, -8, -200);",
        [("Math.max(0, 150, 30, 20, -8, -200)", "Math.max(0, 150, 30, 20, -8, -200)")],
        "**150**.",
    ),
    S(
        "random",
        "Math.random() — sample in [0, 1)",
        [
            "`Math.random()` is **≥ 0** and **< 1**. It is **not** an integer.",
            "Each run is a new sample. The snap is one draw, not a constant.",
        ],
        "Math.random();",
        [
            ("Math.random()", "Math.random()"),
            ("in [0, 1)?", "(function(){ const r = Math.random(); return r >= 0 && r < 1; })()"),
        ],
        "The snap shows a **sample** in **[0, 1)**. Re-run for another value. Never **1**. "
        "The boolean check on a second draw is **true**.",
    ),
    S(
        "log-1",
        "Math.log(1) — natural log",
        [
            "`Math.log(x)` is **ln(x)** (base **e**). `Math.log(1)` is **0** because e⁰ = 1.",
        ],
        "Math.log(1);",
        [("Math.log(1)", "Math.log(1)")],
        "**0**.",
    ),
    S(
        "log-2",
        "Math.log(2)",
        [
            "`Math.log(2)` is **ln(2)** — the same value as **`Math.LN2`**.",
        ],
        "Math.log(2);",
        [("Math.log(2)", "Math.log(2)"), ("Math.LN2", "Math.LN2")],
        "**0.6931471805599453** (equals `Math.LN2`).",
    ),
    S(
        "log-3",
        "Math.log(3)",
        [
            "Natural log of 3 — how many times to multiply **e** to get 3.",
        ],
        "Math.log(3);",
        [("Math.log(3)", "Math.log(3)")],
        "**1.0986122886681096**.",
    ),
    S(
        "log-10",
        "Math.log(10) — times to multiply e to get 10",
        [
            "The page asks: how many times must we multiply **`Math.E`** to get **10**?",
            "That is **ln(10)**, also **`Math.LN10`**.",
        ],
        "Math.log(10);",
        [("Math.log(10)", "Math.log(10)"), ("Math.LN10", "Math.LN10")],
        "**2.302585092994046** (equals `Math.LN10`).",
    ),
    S(
        "log2-8",
        "Math.log2(8)",
        [
            "`Math.log2(x)` is log base **2**. How many times to multiply **2** to get **8**?",
        ],
        "Math.log2(8);",
        [("Math.log2(8)", "Math.log2(8)")],
        "**3** (2³ = 8).",
    ),
    S(
        "log10-1000",
        "Math.log10(1000)",
        [
            "`Math.log10(x)` is log base **10**. How many times to multiply **10** to get **1000**?",
        ],
        "Math.log10(1000);",
        [("Math.log10(1000)", "Math.log10(1000)")],
        "**3** (10³ = 1000).",
    ),
]


# ---------------------------------------------------------------------------
# 15.2 JS Math Reference (every table row is an Example)
# ---------------------------------------------------------------------------

def _mc(stem: str, name: str, meaning: str, value: str) -> dict:
    return S(
        stem,
        f"Math.{name}",
        [f"`Math.{name}` {meaning}."],
        f"Math.{name};",
        [(f"Math.{name}", f"Math.{name}")],
        f"`Math.{name}` is **{value}**.",
    )


def _mf(stem: str, call: str, meaning: str, value: str, extra: str = "") -> dict:
    bullets = [f"`Math.{call}` {meaning}."]
    if extra:
        bullets.append(extra)
    expr = f"Math.{call}"
    return S(
        stem,
        f"Math.{call}",
        bullets,
        f"{expr};",
        [(expr, expr)],
        f"`{expr}` is **{value}**.",
    )


MATH_REF: list[dict] = [
    _mf("abs", "abs(-4.7)", "returns the absolute value of x", "4.7"),
    _mf(
        "acos",
        "acos(0.5)",
        "returns the arccosine of x, in radians",
        "1.0471975511965979",
        "That is **π/3** (60°).",
    ),
    _mf("acosh", "acosh(2)", "returns the hyperbolic arccosine of x", "1.3169578969248166"),
    _mf(
        "asin",
        "asin(0.5)",
        "returns the arcsine of x, in radians",
        "0.5235987755982989",
        "That is **π/6** (30°).",
    ),
    _mf("asinh", "asinh(1)", "returns the hyperbolic arcsine of x", "0.881373587019543"),
    _mf(
        "atan",
        "atan(1)",
        "returns the arctangent of x in (−π/2, π/2) radians",
        "0.7853981633974483",
        "That is **π/4**.",
    ),
    _mf(
        "atan2",
        "atan2(8, 4)",
        "returns the arctangent of y/x, using the signs of both args (quadrant-aware)",
        "1.1071487177940904",
        "Call is **`atan2(y, x)`** — y first.",
    ),
    _mf("atanh", "atanh(0.5)", "returns the hyperbolic arctangent of x", "0.5493061443340548"),
    _mf("cbrt", "cbrt(8)", "returns the cube root of x", "2"),
    _mf("ceil", "ceil(4.4)", "returns x rounded **up** (toward +∞) to an integer", "5"),
    _mf(
        "clz32",
        "clz32(1)",
        "returns the number of leading zero bits in the 32-bit binary form of x",
        "31",
        "`1` is `...0001` in 32 bits, so **31** leading zeros.",
    ),
    _mf("cos", "cos(0)", "returns the cosine of x (radians)", "1"),
    _mf("cosh", "cosh(0)", "returns the hyperbolic cosine of x", "1"),
    _mc("e", "E", "is Euler’s number e (base of natural logs)", "2.718281828459045"),
    _mf("exp", "exp(1)", "returns **eˣ** (`Math.E ** x`)", "2.718281828459045", "Same as `Math.E`."),
    _mf("expm1", "expm1(1)", "returns **eˣ − 1** (accurate near 0)", "1.718281828459045"),
    S(
        "f16round",
        "Math.f16round(1.337)",
        [
            "`Math.f16round(x)` rounds x to the nearest **IEEE 754 binary16** (half-precision) value.",
            "The W3Schools table text (“rounded downwards to the nearest integer”) is **wrong** — that is `floor`.",
        ],
        "Math.f16round(1.337);",
        [("Math.f16round(1.337)", "Math.f16round(1.337)")],
        "**1.3369140625** (not an integer). Chrome implements this; Node 22 does not.",
    ),
    _mf("floor", "floor(4.7)", "returns x rounded **down** (toward −∞) to an integer", "4"),
    _mf(
        "fround",
        "fround(1.337)",
        "returns the nearest **32-bit** (single-precision) float",
        "1.3370000123977661",
    ),
    _mc("ln2", "LN2", "is ln(2), the natural log of 2", "0.6931471805599453"),
    _mc("ln10", "LN10", "is ln(10), the natural log of 10", "2.302585092994046"),
    _mf("log", "log(2)", "returns the natural logarithm of x (ln x)", "0.6931471805599453"),
    _mf("log10", "log10(1000)", "returns the base-10 logarithm of x", "3"),
    _mc("log10e", "LOG10E", "is log₁₀(e)", "0.4342944819032518"),
    _mf("log1p", "log1p(1)", "returns ln(1 + x) (accurate near 0)", "0.6931471805599453"),
    _mf("log2", "log2(8)", "returns the base-2 logarithm of x", "3"),
    _mc("log2e", "LOG2E", "is log₂(e)", "1.4426950408889634"),
    _mf(
        "max",
        "max(0, 150, 30, 20, -8, -200)",
        "returns the largest argument",
        "150",
    ),
    _mf(
        "min",
        "min(0, 150, 30, 20, -8, -200)",
        "returns the smallest argument",
        "-200",
    ),
    _mc("pi", "PI", "is π (ratio of circumference to diameter)", "3.141592653589793"),
    _mf("pow", "pow(8, 2)", "returns x to the power y", "64"),
    S(
        "random",
        "Math.random()",
        [
            "`Math.random()` returns a sample in **[0, 1)** (0 included, 1 excluded).",
            "The snap is one draw — not a stable constant.",
        ],
        "Math.random();",
        [("Math.random()", "Math.random()")],
        "The snap shows a **sample** in **[0, 1)**. Re-running yields another number. Never **1**.",
    ),
    _mf("round", "round(4.5)", "rounds x to the nearest integer (4.5 → 5)", "5"),
    _mf("sign", "sign(-4)", "returns the sign of x: −1, 0, or 1", "-1"),
    _mf("sin", "sin(Math.PI / 2)", "returns the sine of x (radians)", "1"),
    _mf("sinh", "sinh(1)", "returns the hyperbolic sine of x", "1.1752011936438014"),
    _mf("sqrt", "sqrt(64)", "returns the square root of x", "8"),
    _mc("sqrt1-2", "SQRT1_2", "is √(1/2) = 1/√2", "0.7071067811865476"),
    _mc("sqrt2", "SQRT2", "is √2", "1.4142135623730951"),
    S(
        "tan",
        "Math.tan(Math.PI / 4)",
        [
            "`Math.tan(x)` is the tangent of x in **radians**. π/4 is 45°.",
            "Floating-point π is not exact, so the result is **not** a clean `1`.",
        ],
        "Math.tan(Math.PI / 4);",
        [("Math.tan(Math.PI / 4)", "Math.tan(Math.PI / 4)")],
        "**0.9999999999999999** (not exactly 1).",
    ),
    _mf("tanh", "tanh(1)", "returns the hyperbolic tangent of x", "0.7615941559557649"),
    _mf("trunc", "trunc(4.7)", "returns the integer part of x (toward 0)", "4"),
    # Listed in the task; not on the W3Schools July 2025 table.
    S(
        "hypot",
        "Math.hypot(3, 4) — extra (not on the July 2025 table)",
        [
            "`Math.hypot(...)` is the square root of the sum of squares (Euclidean length).",
            "**Not** a row on the live W3Schools table (revised July 2025). Still a standard `Math` method.",
        ],
        "Math.hypot(3, 4);",
        [("Math.hypot(3, 4)", "Math.hypot(3, 4)")],
        "**5** (3-4-5 triangle).",
    ),
    S(
        "imul",
        "Math.imul(2, 4) — extra (not on the July 2025 table)",
        [
            "`Math.imul(a, b)` is **32-bit integer** multiply (C-like `int32`).",
            "**Not** a row on the live W3Schools table. Overflow wraps in 32-bit two’s complement.",
        ],
        "Math.imul(2, 4);\nMath.imul(0xffffffff, 5);",
        [
            ("Math.imul(2, 4)", "Math.imul(2, 4)"),
            ("Math.imul(0xffffffff, 5)", "Math.imul(0xffffffff, 5)"),
        ],
        "`imul(2, 4)` is **8**. `imul(0xffffffff, 5)` is **−5** (32-bit wrap: −1 × 5).",
    ),
]


# ---------------------------------------------------------------------------
# 15.3 JS Math Random
# ---------------------------------------------------------------------------

def _rnd_int(stem: str, title: str, expr: str, lo: int, hi: int, bullets: list[str]) -> dict:
    return S(
        stem,
        title,
        bullets,
        f"{expr};",
        [(expr, expr), ("in range?", f"(function(){{ const n = {expr}; return n >= {lo} && n <= {hi} && Number.isInteger(n); }})()")],
        f"The snap shows a **sample integer in [{lo}, {hi}]**. Re-running can produce any integer in that range. "
        f"The range check on a second draw is **true**.",
    )


RANDOM = [
    S(
        "random",
        "Math.random() — [0, 1)",
        [
            "`Math.random()` is **≥ 0** and **< 1**. Always **lower than 1**.",
            "The snap is one sample, not a fixed teaching constant.",
        ],
        "Math.random();",
        [
            ("Math.random()", "Math.random()"),
            ("in [0, 1)?", "(function(){ const r = Math.random(); return r >= 0 && r < 1; })()"),
        ],
        "The snap shows a **sample in [0, 1)**. Never **1**. A second draw still satisfies the range check.",
    ),
    _rnd_int(
        "int-0-9",
        "Math.floor(Math.random() * 10) — [0, 9]",
        "Math.floor(Math.random() * 10)",
        0,
        9,
        [
            "`Math.random() * 10` is **[0, 10)**. `floor` then yields integers **0 through 9**.",
            "There are no JavaScript integers as a type — this is a **number with no fraction**.",
        ],
    ),
    _rnd_int(
        "int-0-10",
        "Math.floor(Math.random() * 11) — [0, 10]",
        "Math.floor(Math.random() * 11)",
        0,
        10,
        [
            "Multiply by **11** (not 10) to include **10**. Range is **[0, 10]**.",
        ],
    ),
    _rnd_int(
        "int-0-99",
        "Math.floor(Math.random() * 100) — [0, 99]",
        "Math.floor(Math.random() * 100)",
        0,
        99,
        [
            "`* 100` then `floor` → integers **0 through 99**.",
        ],
    ),
    _rnd_int(
        "int-0-100",
        "Math.floor(Math.random() * 101) — [0, 100]",
        "Math.floor(Math.random() * 101)",
        0,
        100,
        [
            "`* 101` then `floor` → **0 through 100** (100 included).",
        ],
    ),
    _rnd_int(
        "int-1-10",
        "Math.floor(Math.random() * 10) + 1 — [1, 10]",
        "Math.floor(Math.random() * 10) + 1",
        1,
        10,
        [
            "`* 10` then `floor` is **[0, 9]**; **`+ 1`** shifts to **[1, 10]**.",
        ],
    ),
    _rnd_int(
        "int-1-100",
        "Math.floor(Math.random() * 100) + 1 — [1, 100]",
        "Math.floor(Math.random() * 100) + 1",
        1,
        100,
        [
            "Same shift: **[0, 99] + 1 → [1, 100]**.",
        ],
    ),
    S(
        "rnd-min-max-excl",
        "getRndInteger(min, max) — max excluded",
        [
            "`Math.floor(Math.random() * (max - min)) + min` includes **min**, excludes **max**.",
            "The Tryit button calls `getRndInteger(0, 10)` → integers **[0, 9]**.",
            "This page auto-runs once so the screenshot is not blank; the button re-rolls.",
        ],
        "function getRndInteger(min, max) {\n  return Math.floor(Math.random() * (max - min)) + min;\n}",
        outcome=(
            "The snap shows a **sample integer in [0, 9]** from `getRndInteger(0, 10)`. "
            "Max is **excluded**. Clicking yields another value in that range."
        ),
        script="""      function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min)) + min;
      }
      document.getElementById("demo").innerText = String(getRndInteger(0, 10));""",
        buttons='<p><button type="button" onclick="document.getElementById(\'demo\').innerText = String(getRndInteger(0, 10))">Click Me</button></p>',
    ),
    S(
        "rnd-min-max-incl",
        "getRndInteger(min, max) — both included",
        [
            "`Math.floor(Math.random() * (max - min + 1)) + min` includes **both** ends.",
            "The Tryit button calls `getRndInteger(1, 10)` → integers **[1, 10]**.",
            "Auto-run once for the screenshot; the button re-rolls.",
        ],
        "function getRndInteger(min, max) {\n  return Math.floor(Math.random() * (max - min + 1) ) + min;\n}",
        outcome=(
            "The snap shows a **sample integer in [1, 10]** from `getRndInteger(1, 10)`. "
            "Both ends **included**. Clicking yields another value in that range."
        ),
        script="""      function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
      }
      document.getElementById("demo").innerText = String(getRndInteger(1, 10));""",
        buttons='<p><button type="button" onclick="document.getElementById(\'demo\').innerText = String(getRndInteger(1, 10))">Click Me</button></p>',
    ),
]


def run_all() -> None:
    sections = [
        (
            "js-iterations",
            "JS Iterations",
            ITERATIONS,
            "JavaScript loops repeat a block. for uses init / condition / increment when the trip count is known. while and do...while follow a condition — do...while always runs once. for...in walks object keys; for...of walks iterable values. Array forEach is a method alternative. Always increment a while-condition variable or the loop never ends.",
            [
                "**`for (exp1; exp2; exp3)`** — init once, test, body, increment.",
                "**`while`** tests first. **`do...while`** runs the body first (at least once).",
                "**`for...in`** → enumerable **keys**. **`for...of`** → iterable **values**.",
                "**`forEach()`** is an Array method (also listed with map / filter / reduce).",
                "Forgetting to increment a `while` / `do...while` variable is an **infinite loop**.",
            ],
            [
                ("When do you use `for` vs `while`?", ["**`for`** when the count is known (init / test / increment).", "**`while`** when you keep going while a condition stays true."]),
                ("What are exp1, exp2, exp3 in `for`?", ["**exp1** runs once (init).", "**exp2** is the continue condition.", "**exp3** runs after each body (usually increment)."]),
                ("What does the page’s `for` Tryit print?", ["**The number is 0** through **The number is 4**."]),
                ("What does the `while (i < 10)` Tryit print?", ["**0** through **9**. After the loop `i` is **10**."]),
                ("How is `do...while` different from `while`?", ["The body runs **before** the test, so it always runs **at least once**."]),
                ("What does `for...in` on `{fname, lname, age}` build?", ['**"John Doe 25 "** — values of those keys, space-separated.']),
                ("What does `for...of` iterate?", ["**Values** of an **iterable** (arrays, strings, Maps, Sets) — not object keys."]),
                ("What did the extra `forEach` print?", ["**45, 4, 9, 16, 25** (one per line)."]),
                ("What happens if you forget to increment in `while`?", ["The condition never becomes false — **infinite loop** (can freeze the page)."]),
                ("Is `forEach` a loop keyword?", ["**No.** It is **`Array.prototype.forEach`**, listed under other methods on this page."]),
            ],
            "Pick for when the trip count is known, while/do...while for a condition (do runs once first), for...in for object keys, and for...of / forEach for values. Always advance the condition variable.",
            [
                ("JS Iterations (W3Schools)", "https://www.w3schools.com/js/js_looping.asp"),
                ("MDN: Loops and iteration", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration"),
                ("MDN: for...of", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of"),
            ],
        ),
        (
            "js-iterables",
            "JS Iterables",
            ITERABLES,
            "An iterable can be walked with for...of because it implements Symbol.iterator. Strings, Arrays, Typed Arrays, Sets, and Maps are iterable. for...of on a Map yields [key, value] pairs. A homemade object with only next() is an iterator, not an iterable — for...of needs Symbol.iterator. When done is true, for...of and a manual while(result.done) break omit that completion value.",
            [
                "**Iterating** means looping a sequence. **`for...of`** is the language loop for iterables.",
                "Built-in iterables: **String, Array, TypedArray, Set, Map** (their prototypes have **`Symbol.iterator`**).",
                "An **iterator** implements **`next()` → `{value, done}`**. An **iterable** implements **`Symbol.iterator`**.",
                "Home-made `next()`-only objects **do not** support `for...of`.",
                "`for...of` / `if (result.done) break` **do not yield** the `{done:true}` value (here: **100** is omitted).",
            ],
            [
                ("What makes an object iterable?", ["It has **`obj[Symbol.iterator]`**, a function that returns an iterator."]),
                ("What must `next()` return?", ["An object with **`value`** and **`done`** (boolean)."]),
                ("What does `for...of` on `\"W3Schools\"` print?", ["Each character: **W 3 S c h o o l s**."]),
                ("What does `for...of` on a Map yield?", ["**`[key, value]`** pairs. `String` of `['apples',500]` is **apples,500**."]),
                ("Can the home-made `myNumbers()` next-only object use `for...of`?", ["**No.** It has `next` but no **`Symbol.iterator`**."]),
                ("What does that next-only demo display after four `next()` calls?", ["**40** (`10, 20, 30`, then the displayed fourth value). `done` stays **false**."]),
                ("What numbers does the `Symbol.iterator` homemade object yield?", ["**10 through 90**. **100** has `done:true` and is **not** printed."]),
                ("Does calling `Symbol.iterator()` yourself change the sequence?", ["**No.** The manual `while` loop prints the same **10–90**."]),
                ("Which built-ins are listed as iterable?", ["**Strings, Arrays, Typed Arrays, Sets, Maps**."]),
                ("What is `done`?", ["**true** when the iterator has finished; **false** when it produced a new `value`."]),
                ("Is a string iterated by index or by character?", ["By **character** (`for...of`). Indexes would be a `for` loop or `for...in`."]),
            ],
            "Use for...of on strings, arrays, maps, and sets. Custom sequences need Symbol.iterator returning next(). A next()-only object is an iterator, not an iterable. done:true values are completion results, not loop items.",
            [
                ("JS Iterables (W3Schools)", "https://www.w3schools.com/js/js_iterables.asp"),
                ("MDN: Iteration protocols", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols"),
                ("MDN: Symbol.iterator", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator"),
            ],
        ),
        (
            "js-iterators",
            "JS Iterators",
            ITERATORS,
            "An iterator follows the iterator protocol: next() returns {value, done}. Built-in iterables expose Symbol.iterator. ECMAScript 2025 adds Iterator helper methods (from, drop, take, map, filter, flatMap, forEach, find, every, some, reduce) so you can transform a stream without first copying it into an Array. Iterator.from wraps an iterable. Helpers that return iterators are lazy; every / some / find / reduce / forEach consume the iterator to a result.",
            [
                "**`next()`** → `{value, done}`. **`done:true`** means no more elements.",
                "Built-ins are iterable because **`Symbol.iterator`** lives on the prototype.",
                "**`Iterator.from(x)`** makes an Iterator helper from an iterable or iterator.",
                "**Lazy helpers:** `drop`, `take`, `map`, `filter`, `flatMap` return **iterators**.",
                "**Eager helpers:** `every`, `some`, `find`, `reduce`, `forEach` walk the rest of the stream now.",
            ],
            [
                ("What does `arr[Symbol.iterator]().next()` look like?", ['First of `["a","b"]` is **`{"value":"a","done":false}`**. After the end: **`done:true`**.']),
                ("What does `Iterator.from([1,2,3])` print in `for...of`?", ["**1, 2, 3**."]),
                ("What does `drop(5)` on `[1..6]` leave?", ["**6** only."]),
                ("Why is `every(x => x > 7)` on `\"123456789\"` false?", ["`'1' > 7` is **false** (coerced to number). `every` fails immediately."]),
                ("What does `filter(x => x > 18)` keep from `[32,33,16,40]`?", ["**32, 33, 40**."]),
                ("What does `find(x => x > 18)` return from `[3,10,18,30,20]`?", ["**30** (18 is not greater than 18)."]),
                ("What does `flatMap(x => [x, x*10])` produce for 1..6?", ["**1, 10, 2, 20, … 6, 60**."]),
                ("What does `map(x => x * 2)` do to the digit string?", ["**2, 4, 6, … 18** (characters coerce to numbers)."]),
                ("What is `reduce` of `[175, 50, 25]` with add?", ["**250**."]),
                ("Is `some(x => x > 7)` on that digit string true?", ["**Yes** — `'8'` and `'9'` pass."]),
                ("What does `take(5)` on `[1..6]` yield?", ["**1, 2, 3, 4, 5**."]),
                ("Does `forEach` return a new iterator?", ["**No.** It runs the callback and returns **undefined**; this demo concatenates **123456789**."]),
            ],
            "Call next() for {value, done}. Use Iterator.from plus the ES2025 helpers to skip, take, map, filter, or reduce a stream. String digits coerce in numeric callbacks. drop/take/map/filter/flatMap stay lazy; every/some/find/reduce/forEach consume.",
            [
                ("JS Iterators (W3Schools)", "https://www.w3schools.com/js/js_iterators.asp"),
                ("MDN: Iterator", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator"),
                ("MDN: Iterator.from", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from"),
            ],
        ),
        (
            "js-generators",
            "JS Generators",
            GENERATORS,
            "A generator function (function*) returns a Generator object that is both iterable and an iterator. yield pauses and produces a value; the function resumes on next(). return finishes with done:true — for...of does not print that value, but next() still reports it. Generator methods are next, return, and throw.",
            [
                "Declare with **`function*`**. The call returns a **Generator**, not the first value.",
                "**`yield`** → `{value, done:false}` and pause. **`return`** → `{value, done:true}` and finish.",
                "**`for...of` exits when done is true** — a final `return 3` is **not** looped.",
                "Yield all values you want in `for...of`. The second Tryit uses **`yield 3`** (the page typo `yeald` is not in the Tryit).",
                "Methods: **`next()`**, **`return(v)`** finish now, **`throw(e)`** inject an error at the pause.",
            ],
            [
                ("What does `function*` return when called?", ["A **Generator object**, not a single return value."]),
                ("What does `for...of` print for `yield 1; yield 2; return 3`?", ["**1** and **2** only. **3** is the completion value (`done:true`)."]),
                ("How do you include 3 in `for...of`?", ["**`yield 3`**, not `return 3`."]),
                ("What is the third `next()` after two yields and `return 3`?", ['**`{"value":3,"done":true}`**. A fourth `next()` is done with **undefined** value.']),
                ("What does `return(99)` do after the first yield?", ['Finishes immediately: **`{"value":99,"done":true}`**. Further `next()` stays done.']),
                ("What does `throw(\"boom\")` do if the generator catches it?", ["It resumes in the `catch`; this demo then **`yield \"caught:boom\"`** and later **yield 3**."]),
                ("Is a generator iterable?", ["**Yes.** It is both **iterable** and an **iterator** (`for...of` and `next()` both work)."]),
                ("Does `yield` lose local state?", ["**No.** Locals are kept until the next `next()` resumes at that `yield`."]),
                ("What are the three generator object methods?", ["**`next()`**, **`return()`**, **`throw()`**."]),
                ("Did the live Tryit use `yeald`?", ["**No.** The Tryit is **`yield 3`**. The tutorial prose typo is not in the runnable code."]),
            ],
            "Write function*, yield values you want in for...of, and use next() to see {value, done}. return on the generator (or a return in the body) completes the stream. throw injects an error at the pause point.",
            [
                ("JS Generators (W3Schools)", "https://www.w3schools.com/js/js_generators.asp"),
                ("MDN: function*", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*"),
                ("MDN: Generator", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator"),
            ],
        ),
        (
            "js-math",
            "JS Math",
            MATH,
            "Math is a static object: call Math.PI and Math.method(x) without constructing it. Eight constants cover e, π, roots, and log bases. round / ceil / floor / trunc convert to integers differently (especially on negatives). Trigonometry is in radians (degrees * PI / 180). min and max take an argument list. random is a sample in [0, 1). log is natural log; log2 and log10 are the named bases.",
            [
                "**`Math` is static** — no `new Math()`.",
                "**8 constants:** E, PI, SQRT2, SQRT1_2, LN2, LN10, LOG2E, LOG10E.",
                "**Integers:** `round` nearest, `ceil` toward +∞, `floor` toward −∞, `trunc` toward 0. **`sign`** is −1 / 0 / 1.",
                "**Trig in radians.** `sin(90 * PI/180)` is **1**.",
                "`min` / `max` take a **list of arguments**. `random()` ∈ **[0, 1)**.",
                "`log` is **ln**. `log2(8)` is **3**. `log10(1000)` is **3**.",
            ],
            [
                ("Do you write `new Math()`?", ["**No.** All properties are **static** on `Math`."]),
                ("What is `Math.PI`?", ["**3.141592653589793**."]),
                ("What are the eight constants?", ["**E, PI, SQRT2, SQRT1_2, LN2, LN10, LOG2E, LOG10E**."]),
                ("`Math.round(4.6)`, `(4.5)`, `(4.4)`?", ["**5**, **5**, **4**."]),
                ("`Math.ceil(-4.2)` vs `Math.floor(-4.2)` vs `Math.trunc(-4.2)`?", ["ceil **−4**, floor **−5**, trunc **−4**."]),
                ("What is `Math.sign(-4)`?", ["**−1**. Zero → **0**. Positive → **1**."]),
                ("`Math.pow(8,2)` and `Math.sqrt(64)`?", ["**64** and **8**."]),
                ("How do you take sine of 90 degrees?", ["`Math.sin(90 * Math.PI / 180)` → **1**."]),
                ("`Math.min` / `Math.max` of `0, 150, 30, 20, -8, -200`?", ["min **−200**, max **150**."]),
                ("What range is `Math.random()`?", ["**[0, 1)** — the snap is a sample, never **1**."]),
                ("`Math.log(1)` and `Math.log(10)`?", ["**0** and **2.302585092994046** (`LN10`)."]),
                ("`Math.log2(8)` and `Math.log10(1000)`?", ["**3** and **3**."]),
            ],
            "Use Math without constructing it. Pick round/ceil/floor/trunc by rounding direction. Convert degrees to radians for sin/cos. min/max take a list. random is [0, 1). log is ln; use log2/log10 for those bases.",
            [
                ("JS Math (W3Schools)", "https://www.w3schools.com/js/js_math.asp"),
                ("MDN: Math", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math"),
                ("MDN: Math.random", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random"),
            ],
        ),
        (
            "js-math-reference",
            "JS Math Reference",
            MATH_REF,
            "The Math reference table (revised July 2025) lists every constant and method as its own row. Each row is its own Example with a real return value. f16round is IEEE binary16 rounding — the table’s “rounded downwards to the nearest integer” text is incorrect (that is floor). hypot and imul are standard Math methods that are not on this table; they still each get an Example. random remains a [0, 1) sample.",
            [
                "**Every table row is an Example** — constants and methods, not a bullet list of names.",
                "Live table (July 2025): abs through trunc as listed on the page, including **E, LN2, LN10, LOG2E, LOG10E, PI, SQRT1_2, SQRT2** and **f16round / fround / clz32**.",
                "**`f16round(1.337)` is 1.3369140625**, not an integer. The W3Schools description copies `floor` by mistake.",
                "**`tan(π/4)` is 0.9999999999999999** (π is approximate), not exactly 1.",
                "**`hypot` and `imul`** are extra (not on the live table) because they are standard `Math` methods named in the task list.",
            ],
            [
                ("Is this page a catalog?", ["**Yes.** One Example **per table row**, not one snippet for many names."]),
                ("What is `Math.E`?", ["**2.718281828459045**."]),
                ("What is `Math.clz32(1)`?", ["**31** leading zeros in the 32-bit form of 1."]),
                ("What does `f16round` actually do?", ["Nearest **binary16** float. `f16round(1.337)` is **1.3369140625**. It is **not** `floor`."]),
                ("What is `Math.fround(1.337)`?", ["**1.3370000123977661** (IEEE 32-bit)."]),
                ("`atan2` argument order?", ["**`atan2(y, x)`** — y first. `atan2(8, 4)` is **1.1071487177940904**."]),
                ("`Math.max` / `Math.min` of the page’s list?", ["**150** and **−200**."]),
                ("What is `Math.sign(-4)`?", ["**−1**."]),
                ("Why isn’t `tan(π/4)` exactly 1?", ["`Math.PI / 4` is not a perfect 45° in binary float → **0.9999999999999999**."]),
                ("Are `hypot` and `imul` on the July 2025 table?", ["**No.** Still run: `hypot(3,4)` is **5**; `imul(2,4)` is **8**; `imul(0xffffffff, 5)` is **−5**."]),
                ("What is `Math.random()` here?", ["A **sample in [0, 1)** — not a fixed number."]),
                ("`exp(1)` vs `expm1(1)`?", ["**e** (2.718…) vs **e − 1** (1.718…)."]),
            ],
            "Treat the reference as a catalog: one run per row. Trust the engine’s number, not the f16round table sentence. trig is radians; atan2 is (y, x). hypot and imul exist even when omitted from this table.",
            [
                ("JS Math Reference (W3Schools)", "https://www.w3schools.com/js/js_math_reference.asp"),
                ("MDN: Math", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math"),
                ("MDN: Math.f16round", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/f16round"),
                ("MDN: Math.hypot", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/hypot"),
                ("MDN: Math.imul", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/imul"),
            ],
        ),
        (
            "js-math-random",
            "JS Math Random",
            RANDOM,
            "Math.random() samples [0, 1). Scale with a multiplier and Math.floor to get integers. *10 then floor is [0, 9]; add 1 to shift to [1, 10]; use *11 to include 10 in a 0-based range. A helper with (max - min) excludes max; (max - min + 1) includes both ends. Snaps are samples — re-run for another value in the same range.",
            [
                "`Math.random()` ∈ **[0, 1)** — 0 included, **1 never**.",
                "`Math.floor(Math.random() * N)` → integers **0 .. N−1**.",
                "`+ 1` after floor shifts a 0-based range up (e.g. **[0,9] → [1,10]**).",
                "**Proper helpers:** `(max - min)` excludes max; `(max - min + 1)` includes both.",
                "Snaps show **one sample**. Outcomes name the **range**, not a promised digit.",
            ],
            [
                ("What range is `Math.random()`?", ["**0 inclusive, 1 exclusive.** The snap is a sample in **[0, 1)**."]),
                ("What integers does `Math.floor(Math.random() * 10)` produce?", ["**0 through 9** (both included)."]),
                ("Why `* 11` for 0 through 10?", ["`* 10` only reaches **[0, 9]**. `* 11` then `floor` includes **10**."]),
                ("`Math.floor(Math.random() * 100)` range?", ["**[0, 99]**."]),
                ("`Math.floor(Math.random() * 101)` range?", ["**[0, 100]**."]),
                ("How do you get **1 through 10**?", ["`Math.floor(Math.random() * 10) + 1`."]),
                ("How do you get **1 through 100**?", ["`Math.floor(Math.random() * 100) + 1`."]),
                ("What does the max-**excluded** helper do for `(0, 10)`?", ["Integers **[0, 9]**. Formula: `(max - min)` without `+ 1`."]),
                ("What does the max-**included** helper do for `(1, 10)`?", ["Integers **[1, 10]**. Formula: `(max - min + 1)`."]),
                ("Are these cryptographic random numbers?", ["**No.** `Math.random()` is a PRNG for demos/games, not security."]),
                ("Will two screenshots of `Math.random()` match?", ["**Usually not.** Each load is a new sample in the same range."]),
            ],
            "Scale Math.random() with floor for integer ranges. Count the span carefully (*10 is 0–9, *11 is 0–10). Prefer a named helper: exclude max with (max-min), include both with (max-min+1). Treat every snap as a sample in that range.",
            [
                ("JS Random (W3Schools)", "https://www.w3schools.com/js/js_random.asp"),
                ("MDN: Math.random", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random"),
            ],
        ),
    ]

    import sys

    wanted = set(sys.argv[1:])
    print("example counts:")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        print(f"  {slug}: {len(recs)}")
        nqa = len(qa)
        if not (8 <= nqa <= 15):
            raise SystemExit(f"{slug} Q&A count {nqa} not in 8-15")
    for slug, title, recs, intro, concepts, qa, summary, refs in sections:
        if wanted and slug not in wanted:
            continue
        print("building", slug, "examples", len(recs))
        build_and_snap(slug, title, recs, intro, concepts, qa, summary, refs)
        print("done", slug)


if __name__ == "__main__":
    run_all()
