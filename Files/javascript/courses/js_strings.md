# JS Strings

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Strings store **text**. Write them with **single** or **double** quotes (same result), or **backticks** (templates). Use **`length`**, **escape** quotes with `\`, break long lines **after an operator** or with **`+`**, and prefer **literals** over `new String()`. Each Tryit on the W3Schools page is its own Example, the same grain as **JS Output**.

This section has **16** examples:

- [x] **Example 1:** String with quotes [View](#js-strings-example-01)
- [x] **Example 2:** Single vs double quotes [View](#js-strings-example-02)
- [x] **Example 3:** Quotes inside quotes [View](#js-strings-example-03)
- [x] **Example 4:** Template backticks with mixed quotes [View](#js-strings-example-04)
- [x] **Example 5:** `length` of A-Z [View](#js-strings-example-05)
- [x] **Example 6:** Escape \" double quote [View](#js-strings-example-06)
- [x] **Example 7:** Escape \' single quote [View](#js-strings-example-07)
- [x] **Example 8:** Escape \\ backslash [View](#js-strings-example-08)
- [x] **Example 9:** Break a long line after an operator [View](#js-strings-example-09)
- [x] **Example 10:** Break a string with `+` [View](#js-strings-example-10)
- [x] **Example 11:** Multiline template string [View](#js-strings-example-11)
- [x] **Example 12:** `new String()` vs a literal [View](#js-strings-example-12)
- [x] **Example 13:** Literal `==` String object [View](#js-strings-example-13)
- [x] **Example 14:** Literal `===` String object [View](#js-strings-example-14)
- [x] **Example 15:** Two String objects with `==` [View](#js-strings-example-15)
- [x] **Example 16:** Two String objects with `===` [View](#js-strings-example-16)

## Detailed Explanation

- [x] **Quotes** — `'text'` and `"text"` are the same; inner quotes must differ from the outer ones, or use a template / escape.
- [x] **Escape** — `\"` `\'` `\\` put a quote or backslash in the string. Typewriter escapes like `\n` exist but do not matter in HTML.
- [x] **Long lines** — break after an operator, or split a string with `+`. Templates may span lines.
- [x] **Do not use `new String()`** — it is an object. `==` against a literal can be **true** while `===` is **false**; two String objects compare **false**.

<a id="js-strings-example-01"></a>

### **Example 1: String with quotes**

- [x] A JavaScript string is **zero or more characters** written inside quotes.
- [x] This Tryit stores the name **John Doe**.

Sandbox: `code_sandbox/js-strings/quotes.html`

```javascript
let text = "John Doe";
```

![js-strings example 1 source](../code_sandbox/snaps/js-strings-01-code.png)

![js-strings example 1 result](../code_sandbox/snaps/js-strings-01-result.png)

- [x] **Outcome:** The variable holds **John Doe**.

<a id="js-strings-example-02"></a>

### **Example 2: Single vs double quotes**

- [x] You can use **single** or **double** quotes around a string.
- [x] There is **no difference** between the two for ordinary text.

Sandbox: `code_sandbox/js-strings/single-double.html`

```javascript
let carName1 = "Volvo XC60";
let carName2 = "Volvo XC60";
```

![js-strings example 2 source](../code_sandbox/snaps/js-strings-02-code.png)

![js-strings example 2 result](../code_sandbox/snaps/js-strings-02-result.png)

- [x] **Outcome:** Both values are **Volvo XC60**; they compare equal.

<a id="js-strings-example-03"></a>

### **Example 3: Quotes inside quotes**

- [x] You can put quotes **inside** a string if they **do not match** the outer quotes.
- [x] `"It's alright"` uses a double-quoted string so the apostrophe is legal.
- [x] The third form uses single quotes around a name in **double** quotes.

Sandbox: `code_sandbox/js-strings/quotes-inside.html`

```javascript
let answer1 = "It's alright";
let answer2 = "He is called 'Johnny'";
let answer3 = 'He is called "Johnny"';
```

![js-strings example 3 source](../code_sandbox/snaps/js-strings-03-code.png)

![js-strings example 3 result](../code_sandbox/snaps/js-strings-03-result.png)

- [x] **Outcome:** The three strings are **It's alright**, **He is called 'Johnny'**, and **He is called "Johnny"**.

<a id="js-strings-example-04"></a>

### **Example 4: Template backticks with mixed quotes**

- [x] **Template strings** (ES6) use **backticks** `` ` ``.
- [x] Backticks allow **both** single and double quotes inside the same string.

Sandbox: `code_sandbox/js-strings/template-quotes.html`

```javascript
let text = `He's often called "Johnny"`;
```

![js-strings example 4 source](../code_sandbox/snaps/js-strings-04-code.png)

![js-strings example 4 result](../code_sandbox/snaps/js-strings-04-result.png)

- [x] **Outcome:** The template prints **He's often called "Johnny"**.

<a id="js-strings-example-05"></a>

### **Example 5: `length` of A-Z**

- [x] **`length`** is a **property**, not a method — no parentheses.
- [x] It counts the characters in the string (UTF-16 code units).

Sandbox: `code_sandbox/js-strings/length.html`

```javascript
let text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length = text.length;
```

![js-strings example 5 source](../code_sandbox/snaps/js-strings-05-code.png)

![js-strings example 5 result](../code_sandbox/snaps/js-strings-05-result.png)

- [x] **Outcome:** A-Z is **26** characters.

<a id="js-strings-example-06"></a>

### **Example 6: Escape \" double quote**

- [x] JavaScript would **chop** `"We are the so-called "Vikings" ..."` at the inner quote.
- [x] **`\"`** inserts a literal double quote inside a double-quoted string.

Sandbox: `code_sandbox/js-strings/escape-double.html`

```javascript
let text = 'We are the so-called "Vikings" from the north.';
```

![js-strings example 6 source](../code_sandbox/snaps/js-strings-06-code.png)

![js-strings example 6 result](../code_sandbox/snaps/js-strings-06-result.png)

- [x] **Outcome:** The printed text is **We are the so-called "Vikings" from the north.**

<a id="js-strings-example-07"></a>

### **Example 7: Escape \' single quote**

- [x] **`\'`** inserts a literal apostrophe inside a single-quoted string.
- [x] This is the other way to write **It's alright** without switching quote styles.

Sandbox: `code_sandbox/js-strings/escape-single.html`

```javascript
let text = "It's alright.";
```

![js-strings example 7 source](../code_sandbox/snaps/js-strings-07-code.png)

![js-strings example 7 result](../code_sandbox/snaps/js-strings-07-result.png)

- [x] **Outcome:** The printed text is **It's alright.**

<a id="js-strings-example-08"></a>

### **Example 8: Escape \\ backslash**

- [x] **`\\`** inserts a literal **backslash**.
- [x] The other typewriter-era escapes (`\n`, `\t`, `\b`, `\f`, `\r`, `\v`) are valid JS but do not matter in HTML.

Sandbox: `code_sandbox/js-strings/escape-backslash.html`

```javascript
let text = "The character \\ is called backslash.";
```

![js-strings example 8 source](../code_sandbox/snaps/js-strings-08-code.png)

![js-strings example 8 result](../code_sandbox/snaps/js-strings-08-result.png)

- [x] **Outcome:** The printed text is **The character \ is called backslash.**

<a id="js-strings-example-09"></a>

### **Example 9: Break a long line after an operator**

- [x] A **safe** place to break a statement is **after an operator** (here, after `=`).
- [x] Do not break in the middle of a quoted string without `+` or a template.

Sandbox: `code_sandbox/js-strings/break-operator.html`

```javascript
document.getElementById("demo").innerHTML = "Hello Dolly!";
```

![js-strings example 9 source](../code_sandbox/snaps/js-strings-09-code.png)

![js-strings example 9 result](../code_sandbox/snaps/js-strings-09-result.png)

- [x] **Outcome:** The output is **Hello Dolly!**

<a id="js-strings-example-10"></a>

### **Example 10: Break a string with `+`**

- [x] A safe way to split a **string** across lines is **string addition** with **`+`**.
- [x] Each piece is its own quoted string; `+` concatenates them.

Sandbox: `code_sandbox/js-strings/break-plus.html`

```javascript
document.getElementById("demo").innerHTML = "Hello " + "Dolly!";
```

![js-strings example 10 source](../code_sandbox/snaps/js-strings-10-code.png)

![js-strings example 10 result](../code_sandbox/snaps/js-strings-10-result.png)

- [x] **Outcome:** The joined string is **Hello Dolly!**

<a id="js-strings-example-11"></a>

### **Example 11: Multiline template string**

- [x] Templates also allow **multiline** strings — newlines inside backticks are **kept**.
- [x] This is the same backtick syntax as the quotes-inside example, now spanning lines.

Sandbox: `code_sandbox/js-strings/multiline-template.html`

```javascript
let text = `The quick
brown fox
jumps over
the lazy dog`;
```

![js-strings example 11 source](../code_sandbox/snaps/js-strings-11-code.png)

![js-strings example 11 result](../code_sandbox/snaps/js-strings-11-result.png)

- [x] **Outcome:** The string keeps the line breaks: **The quick / brown fox / jumps over / the lazy dog**.

<a id="js-strings-example-12"></a>

### **Example 12: `new String()` vs a literal**

- [x] Normally strings are **primitives** from literals: `let x = "John";`
- [x] `new String("John")` creates a String **object**. Do **not** do this — it is slower and surprising.

Sandbox: `code_sandbox/js-strings/string-objects.html`

```javascript
let x = "John";
let y = new String("John");
```

![js-strings example 12 source](../code_sandbox/snaps/js-strings-12-code.png)

![js-strings example 12 result](../code_sandbox/snaps/js-strings-12-result.png)

- [x] **Outcome:** `x` is a **string** primitive; `y` is an **object**. Both display as **John**.

<a id="js-strings-example-13"></a>

### **Example 13: Literal `==` String object**

- [x] **`==`** converts types, so a string literal and a String object with the same text compare **equal**.
- [x] That hidden conversion is why `new String()` is a trap.

Sandbox: `code_sandbox/js-strings/equal-loose.html`

```javascript
let x = "John";
let y = new String("John");
x == y;
```

![js-strings example 13 source](../code_sandbox/snaps/js-strings-13-code.png)

![js-strings example 13 result](../code_sandbox/snaps/js-strings-13-result.png)

- [x] **Outcome:** `x == y` is **true**.

<a id="js-strings-example-14"></a>

### **Example 14: Literal `===` String object**

- [x] **`===`** requires the **same type** as well as the same value.
- [x] A primitive string is **not** strictly equal to a String object.

Sandbox: `code_sandbox/js-strings/equal-strict.html`

```javascript
let x = "John";
let y = new String("John");
x === y;
```

![js-strings example 14 source](../code_sandbox/snaps/js-strings-14-code.png)

![js-strings example 14 result](../code_sandbox/snaps/js-strings-14-result.png)

- [x] **Outcome:** `x === y` is **false**.

<a id="js-strings-example-15"></a>

### **Example 15: Two String objects with `==`**

- [x] Comparing **two objects** with `==` still asks “are these the **same object**?”
- [x] Two separately constructed String objects are never the same object.

Sandbox: `code_sandbox/js-strings/two-objects-loose.html`

```javascript
let x = new String("John");
let y = new String("John");
x == y;
```

![js-strings example 15 source](../code_sandbox/snaps/js-strings-15-code.png)

![js-strings example 15 result](../code_sandbox/snaps/js-strings-15-result.png)

- [x] **Outcome:** `x == y` is **false**.

<a id="js-strings-example-16"></a>

### **Example 16: Two String objects with `===`**

- [x] **`===`** between two objects is also identity: they must be the **same** object.
- [x] Comparing two JavaScript objects **always returns false** when they are distinct instances.

Sandbox: `code_sandbox/js-strings/two-objects-strict.html`

```javascript
let x = new String("John");
let y = new String("John");
x === y;
```

![js-strings example 16 source](../code_sandbox/snaps/js-strings-16-code.png)

![js-strings example 16 result](../code_sandbox/snaps/js-strings-16-result.png)

- [x] **Outcome:** `x === y` is **false**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-strings/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `let text = "John Doe"` store?

<details>
<summary>Answer</summary>

- [x] The string **John Doe**.

</details>

### Question 2: Is `'Volvo XC60'` different from `"Volvo XC60"`?

<details>
<summary>Answer</summary>

- [x] **No.** Single and double quotes work the **same**.

</details>

### Question 3: How do you put an apostrophe in a double-quoted string?

<details>
<summary>Answer</summary>

- [x] Write `"It's alright"` — the inner `'` does not match the outer `"`.
- [x] Or escape: `'It\'s alright.'`

</details>

### Question 4: What can a template store that a quoted string cannot without escapes?

<details>
<summary>Answer</summary>

- [x] **Both** quote kinds, and **multiline** text.

</details>

### Question 5: What does `"ABCDEFGHIJKLMNOPQRSTUVWXYZ".length` return?

<details>
<summary>Answer</summary>

- [x] **26.**
- [x] `length` is a **property**, not a method.

</details>

### Question 6: How do you put double quotes inside a double-quoted string?

<details>
<summary>Answer</summary>

- [x] Escape them: `\"Vikings\"`.
- [x] The printed text is **We are the so-called "Vikings" from the north.**

</details>

### Question 7: What does `\` do in `'It\'s alright.'`?

<details>
<summary>Answer</summary>

- [x] It inserts a literal **apostrophe**.

</details>

### Question 8: What does `"The character \\ is called backslash."` print?

<details>
<summary>Answer</summary>

- [x] **The character \ is called backslash.**

</details>

### Question 9: Where is a safe place to break a long statement?

<details>
<summary>Answer</summary>

- [x] **After an operator**, such as after `=`.
- [x] The broken line still outputs **Hello Dolly!**

</details>

### Question 10: How do you split a string across two lines without a template?

<details>
<summary>Answer</summary>

- [x] Use **`+`**: `"Hello " + "Dolly!"`.
- [x] The result is still **Hello Dolly!**

</details>

### Question 11: Does a multiline template keep the line breaks?

<details>
<summary>Answer</summary>

- [x] **Yes.** Newlines inside backticks are part of the string.

</details>

### Question 12: What is `typeof new String("John")`?

<details>
<summary>Answer</summary>

- [x] **object.** A literal `"John"` is **string**.

</details>

### Question 13: Is `"John" == new String("John")` true?

<details>
<summary>Answer</summary>

- [x] **true** with `==` (types convert).
- [x] **false** with `===` (different types).

</details>

### Question 14: Are two `new String("John")` objects equal?

<details>
<summary>Answer</summary>

- [x] **No.** `==` and `===` are both **false**.
- [x] Comparing two distinct objects always returns false.

</details>

</details>

## Summary

Strings are quoted text. Single and double quotes match; backticks add mixed quotes and multiline. Escape with `\`. `length` of A-Z is **26**. Break lines after an operator or with `+`. Prefer literals: `new String()` is an object, so `===` against a literal is **false** and two String objects never compare equal.

## References

- [JS Strings (W3Schools)](https://www.w3schools.com/js/js_strings.asp)
- [MDN: String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [MDN: Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
