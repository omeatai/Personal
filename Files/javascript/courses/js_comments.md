# JS Comments

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Comments **explain** code and make it **readable**. They can also **prevent execution** when you test alternatives. JavaScript has **single-line** comments (`//`) and **multi-line** comments (`/* ... */`).

This section has **3** examples:

- [x] **Example 1:** Single-line comments (`//`) [View](#js-comments-example-01)
- [x] **Example 2:** Multi-line comments (`/* ... */`) [View](#js-comments-example-02)
- [x] **Example 3:** Using comments to prevent execution [View](#js-comments-example-03)

## Detailed Explanation

- [x] **Comments do two jobs**
  - **Explain** code so it is easier to read.
  - **Prevent execution** of a line or block while you test alternatives.
- [x] Comments are ignored by the engine — they never affect the output, only the readability/behaviour of which lines run.

<a id="js-comments-example-01"></a>

### **Example 1: Single-line comments (`//`)**

- [x] A `//` comment runs from the `//` to the **end of the line**; everything after it on that line is ignored.
- [x] Two placements: **on their own line** before code (`// Change heading:`) or **at the end** of a code line (`let x = 5; // Declare x`).
- [x] Comments do not stop the real statements — the heading/paragraph still change and `x`, `y` are still computed.

Sandbox: `code_sandbox/js-comments/single.html`

```javascript
// Change heading:
document.getElementById("myH").innerHTML = "My First Page";
// Change paragraph:
document.getElementById("myP").innerHTML = "My first paragraph.";

let x = 5; // Declare x, give it the value of 5
let y = x + 2; // Declare y, give it the value of x + 2
```

![js-comments example 1 source](../code_sandbox/snaps/js-comments-01-code.png)

![js-comments example 1 result](../code_sandbox/snaps/js-comments-01-result.png)

- [x] **Outcome:** despite the comments, the heading becomes **My First Page**, the paragraph **My first paragraph.**, and the page prints **x = 5, y = x + 2 = 7**.

<a id="js-comments-example-02"></a>

### **Example 2: Multi-line comments (`/* ... */`)**

- [x] Everything between **`/*`** and **`*/`** is ignored, across as many lines as you like — a **comment block**.
- [x] Block comments are handy for a few lines of explanation or **formal documentation**; single-line `//` comments are the more common day-to-day style.
- [x] The two real statements after the block still run.

Sandbox: `code_sandbox/js-comments/multi.html`

```javascript
/*
The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
*/
document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
```

![js-comments example 2 source](../code_sandbox/snaps/js-comments-02-code.png)

![js-comments example 2 result](../code_sandbox/snaps/js-comments-02-result.png)

- [x] **Outcome:** the block is ignored and both statements run, so the page shows **My First Page** and **My first paragraph.** — identical to Example 1's heading/paragraph.

<a id="js-comments-example-03"></a>

### **Example 3: Using comments to prevent execution**

- [x] Adding `//` in front of a statement turns it into a comment, so it **does not run** — great for temporarily disabling code while testing.
- [x] Here the heading-change line is commented out, so the `<h1>` keeps its original text **Heading**, while the paragraph line still runs.
- [x] A `/* ... */` block can disable **several** lines at once.

Sandbox: `code_sandbox/js-comments/prevent.html`

```javascript
//document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
```

![js-comments example 3 source](../code_sandbox/snaps/js-comments-03-code.png)

![js-comments example 3 result](../code_sandbox/snaps/js-comments-03-result.png)

- [x] **Outcome:** the heading stays **Heading** (its change was commented out) while the paragraph becomes **My first paragraph.** — proof the commented line never executed.
- [x] **Page exercise —** _Correct comment syntax?_ → **`// this is a comment`** (not `#`, `''`, or `##`).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-comments/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are JavaScript comments for?

<details>
<summary>Answer</summary>

- [x] To **explain** code and make it **readable**.
- [x] To **prevent execution** when testing alternative code.

</details>

### Question 2: How do you write a single-line comment?

<details>
<summary>Answer</summary>

- [x] Start with **`//`**.
- [x] The rest of that line is ignored.

</details>

### Question 3: How do you write a multi-line comment?

<details>
<summary>Answer</summary>

- [x] Start with **`/*`** and end with **`*/`**.

</details>

### Question 4: Which comment style is most common?

<details>
<summary>Answer</summary>

- [x] **Single-line** comments.
- [x] Block comments are often used for **formal documentation**.

</details>

### Question 5: How do you use comments to prevent execution?

<details>
<summary>Answer</summary>

- [x] Put **`//`** in front of a line.
- [x] Wrap **multiple lines** in `/* ... */`.

</details>

</details>

## Summary

Use **`//`** for single-line comments and **`/* ... */`** for blocks. Comments explain code or **disable** it for testing. Single-line comments are most common; blocks are typical for **documentation**.

## References

- [JS Comments (W3Schools)](https://www.w3schools.com/js/js_comments.asp)
- [MDN: Comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)
