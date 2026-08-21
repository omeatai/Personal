# HTML Comments

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

HTML **comments** are **not displayed** in the browser. They document the source, hold reminders, and can **hide** content (temporarily, for debugging, or in the middle of a line). Syntax: `<!-- Write your comments here -->`. There is an **exclamation point** in the start tag, not the end tag.

This section has **5** examples:

- [x] **Example 1:** Syntax [View](#html-comments-example-01)
- [x] **Example 2:** Add comments [View](#html-comments-example-02)
- [x] **Example 3:** Hide content [View](#html-comments-example-03)
- [x] **Example 4:** Hide a section [View](#html-comments-example-04)
- [x] **Example 5:** Hide inline [View](#html-comments-example-05)

## Detailed Explanation

- [x] **Hide inline content**
  - Comments can hide a **part of a line**.
  - `This <!-- great text --> is a paragraph.` displays as “This is a paragraph.”

<a id="html-comments-example-01"></a>

### **Example 1: Syntax**

- [x] **Comment syntax**
  - `<!-- Write your comments here -->`
  - `!` is only on the **start** tag.
  - Comments do **not** show in the browser; they document the source.
- [x] **Add comments (notifications and reminders)**
  - Place notes in the HTML: `<!-- This is a comment -->` and `<!-- Remember to add more information here -->`.
  - Only the paragraph is visible.

Sandbox: `code_sandbox/html-comments/index.html`

```html
<!-- Write your comments here -->
```

<img alt="html-comments syntax source" src="../code_sandbox/snaps/html-comments-code.png" />

<img alt="html-comments add source" src="../code_sandbox/snaps/html-comments-01-code.png" />

- [x] **Outcome:** the page demonstrates **Syntax** as shown in the result snap.

<a id="html-comments-example-02"></a>

### **Example 2: Add comments**

- [x] **Add comments (notifications and reminders)**
  - Place notes in the HTML: `<!-- This is a comment -->` and `<!-- Remember to add more information here -->`.
  - Only the paragraph is visible.

Sandbox: `code_sandbox/html-comments/index.html`

```html
<!-- This is a comment -->

<p>This is a paragraph.</p>

<!-- Remember to add more information here -->
```

<img alt="html-comments add source" src="../code_sandbox/snaps/html-comments-01-code.png" />

<img alt="html-comments add result" src="../code_sandbox/snaps/html-comments-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**.

<a id="html-comments-example-03"></a>

### **Example 3: Hide content**

- [x] **Hide content**
  - Comment out markup to hide it **temporarily**.
  - Everything between `<!--` and `-->` is hidden from display.
  - Useful for **debugging**: comment out lines one at a time to find errors.

Sandbox: `code_sandbox/html-comments/hide.html`

```html
<p>This is a paragraph.</p>

<!-- <p>This is another paragraph </p> -->

<p>This is a paragraph too.</p>
```

<img alt="html-comments hide source" src="../code_sandbox/snaps/html-comments-02-code.png" />

<img alt="html-comments hide result" src="../code_sandbox/snaps/html-comments-02-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**, **This is another paragraph**, **--> This is a paragraph too.**.

<a id="html-comments-example-04"></a>

### **Example 4: Hide a section**

- [x] **Hide more than one line**
  - A whole block (paragraph + image) can sit inside one comment.

Sandbox: `code_sandbox/html-comments/hide-block.html`

```html
<p>This is a paragraph.</p>
<!--
<p>Look at this cool image:</p>
<img border="0" src="pic_trulli.jpg" alt="Trulli">
-->
<p>This is a paragraph too.</p>
```

<img alt="html-comments hide-block source" src="../code_sandbox/snaps/html-comments-03-code.png" />

<img alt="html-comments hide-block result" src="../code_sandbox/snaps/html-comments-03-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**, **Look at this cool image:**, **--> This is a paragraph too.**.

<a id="html-comments-example-05"></a>

### **Example 5: Hide inline**

- [x] This example runs the tested markup in `code_sandbox/html-comments/inline.html`.

Sandbox: `code_sandbox/html-comments/inline.html`

```html
<p>
  This
  <!-- great text -->
  is a paragraph.
</p>
```

<img alt="html-comments inline source" src="../code_sandbox/snaps/html-comments-04-code.png" />

<img alt="html-comments inline result" src="../code_sandbox/snaps/html-comments-04-result.png" />

- [x] **Outcome:** the browser shows **This is a paragraph.**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-comments/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Are HTML comments shown in the browser?

<details>
<summary>Answer</summary>

- [x] **No.** They are not displayed.
- [x] They can **document** the HTML source.

</details>

### Question 2: What is the comment syntax, and where is the `!`?

<details>
<summary>Answer</summary>

- [x] `<!-- Write your comments here -->`.
- [x] There is an **exclamation point** in the **start** tag, not the end tag.

</details>

### Question 3: Why add comments besides documentation?

<details>
<summary>Answer</summary>

- [x] **Notifications** and **reminders** in the source.
- [x] **Hide** content temporarily.
- [x] **Debug** by commenting out lines one at a time.

</details>

### Question 4: What is hidden when you wrap markup in `<!--` … `-->`?

<details>
<summary>Answer</summary>

- [x] **Everything** between the start and end of the comment.
- [x] That can be one tag, several lines, or part of a line.

</details>

### Question 5: What does `This <!-- great text --> is a paragraph.` display?

<details>
<summary>Answer</summary>

- [x] **This is a paragraph.**
- [x] The words **great text** are commented out.

</details>

### Question 6: Can you hide an image and a paragraph in one comment?

<details>
<summary>Answer</summary>

- [x] **Yes.** A multi-line comment can wrap several elements.
- [x] The chapter example comments out a paragraph and an `<img>`.

</details>

</details>

## Summary

Comments use `<!-- … -->` (`!` only on the start tag). They do **not** display. Use them for notes, to **hide** markup (one line, a block, or part of a line), and to **debug** by commenting code out.

## References

- [HTML Comments (W3Schools)](https://www.w3schools.com/html/html_comments.asp)
- [Try it Yourself: tryhtml_comment](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_comment)
- [Try it Yourself: tryhtml_comment_hide](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_comment_hide)
- [Try it Yourself: tryhtml_comment_out](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_comment_out)
- [Try it Yourself: tryhtml_comment_inline](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_comment_inline)
- [MDN: Comments](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments)
- [WHATWG: Comments](https://html.spec.whatwg.org/multipage/syntax.html#comments)
