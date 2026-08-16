# HTML Tutorial

Section-by-section notes. Each accordion is one tutorial page: explained, coded in `code_sandbox`, run in the browser, and snapped.

<details>
  <summary>HTML Introduction</summary>

## Introduction

HTML is the **standard markup language** for creating Web pages. This section defines what HTML is, walks through a **simple HTML document**, explains **elements** (including empty ones like `<br>`), shows how **browsers** use tags without displaying them, outlines **page structure** (`<html>`, `<head>`, `<body>`), and sketches **HTML history** up to HTML5. This tutorial follows the **latest HTML5 standard**.

## Detailed Explanation

- [x] **What is HTML?**
  - **H**yper **T**ext **M**arkup **L**anguage.
  - The **standard markup language** for creating Web pages.
  - Describes the **structure** of a Web page.
  - Consists of a **series of elements**.
  - Elements tell the **browser how to display** the content.
  - Elements **label** pieces of content: heading, paragraph, link, and so on.
- [x] **A simple HTML document**
  - The page example is a full HTML5 file: doctype, `html`, `head`/`title`, and `body` with one heading and one paragraph.
  - Sandbox file: `code_sandbox/html-introduction/index.html`.
  - Running it in the browser shows **My First Heading** and **My first paragraph.** The tab title is **Page Title**.

<img alt="html-introduction result" src="./code_sandbox/snaps/html-introduction-result.png" />

- [x] **Example explained**
  - `<!DOCTYPE html>` declares an **HTML5** document.
  - `<html>` is the **root** element of the page.
  - `<head>` holds **meta information** about the page.
  - `<title>` sets the title in the **browser tab / title bar**.
  - `<body>` is the container for **all visible content** (headings, paragraphs, images, links, tables, lists, and so on).
  - `<h1>` defines a **large heading**.
  - `<p>` defines a **paragraph**.
- [x] **What is an HTML element?**
  - An element is a **start tag**, **content**, and an **end tag**: `<tagname> Content goes here... </tagname>`.
  - The element is **everything** from the start tag through the end tag.
  - Examples: `<h1>My First Heading</h1>` and `<p>My first paragraph.</p>`.
- [x] **Start tag, content, end tag**

| Start tag | Element content     | End tag |
| --------- | ------------------- | ------- |
| `<h1>`    | My First Heading    | `</h1>` |
| `<p>`     | My first paragraph. | `</p>`  |
| `<br>`    | none                | none    |

- [x] **Empty elements**
  - Some elements have **no content** (for example `<br>`).
  - These are **empty elements**.
  - Empty elements **do not have an end tag**.
- [x] **Web browsers**
  - Chrome, Edge, Firefox, Safari **read HTML documents** and **display them correctly**.
  - A browser **does not show the tags**; it uses them to decide **how** to display the document.
- [x] **HTML page structure**
  - Typical nesting: `<html>` → `<head>` (`<title>`) and `<body>` (headings and paragraphs).
  - Content inside **`<body>`** is what you **see in the page**.
  - Content inside **`<title>`** is what you **see in the tab / title bar**.
- [x] **HTML history (high level)**
  - **1989:** Tim Berners-Lee invented **www**.
  - **1991:** Tim Berners-Lee invented **HTML**.
  - Later versions include HTML 2.0, 3.2, 4.01, XHTML 1.0, then **HTML5**.
  - **2012:** WHATWG **HTML5 Living Standard**.
  - **2014:** W3C Recommendation: **HTML5**.
  - This tutorial follows the **latest HTML5 standard**.

<details>
  <summary>Lab</summary>

## Lab

Recreate the W3Schools **HTML Introduction** example locally, serve it, and confirm the heading, paragraph, and tab title.

### **Overview**

- [ ] Build `code_sandbox/html-introduction/index.html` from the section example.
- [ ] You will:
  - [ ] Write the HTML5 doctype, `html`, `head`/`title`, and `body` with `<h1>` and `<p>`.
  - [ ] Serve `code_sandbox` over HTTP (Cursor browser blocks `file://`).
  - [ ] Open `http://127.0.0.1:8766/html-introduction/`.
  - [ ] Confirm the tab title is **Page Title**, the heading is **My First Heading**, and the paragraph is **My first paragraph.**
- [ ] Success: the running page matches the snapped result below.

### **Task 1: Create the sandbox file**

- [ ] Open `Personal/Files/html/code_sandbox/html-introduction/index.html`.
- [ ] Use this document (same as the W3Schools example):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
  </body>
</html>
```

### **Task 2: Serve and open the page**

- [ ] From `Personal/Files/html/code_sandbox`, start a static server:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] In the browser, open `http://127.0.0.1:8766/html-introduction/`.
- [ ] Check:
  - [ ] Tab / title: **Page Title**
  - [ ] Large heading: **My First Heading**
  - [ ] Paragraph: **My first paragraph.**
  - [ ] You should **not** see the tags `<h1>` or `<p>` on the page.

<img alt="html-introduction result" src="./code_sandbox/snaps/html-introduction-result.png" />

The sandbox example is running and matches the Introduction document.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Serve the sandbox so the Cursor browser can load the example (it cannot open `file://`).

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-introduction/`.

</details>

<details>
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-introduction/index.html`

Tested source (W3Schools **A Simple HTML Document**):

<img alt="html-introduction source" src="./code_sandbox/snaps/html-introduction-code.png" />

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
  </body>
</html>
```

Rendered result (browser uses the tags; it does not print them):

<img alt="html-introduction result" src="./code_sandbox/snaps/html-introduction-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does HTML stand for?

<details>
<summary>Answer</summary>

- [x] **Hyper Text Markup Language**.

</details>

### Question 2: What is HTML used for?

<details>
<summary>Answer</summary>

- [x] It is the **standard markup language** for creating **Web pages**.
- [x] It describes the **structure** of a page using **elements**.

</details>

### Question 3: What do HTML elements do?

<details>
<summary>Answer</summary>

- [x] They tell the **browser how to display** the content.
- [x] They **label** pieces of content (heading, paragraph, link, and so on).

</details>

### Question 4: What does `<!DOCTYPE html>` mean?

<details>
<summary>Answer</summary>

- [x] It declares that the document is an **HTML5** document.

</details>

### Question 5: What is the `<html>` element?

<details>
<summary>Answer</summary>

- [x] It is the **root** element of an HTML page.

</details>

### Question 6: What belongs in `<head>` vs `<body>`?

<details>
<summary>Answer</summary>

- [x] `<head>` contains **meta information** about the page.
- [x] `<body>` contains **all visible contents** (headings, paragraphs, images, links, tables, lists, and so on).

</details>

### Question 7: What does the `<title>` element control?

<details>
<summary>Answer</summary>

- [x] The title shown in the **browser title bar** or the **page tab**.
- [x] In this example it is **Page Title**.

</details>

### Question 8: What do `<h1>` and `<p>` define in the example?

<details>
<summary>Answer</summary>

- [x] `<h1>` defines a **large heading** (**My First Heading**).
- [x] `<p>` defines a **paragraph** (**My first paragraph.**).

</details>

### Question 9: How is an HTML element defined?

<details>
<summary>Answer</summary>

- [x] A **start tag**, some **content**, and an **end tag**.
- [x] Pattern: `<tagname> Content goes here... </tagname>`.
- [x] The element is **everything** from the start tag to the end tag.

</details>

### Question 10: What is an empty HTML element?

<details>
<summary>Answer</summary>

- [x] An element with **no content**, such as `<br>`.
- [x] Empty elements **do not have an end tag**.

</details>

### Question 11: What is the purpose of a web browser?

<details>
<summary>Answer</summary>

- [x] To **read HTML documents** and **display them correctly**.
- [x] Examples: Chrome, Edge, Firefox, Safari.

</details>

### Question 12: Does the browser show HTML tags on the page?

<details>
<summary>Answer</summary>

- [x] **No.** It does **not** display the tags.
- [x] It **uses** the tags to decide **how** to display the document.

</details>

### Question 13: What appears in the page vs in the tab?

<details>
<summary>Answer</summary>

- [x] **`<body>`** content is displayed **in the browser page**.
- [x] **`<title>`** content is shown in the **title bar / tab**.

</details>

### Question 14: Who invented the www and HTML, and in which years?

<details>
<summary>Answer</summary>

- [x] **Tim Berners-Lee** invented **www** in **1989**.
- [x] **Tim Berners-Lee** invented **HTML** in **1991**.

</details>

### Question 15: Which HTML standard does this tutorial follow?

<details>
<summary>Answer</summary>

- [x] The **latest HTML5** standard.
- [x] HTML5 became a W3C Recommendation in **2014**.
- [x] WHATWG maintains an **HTML5 Living Standard** (from **2012**).

</details>

### Question 16: In the element table, why does `<br>` show “none” for content and end tag?

<details>
<summary>Answer</summary>

- [x] `<br>` is an **empty element**.
- [x] It has **no content** and **no end tag**.

</details>

</details>

## Summary

HTML is **Hyper Text Markup Language**: elements describe page **structure** and tell the browser **how to display** content. A minimal HTML5 page uses `<!DOCTYPE html>`, a root `<html>`, `<head>` with `<title>` (tab text), and `<body>` for what you **see**. An element is start tag + content + end tag, except **empty** elements like `<br>`, which have **no end tag**. Browsers **hide tags** and render the result. This tutorial uses **HTML5**.

## References

- [HTML Introduction (W3Schools)](https://www.w3schools.com/html/html_intro.asp)
- [Try it Yourself: tryhtml_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro)
- [WHATWG HTML Living Standard](https://whatwg.org/html/)
- [W3C HTML5 Recommendation](https://www.w3.org/TR/html5/)
- [W3C HTML5.1 2nd Edition](https://www.w3.org/TR/html51/)
- [W3C HTML5.2 Recommendation](https://www.w3.org/TR/html52/)

</details>

<details>
  <summary>HTML Editors</summary>

## Introduction

You do not need a professional IDE to learn HTML. A **simple text editor**—**Notepad** on Windows or **TextEdit** on Mac—is enough to write a page, save it as **`.htm` / `.html`** with **UTF-8** encoding, and open it in a browser. This section walks through that workflow and also points to W3Schools’ **online editor** (“Try it Yourself”) for fast tests.

## Detailed Explanation

- [x] **A simple text editor is enough**
  - Web pages _can_ be built with professional HTML editors.
  - For **learning**, the tutorial recommends **Notepad** (PC) or **TextEdit** (Mac).
  - Writing tags by hand in a plain editor is a good way to learn HTML.
- [x] **Step 1 (PC): Open Notepad**
  - **Windows 8 or later:** open the **Start** screen (Windows logo, bottom left) and type **Notepad**.
  - **Windows 7 or earlier:** **Start** → **Programs** → **Accessories** → **Notepad**.
- [x] **Step 1 (Mac): Open TextEdit and set it to plain HTML**
  - **Finder** → **Applications** → **TextEdit**.
  - **Preferences** → **Format** → choose **Plain Text** so files save correctly.
  - Under **Open and Save**, check **Display HTML files as HTML code instead of formatted text**.
  - Then open a **new document** for the code.
- [x] **Step 2: Write some HTML**
  - Copy this document into the editor (sandbox: `code_sandbox/html-editors/index.html`).

<img alt="html-editors source" src="./code_sandbox/snaps/html-editors-code.png" />

- [x] **Step 3: Save the HTML page**
  - **File** → **Save as**.
  - Name it **`index.htm`** (or **`index.html`**—the extensions are equivalent).
  - Set encoding to **UTF-8** (preferred for HTML files).
- [x] **Step 4: View it in a browser**
  - Double-click the file, or right-click → **Open with** your browser.
  - The browser shows **My First Heading** and **My first paragraph.** (it does not print the tags).

<img alt="html-editors result" src="./code_sandbox/snaps/html-editors-result.png" />

- [x] **W3Schools online editor (“Try it Yourself”)**
  - Edit HTML and see the result in the browser.
  - Useful for **fast tests**; it has **color coding** and can **save / share** code.
  - That example uses a `<title>` (**Page Title**), heading **This is a Heading**, and paragraph **This is a paragraph.** Sandbox: `code_sandbox/html-editors/tryit.html`.

<img alt="html-editors tryit result" src="./code_sandbox/snaps/html-editors-01-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Write the Notepad example locally, serve it (Cursor blocks `file://`), and confirm the heading and paragraph. Optionally open the Try it Yourself copy.

### **Overview**

- [ ] Recreate both section examples in `code_sandbox/html-editors/` and open them in the browser.
- [ ] You will:
  - [ ] Save the Notepad document as `index.html`.
  - [ ] Save the online-editor document as `tryit.html`.
  - [ ] Serve `code_sandbox` over HTTP.
  - [ ] Confirm **My First Heading** / **My first paragraph.** on `index.html`.
  - [ ] Confirm tab **Page Title**, **This is a Heading**, and **This is a paragraph.** on `tryit.html`.
- [ ] Success: both pages match the snapped results.

### **Task 1: Create the Notepad example**

- [ ] Open `Personal/Files/html/code_sandbox/html-editors/index.html`.
- [ ] Use this document (same as the W3Schools Notepad step):

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>My First Heading</h1>

    <p>My first paragraph.</p>
  </body>
</html>
```

### **Task 2: Create the Try it Yourself example**

- [ ] Open `Personal/Files/html/code_sandbox/html-editors/tryit.html`.
- [ ] Use this document:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

### **Task 3: Serve and open the pages**

- [ ] From `Personal/Files/html/code_sandbox`, start a static server:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] Open `http://127.0.0.1:8766/html-editors/`.
- [ ] Check: **My First Heading** and **My first paragraph.**

<img alt="html-editors result" src="./code_sandbox/snaps/html-editors-result.png" />

- [ ] Open `http://127.0.0.1:8766/html-editors/tryit.html`.
- [ ] Check: tab **Page Title**, heading **This is a Heading**, paragraph **This is a paragraph.**

<img alt="html-editors tryit result" src="./code_sandbox/snaps/html-editors-01-result.png" />

Both editor examples are running and match the section.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Serve the sandbox so the Cursor browser can load the examples (it cannot open `file://`).

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-editors/` and `http://127.0.0.1:8766/html-editors/tryit.html`.

</details>

<details>
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-editors/index.html` (Notepad / save-as `index.htm` example)

<img alt="html-editors source" src="./code_sandbox/snaps/html-editors-code.png" />

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>My First Heading</h1>

    <p>My first paragraph.</p>
  </body>
</html>
```

<img alt="html-editors result" src="./code_sandbox/snaps/html-editors-result.png" />

Sandbox: `code_sandbox/html-editors/tryit.html` (online editor example)

<img alt="html-editors tryit source" src="./code_sandbox/snaps/html-editors-01-code.png" />

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

<img alt="html-editors tryit result" src="./code_sandbox/snaps/html-editors-01-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do you need a professional HTML editor to learn HTML?

<details>
<summary>Answer</summary>

- [x] **No.** A **simple text editor** is enough.
- [x] The tutorial recommends **Notepad** (PC) or **TextEdit** (Mac).

</details>

### Question 2: How do you open Notepad on Windows 8 or later?

<details>
<summary>Answer</summary>

- [x] Open the **Start** screen (Windows logo, bottom left).
- [x] Type **Notepad**.

</details>

### Question 3: What TextEdit settings are required on Mac?

<details>
<summary>Answer</summary>

- [x] **Preferences** → **Format** → **Plain Text**.
- [x] Under **Open and Save**, check **Display HTML files as HTML code instead of formatted text**.

</details>

### Question 4: What filename and encoding should you use when saving?

<details>
<summary>Answer</summary>

- [x] Name the file **`index.htm`** (or **`index.html`**).
- [x] Set encoding to **UTF-8**.

</details>

### Question 5: Is there a difference between `.htm` and `.html`?

<details>
<summary>Answer</summary>

- [x] **No.** Either extension works.
- [x] The choice is up to you.

</details>

### Question 6: How do you view the saved HTML page?

<details>
<summary>Answer</summary>

- [x] Open the file in a **browser**.
- [x] Double-click it, or right-click and choose **Open with**.

</details>

### Question 7: What does the Notepad example display in the browser?

<details>
<summary>Answer</summary>

- [x] A heading: **My First Heading**.
- [x] A paragraph: **My first paragraph.**

</details>

### Question 8: What is the W3Schools “Try it Yourself” editor for?

<details>
<summary>Answer</summary>

- [x] Edit HTML and **view the result** in the browser.
- [x] It is useful for **testing code fast**.
- [x] It has **color coding** and can **save and share** code.

</details>

### Question 9: What extra markup does the Try it Yourself example add compared with the Notepad snippet?

<details>
<summary>Answer</summary>

- [x] A `<head>` with `<title>Page Title</title>`.
- [x] Different body text: **This is a Heading** and **This is a paragraph.**

</details>

### Question 10: Why is UTF-8 mentioned when saving?

<details>
<summary>Answer</summary>

- [x] **UTF-8** is the **preferred encoding** for HTML files.

</details>

</details>

## Summary

Learn HTML in a **plain text editor** (Notepad or TextEdit). Write a basic document, save it as **`index.htm` / `.html`** with **UTF-8**, and open it in a browser. **`.htm` and `.html` are the same.** On Mac, TextEdit must use **Plain Text** and must show HTML as **code**. The **Try it Yourself** online editor is for quick tests with color coding. The Notepad sample renders **My First Heading**; the online sample adds a **Page Title** tab and **This is a Heading**.

## References

- [HTML Editors (W3Schools)](https://www.w3schools.com/html/html_editors.asp)
- [Try it Yourself: tryhtml_editors](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_editors)

</details>

<details>
  <summary>HTML Basic</summary>

## Introduction

This chapter shows **basic HTML examples**: a full document, the `<!DOCTYPE html>` declaration, **headings**, **paragraphs**, **links**, and **images**. The tags may be new; the point is to see the pattern. You can also **view page source** and **inspect** elements in the browser.

## Detailed Explanation

- [x] **HTML documents**
  - Every document starts with a document type declaration: `<!DOCTYPE html>`.
  - The document itself starts with `<html>` and ends with `</html>`.
  - Visible content sits between `<body>` and `</body>`.
  - Sandbox: `code_sandbox/html-basic/index.html`.

<img alt="html-basic document result" src="./code_sandbox/snaps/html-basic-result.png" />

- [x] **The `<!DOCTYPE>` declaration**
  - Represents the **document type** and helps browsers **display pages correctly**.
  - Must appear **once**, at the **top** of the page (before any HTML tags).
  - It is **not case sensitive**.
  - HTML5 doctype is: `<!DOCTYPE html>`.
- [x] **HTML headings**
  - Defined with `<h1>` through `<h6>`.
  - `<h1>` is the **most important**; `<h6>` is the **least important**.
  - Sandbox: `code_sandbox/html-basic/headings.html`.

<img alt="html-basic headings result" src="./code_sandbox/snaps/html-basic-01-result.png" />

- [x] **HTML paragraphs**
  - Defined with the `<p>` tag.
  - Sandbox: `code_sandbox/html-basic/paragraphs.html`.

<img alt="html-basic paragraphs result" src="./code_sandbox/snaps/html-basic-02-result.png" />

- [x] **HTML links**
  - Defined with the `<a>` tag.
  - The destination is the **`href` attribute**.
  - Attributes add extra information about an element (covered in a later chapter).
  - Sandbox: `code_sandbox/html-basic/link.html`.

<img alt="html-basic link result" src="./code_sandbox/snaps/html-basic-03-result.png" />

- [x] **HTML images**
  - Defined with the `<img>` tag.
  - Attributes: **`src`** (file), **`alt`** (alternative text), **`width`**, **`height`**.
  - Sandbox: `code_sandbox/html-basic/img.html` (local `w3schools.jpg`, 104×142).

<img alt="html-basic image result" src="./code_sandbox/snaps/html-basic-04-result.png" />

- [x] **How to view HTML source**
  - **View Page Source:** `Ctrl`+`U`, or right-click the page → **View Page Source**. Opens a tab with the HTML source.
  - **Inspect an element:** right-click an element (or a blank area) → **Inspect**. Shows HTML and CSS; you can edit them on the fly in the Elements / Styles panel.

<details>
  <summary>Lab</summary>

## Lab

Run each Basic example from `code_sandbox/html-basic/` and match the snaps.

### **Overview**

- [ ] Recreate the document, headings, paragraphs, link, and image examples.
- [ ] You will:
  - [ ] Serve `code_sandbox` over HTTP.
  - [ ] Open each sandbox file and confirm the output.
- [ ] Success: the five pages match the snapped results.

### **Task 1: Serve the sandbox**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

### **Task 2: Open each example**

- [ ] Document: `http://127.0.0.1:8766/html-basic/` — **My First Heading** / **My first paragraph.**
- [ ] Headings: `http://127.0.0.1:8766/html-basic/headings.html` — heading 1, 2, and 3.
- [ ] Paragraphs: `http://127.0.0.1:8766/html-basic/paragraphs.html` — two paragraphs.
- [ ] Link: `http://127.0.0.1:8766/html-basic/link.html` — blue underlined **This is a link**.
- [ ] Image: `http://127.0.0.1:8766/html-basic/img.html` — W3Schools logo at 104×142 with alt **W3Schools.com**.

<img alt="html-basic document result" src="./code_sandbox/snaps/html-basic-result.png" />

The Basic examples are running and match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-basic/` and the other files in that folder.

</details>

<details>
  <summary>Code</summary>

## Code

Sandbox: `code_sandbox/html-basic/index.html`

<img alt="html-basic document source" src="./code_sandbox/snaps/html-basic-code.png" />

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
  </body>
</html>
```

<img alt="html-basic document result" src="./code_sandbox/snaps/html-basic-result.png" />

Headings (`headings.html`):

<img alt="html-basic headings source" src="./code_sandbox/snaps/html-basic-01-code.png" />

```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
```

<img alt="html-basic headings result" src="./code_sandbox/snaps/html-basic-01-result.png" />

Paragraphs (`paragraphs.html`):

<img alt="html-basic paragraphs source" src="./code_sandbox/snaps/html-basic-02-code.png" />

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

<img alt="html-basic paragraphs result" src="./code_sandbox/snaps/html-basic-02-result.png" />

Link (`link.html`):

<img alt="html-basic link source" src="./code_sandbox/snaps/html-basic-03-code.png" />

```html
<a href="https://www.w3schools.com">This is a link</a>
```

<img alt="html-basic link result" src="./code_sandbox/snaps/html-basic-03-result.png" />

Image (`img.html`):

<img alt="html-basic image source" src="./code_sandbox/snaps/html-basic-04-code.png" />

```html
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142" />
```

<img alt="html-basic image result" src="./code_sandbox/snaps/html-basic-04-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What must every HTML document start with?

<details>
<summary>Answer</summary>

- [x] A document type declaration: `<!DOCTYPE html>`.

</details>

### Question 2: Where does visible content go?

<details>
<summary>Answer</summary>

- [x] Between `<body>` and `</body>`.

</details>

### Question 3: How many times may `<!DOCTYPE>` appear, and where?

<details>
<summary>Answer</summary>

- [x] **Once**.
- [x] At the **top** of the page, **before any HTML tags**.

</details>

### Question 4: Is `<!DOCTYPE>` case sensitive?

<details>
<summary>Answer</summary>

- [x] **No.**

</details>

### Question 5: Which tags define headings, and which is most important?

<details>
<summary>Answer</summary>

- [x] `<h1>` through `<h6>`.
- [x] `<h1>` is the **most important**; `<h6>` is the **least important**.

</details>

### Question 6: Which tag defines a paragraph?

<details>
<summary>Answer</summary>

- [x] `<p>`.

</details>

### Question 7: How do you write a link, and where is the URL?

<details>
<summary>Answer</summary>

- [x] Use the `<a>` tag.
- [x] Put the destination in the **`href` attribute**.

</details>

### Question 8: Which attributes does the image example use?

<details>
<summary>Answer</summary>

- [x] **`src`** — the image file.
- [x] **`alt`** — alternative text.
- [x] **`width`** and **`height`**.

</details>

### Question 9: How do you view a page’s HTML source?

<details>
<summary>Answer</summary>

- [x] Press **`Ctrl`+`U`**, or right-click → **View Page Source**.
- [x] That opens a tab with the HTML source.

</details>

### Question 10: What does Inspect show you?

<details>
<summary>Answer</summary>

- [x] Right-click an element → **Inspect**.
- [x] You see the **HTML and CSS**.
- [x] You can edit them **on the fly** in Elements / Styles.

</details>

</details>

## Summary

A page starts with `<!DOCTYPE html>`, then `<html>` / `<body>`. Headings are `<h1>`–`<h6>`, paragraphs `<p>`, links `<a href="...">`, images `<img src alt width height>`. The doctype appears **once at the top** and is **not case sensitive**. Use **View Source** (`Ctrl`+`U`) or **Inspect** to study a page.

## References

- [HTML Basic (W3Schools)](https://www.w3schools.com/html/html_basic.asp)
- [Try it Yourself: tryhtml_basic_document](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_document)
- [Try it Yourself: tryhtml_basic_headings](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_headings)
- [Try it Yourself: tryhtml_basic_paragraphs](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_paragraphs)
- [Try it Yourself: tryhtml_basic_link](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_link)
- [Try it Yourself: tryhtml_basic_img](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_img)
- [MDN: DOCTYPE](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)
- [MDN: `<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
- [MDN: `<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)

</details>

<details>
  <summary>HTML Elements</summary>

## Introduction

An HTML **element** is a **start tag**, **content**, and an **end tag**. Elements can be **nested**. Some elements are **empty** (no content, no end tag), such as `<br>`. Tags are **not case sensitive**, but this tutorial (and W3C) prefers **lowercase**.

## Detailed Explanation

- [x] **What is an HTML element?**
  - Start tag + content + end tag: `<tagname> Content goes here... </tagname>`.
  - The element is **everything** from the start tag through the end tag.

| Start tag | Element content     | End tag |
| --------- | ------------------- | ------- |
| `<h1>`    | My First Heading    | `</h1>` |
| `<p>`     | My first paragraph. | `</p>`  |
| `<br>`    | none                | none    |

- [x] **Empty elements**
  - No content (example: `<br>`).
  - **No end tag**.
- [x] **Nested HTML elements**
  - Elements can contain other elements.
  - A whole document is nested: `<html>` → `<body>` → `<h1>` and `<p>`.
  - `<html>` is the **root** (whole document). `<body>` is the **visible body**. `<h1>` is a heading. `<p>` is a paragraph.
  - Sandbox: `code_sandbox/html-elements/index.html`.

<img alt="html-elements nested result" src="./code_sandbox/snaps/html-elements-result.png" />

- [x] **Never skip the end tag**
  - Some elements still **display** if you omit `</p>`.
  - **Do not rely on that.** Missing end tags can cause unexpected results and errors.
  - WHATWG HTML does allow **optional end tags** for a few elements (including `<p>` in some contexts). The tutorial’s advice still stands for learning: **write the end tag**.
  - Sandbox: `code_sandbox/html-elements/no-endtag.html` (two paragraphs, no `</p>` — the browser still shows two blocks).

<img alt="html-elements omitted end tags result" src="./code_sandbox/snaps/html-elements-01-result.png" />

- [x] **Empty HTML elements (`<br>`)**
  - `<br>` is a **line break** with no closing tag.
  - Sandbox: `code_sandbox/html-elements/br.html`.

<img alt="html-elements br result" src="./code_sandbox/snaps/html-elements-02-result.png" />

- [x] **HTML is not case sensitive**
  - `<P>` means the same as `<p>`.
  - The HTML standard does not require lowercase, but **W3C recommends lowercase**, and **XHTML requires it**.
  - W3Schools always uses **lowercase** tag names.

<details>
  <summary>Lab</summary>

## Lab

Run the nested document, the omitted-end-tag demo, and the `<br>` demo.

### **Overview**

- [ ] Recreate the three sandbox files and open them over HTTP.
- [ ] Success: nested page shows heading + paragraph; omitted `</p>` still shows two paragraphs; `<br>` splits one paragraph onto two lines.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] Open `http://127.0.0.1:8766/html-elements/`.
- [ ] Open `http://127.0.0.1:8766/html-elements/no-endtag.html`.
- [ ] Open `http://127.0.0.1:8766/html-elements/br.html`.

<img alt="html-elements nested result" src="./code_sandbox/snaps/html-elements-result.png" />

The three element examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-elements/`.

</details>

<details>
  <summary>Code</summary>

## Code

Nested document: `code_sandbox/html-elements/index.html`

<img alt="html-elements nested source" src="./code_sandbox/snaps/html-elements-code.png" />

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
  </body>
</html>
```

<img alt="html-elements nested result" src="./code_sandbox/snaps/html-elements-result.png" />

Omitted end tags: `code_sandbox/html-elements/no-endtag.html`

<img alt="html-elements omitted end tags source" src="./code_sandbox/snaps/html-elements-01-code.png" />

```html
<html>
  <body>
    <p>This is a paragraph</p>
    <p>This is a paragraph</p>
  </body>
</html>
```

<img alt="html-elements omitted end tags result" src="./code_sandbox/snaps/html-elements-01-result.png" />

Line break: `code_sandbox/html-elements/br.html`

<img alt="html-elements br source" src="./code_sandbox/snaps/html-elements-02-code.png" />

```html
<p>
  This is a <br />
  paragraph with a line break.
</p>
```

<img alt="html-elements br result" src="./code_sandbox/snaps/html-elements-02-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is an HTML element?

<details>
<summary>Answer</summary>

- [x] A **start tag**, some **content**, and an **end tag**.
- [x] The element is everything from the start tag to the end tag.

</details>

### Question 2: What is a nested element?

<details>
<summary>Answer</summary>

- [x] An element **inside** another element.
- [x] A whole HTML document is nested (`<html>` contains `<body>`, which contains headings and paragraphs).

</details>

### Question 3: What is the root element?

<details>
<summary>Answer</summary>

- [x] `<html>` — it defines the **whole HTML document**.

</details>

### Question 4: Should you skip end tags if the page still looks OK?

<details>
<summary>Answer</summary>

- [x] **No.** Never rely on omitted end tags.
- [x] You can get **unexpected results and errors**.

</details>

### Question 5: What is an empty HTML element?

<details>
<summary>Answer</summary>

- [x] An element with **no content**.
- [x] Example: `<br>` (line break).
- [x] Empty elements **do not have an end tag**.

</details>

### Question 6: Are HTML tags case sensitive?

<details>
<summary>Answer</summary>

- [x] **No.** `<P>` means the same as `<p>`.
- [x] W3C **recommends lowercase**; XHTML **requires** it.
- [x] W3Schools always uses **lowercase**.

</details>

### Question 7: In the element table, why does `<br>` show “none”?

<details>
<summary>Answer</summary>

- [x] `<br>` is **empty**.
- [x] It has **no content** and **no end tag**.

</details>

### Question 8: What does the WHATWG spec say about omitted `</p>`?

<details>
<summary>Answer</summary>

- [x] Some end tags (including `<p>` in certain cases) are **optional** in the HTML living standard.
- [x] For learning, still **write the end tag**, as the tutorial warns.

</details>

</details>

## Summary

An element is **start tag + content + end tag**, except **empty** elements like `<br>`. Documents are **nested** (`<html>` / `<body>` / headings and paragraphs). Browsers may forgive a missing `</p>`, but **do not skip end tags**. Tags are **case-insensitive**; use **lowercase**.

## References

- [HTML Elements (W3Schools)](https://www.w3schools.com/html/html_elements.asp)
- [Try it Yourself: tryhtml_elements](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elements)
- [Try it Yourself: tryhtml_no_endtag](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_no_endtag)
- [Try it Yourself: tryhtml_elements_br](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elements_br)
- [HTML Tag Reference (W3Schools)](https://www.w3schools.com/tags/default.asp)
- [WHATWG: optional tags](https://html.spec.whatwg.org/multipage/syntax.html#optional-tags)
- [MDN: HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

</details>

<details>
  <summary>HTML Attributes</summary>

## Introduction

HTML **attributes** add extra information about an element. They go in the **start tag**, usually as `name="value"`. This chapter covers **`href`**, **`src`**, **`width`/`height`**, **`alt`**, **`style`**, **`lang`**, and **`title`**, plus quoting and lowercase conventions.

## Detailed Explanation

- [x] **Attribute rules**
  - All HTML elements can have attributes.
  - Attributes provide **additional information** about elements.
  - Always specified in the **start tag**.
  - Usually **name/value** pairs: `name="value"`.
- [x] **The `href` attribute**
  - `<a>` is a hyperlink. **`href`** is the URL it goes to.
  - Sandbox: `code_sandbox/html-attributes/href.html`.

<img alt="html-attributes href result" src="./code_sandbox/snaps/html-attributes-result.png" />

- [x] **The `src` attribute**
  - `<img>` embeds an image. **`src`** is the path.
  - **Absolute URL:** full address, e.g. `https://www.w3schools.com/images/img_girl.jpg`. External images can be copyrighted or disappear.
  - **Relative URL:** no domain. `img_girl.jpg` is relative to the **current page**; `/images/img_girl.jpg` is relative to the **domain**.
  - Prefer **relative** URLs so they do not break if the domain changes.
- [x] **`width` and `height`**
  - Size the image in **pixels**.
  - Example: `width="500"` `height="600"` with `src="img_girl.jpg"`.
  - Sandbox: `code_sandbox/html-attributes/img.html`.

<img alt="html-attributes img size result" src="./code_sandbox/snaps/html-attributes-01-result.png" />

- [x] **The `alt` attribute**
  - **Required** on `<img>`. Alternate text if the image cannot be shown (slow connection, bad `src`, or a screen reader).
  - Broken `src` (`img_typo.jpg`) still shows **Girl with a jacket**.
  - Sandbox: `code_sandbox/html-attributes/alt-error.html`.

<img alt="html-attributes alt fallback result" src="./code_sandbox/snaps/html-attributes-02-result.png" />

- [x] **The `style` attribute**
  - Adds styles (color, font, size, and more).
  - Example: red paragraph.
  - Sandbox: `code_sandbox/html-attributes/style.html`.

<img alt="html-attributes style result" src="./code_sandbox/snaps/html-attributes-03-result.png" />

- [x] **The `lang` attribute**
  - Put **`lang`** on `<html>` to declare the page language (helps search engines and browsers).
  - English: `<html lang="en">`. Country: `<html lang="en-US">` (language + country).
- [x] **The `title` attribute**
  - Extra information about an element.
  - Shown as a **tooltip** on mouse over.
  - Sandbox: `code_sandbox/html-attributes/title.html` (`title="I'm a tooltip"`).

<img alt="html-attributes title result" src="./code_sandbox/snaps/html-attributes-04-result.png" />

- [x] **Lowercase and quotes**
  - The HTML standard does not require lowercase names or quotes, but **W3C recommends** both; **XHTML requires** them.
  - W3Schools always uses **lowercase names** and **quoted values**.
  - Quotes are **required** when the value has a **space** (`title=Description of W3Schools` fails).
  - Double quotes are most common; use single quotes if the value itself contains double quotes (or the reverse).

<details>
  <summary>Lab</summary>

## Lab

Run the href, sized image, broken-image alt, style, and title sandboxes.

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-attributes` example.
- [ ] Success: blue **Visit W3Schools** link; 500×600 photo; alt text **Girl with a jacket** on a missing file; red paragraph; tooltip paragraph.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-attributes/href.html`
- [ ] `http://127.0.0.1:8766/html-attributes/img.html`
- [ ] `http://127.0.0.1:8766/html-attributes/alt-error.html`
- [ ] `http://127.0.0.1:8766/html-attributes/style.html`
- [ ] `http://127.0.0.1:8766/html-attributes/title.html` (hover for the tooltip)

<img alt="html-attributes href result" src="./code_sandbox/snaps/html-attributes-result.png" />

The attribute examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-attributes/href.html`.

</details>

<details>
  <summary>Code</summary>

## Code

`href` (`href.html`):

<img alt="html-attributes href source" src="./code_sandbox/snaps/html-attributes-code.png" />

```html
<a href="https://www.w3schools.com">Visit W3Schools</a>
```

<img alt="html-attributes href result" src="./code_sandbox/snaps/html-attributes-result.png" />

Image size (`img.html`):

<img alt="html-attributes img source" src="./code_sandbox/snaps/html-attributes-01-code.png" />

```html
<img src="img_girl.jpg" alt="Girl with a jacket" width="500" height="600" />
```

<img alt="html-attributes img size result" src="./code_sandbox/snaps/html-attributes-01-result.png" />

Broken image + `alt` (`alt-error.html`):

<img alt="html-attributes alt-error source" src="./code_sandbox/snaps/html-attributes-02-code.png" />

```html
<img src="img_typo.jpg" alt="Girl with a jacket" />
```

<img alt="html-attributes alt fallback result" src="./code_sandbox/snaps/html-attributes-02-result.png" />

`style` (`style.html`):

<img alt="html-attributes style source" src="./code_sandbox/snaps/html-attributes-03-code.png" />

```html
<p style="color:red;">This is a red paragraph.</p>
```

<img alt="html-attributes style result" src="./code_sandbox/snaps/html-attributes-03-result.png" />

`title` (`title.html`):

<img alt="html-attributes title source" src="./code_sandbox/snaps/html-attributes-04-code.png" />

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

<img alt="html-attributes title result" src="./code_sandbox/snaps/html-attributes-04-result.png" />

`lang` on the document (used on these sandbox files):

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    ...
  </body>
</html>
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Where do you put attributes, and in what form?

<details>
<summary>Answer</summary>

- [x] In the **start tag**.
- [x] Usually **name/value** pairs: `name="value"`.

</details>

### Question 2: What does `href` on `<a>` do?

<details>
<summary>Answer</summary>

- [x] It specifies the **URL** of the page the link goes to.

</details>

### Question 3: Absolute vs relative `src` — which is safer for your own images?

<details>
<summary>Answer</summary>

- [x] **Relative** URLs (no domain).
- [x] They do not break if you **change domain**.
- [x] Absolute URLs point at another site and can vanish or be copyrighted.

</details>

### Question 4: Why set `width` and `height` on `<img>`?

<details>
<summary>Answer</summary>

- [x] They specify the image size in **pixels**.

</details>

### Question 5: Why is `alt` required?

<details>
<summary>Answer</summary>

- [x] It is the **alternate text** if the image cannot be displayed.
- [x] Used for slow connections, bad `src`, and **screen readers**.

</details>

### Question 6: What does `lang` on `<html>` do?

<details>
<summary>Answer</summary>

- [x] Declares the **language** of the page.
- [x] Helps **search engines** and **browsers**.
- [x] Example: `lang="en"` or `lang="en-US"`.

</details>

### Question 7: What does `title` show?

<details>
<summary>Answer</summary>

- [x] Extra information as a **tooltip** when you mouse over the element.

</details>

### Question 8: Must attribute names be lowercase and values quoted?

<details>
<summary>Answer</summary>

- [x] HTML does **not require** either.
- [x] **W3C recommends** lowercase and quotes; **XHTML requires** them.
- [x] Quotes are needed when the value contains a **space**.

</details>

### Question 9: When do you use single quotes around an attribute value?

<details>
<summary>Answer</summary>

- [x] When the value itself contains **double quotes**.
- [x] Or use double quotes if the value contains **single quotes**.

</details>

</details>

## Summary

Attributes live in the **start tag** as `name="value"`. **`href`** is the link URL, **`src`** the image path (prefer **relative**), **`width`/`height`** size in pixels, **`alt`** fallback text, **`style`** inline CSS, **`lang`** the page language, **`title`** a tooltip. Use **lowercase names** and **quoted values**.

## References

- [HTML Attributes (W3Schools)](https://www.w3schools.com/html/html_attributes.asp)
- [Try it Yourself: tryhtml_attributes_link](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_link)
- [Try it Yourself: tryhtml_attributes_img](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_img)
- [Try it Yourself: tryhtml_attributes_alt_error](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_alt_error)
- [Try it Yourself: tryhtml_attributes_style](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_style)
- [Try it Yourself: tryhtml_attributes_title](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_attributes_title)
- [HTML Attribute Reference](https://www.w3schools.com/tags/ref_attributes.asp)
- [HTML Language Code Reference](https://www.w3schools.com/tags/ref_language_codes.asp)
- [MDN: HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes)

</details>

<details>
  <summary>HTML Headings</summary>

## Introduction

HTML **headings** are titles and subtitles on a page. They use `<h1>` through `<h6>`: **`<h1>` is most important**, **`<h6>` least**. Search engines and skimmers use them for **structure**. Use headings for **headings**, not just to make text big.

## Detailed Explanation

- [x] **`<h1>` to `<h6>`**
  - Headings are titles or subtitles you want on a webpage.
  - `<h1>` = most important; `<h6>` = least important.
  - Browsers add **margin** (white space) before and after a heading.
  - Sandbox: `code_sandbox/html-headings/index.html`.

<img alt="html-headings h1 to h6 result" src="./code_sandbox/snaps/html-headings-result.png" />

- [x] **Headings are important**
  - Search engines **index** structure and content from headings.
  - Users often **skim** by headings, so headings should show the **document structure**.
  - Use `<h1>` for the **main** heading, then `<h2>`, then less important `<h3>`, and so on.
  - Example outline: **Travel Guide** (`h1`) → **Europe** / **Asia** (`h2`) → countries (`h3`).
  - **Tip:** use **only one `<h1>` per page** — it is the main topic or title.
  - **Note:** use heading tags for headings only. **Do not** use them just to make text BIG or bold.
  - Sandbox: `code_sandbox/html-headings/structure.html`.

<img alt="html-headings structure result" src="./code_sandbox/snaps/html-headings-01-result.png" />

- [x] **Bigger headings**
  - Each heading has a **default size**.
  - You can change size with the **`style`** attribute and CSS **`font-size`**.
  - Example: `<h1 style="font-size:60px;">Heading 1</h1>`.
  - That still **is** a heading (for structure); the style only changes how large it looks.
  - Sandbox: `code_sandbox/html-headings/size.html`.

<img alt="html-headings font-size result" src="./code_sandbox/snaps/html-headings-02-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the six heading levels, the Travel Guide outline, and the 60px `<h1>`.

### **Overview**

- [ ] Serve `code_sandbox` and open the three `html-headings` files.
- [ ] Success: Heading 1–6 shrink in size; Travel Guide nests continents under one `h1`; the sized `h1` is visually larger than the default.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-headings/`
- [ ] `http://127.0.0.1:8766/html-headings/structure.html`
- [ ] `http://127.0.0.1:8766/html-headings/size.html`

<img alt="html-headings h1 to h6 result" src="./code_sandbox/snaps/html-headings-result.png" />

The heading examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-headings/`.

</details>

<details>
  <summary>Code</summary>

## Code

Levels 1–6 (`index.html`):

<img alt="html-headings h1 to h6 source" src="./code_sandbox/snaps/html-headings-code.png" />

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

<img alt="html-headings h1 to h6 result" src="./code_sandbox/snaps/html-headings-result.png" />

Document structure (`structure.html`):

<img alt="html-headings structure source" src="./code_sandbox/snaps/html-headings-01-code.png" />

```html
<h1>Travel Guide</h1>

<h2>Europe</h2>
<h3>France</h3>
<h3>Italy</h3>

<h2>Asia</h2>
<h3>India</h3>
<h3>Thailand</h3>
```

<img alt="html-headings structure result" src="./code_sandbox/snaps/html-headings-01-result.png" />

Custom size (`size.html`):

<img alt="html-headings font-size source" src="./code_sandbox/snaps/html-headings-02-code.png" />

```html
<h1 style="font-size:60px;">Heading 1</h1>
```

<img alt="html-headings font-size result" src="./code_sandbox/snaps/html-headings-02-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which tags define HTML headings?

<details>
<summary>Answer</summary>

- [x] `<h1>` through `<h6>`.
- [x] `<h1>` is the **most important**; `<h6>` is the **least important**.

</details>

### Question 2: Do browsers add space around headings?

<details>
<summary>Answer</summary>

- [x] **Yes.** They add **margin** (white space) before and after a heading.

</details>

### Question 3: Why do search engines care about headings?

<details>
<summary>Answer</summary>

- [x] They use headings to **index** the **structure and content** of the page.

</details>

### Question 4: How should you order heading levels?

<details>
<summary>Answer</summary>

- [x] `<h1>` for the **main** heading.
- [x] Then `<h2>`, then less important `<h3>`, and so on.

</details>

### Question 5: How many `<h1>` elements should a page have, according to this chapter?

<details>
<summary>Answer</summary>

- [x] **Only one** `<h1>` per page.
- [x] It represents the **main topic or title**.

</details>

### Question 6: Should you use heading tags just to make text look big?

<details>
<summary>Answer</summary>

- [x] **No.** Use headings for **headings only**.
- [x] Do not use them just to make text **BIG** or **bold**.

</details>

### Question 7: How do you change a heading’s visual size without changing its level?

<details>
<summary>Answer</summary>

- [x] Use the **`style`** attribute with CSS **`font-size`**.
- [x] Example: `<h1 style="font-size:60px;">Heading 1</h1>`.

</details>

### Question 8: In the Travel Guide example, what is `<h1>` vs `<h2>` vs `<h3>`?

<details>
<summary>Answer</summary>

- [x] `<h1>`: **Travel Guide** (page topic).
- [x] `<h2>`: **Europe** and **Asia** (regions).
- [x] `<h3>`: countries (**France**, **Italy**, **India**, **Thailand**).

</details>

</details>

## Summary

Headings are `<h1>`–`<h6>`: **h1 most important**, **h6 least**. They outline the page for **search engines** and **skimmers**. Use **one `<h1>`**, then `<h2>`, then `<h3>`. Do **not** fake size with heading tags; if you need a larger look, keep the heading and set **`font-size`** with **`style`**. Browsers add **margin** around headings.

## References

- [HTML Headings (W3Schools)](https://www.w3schools.com/html/html_headings.asp)
- [Try it Yourself: tryhtml_headings](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_headings)
- [Try it Yourself: tryhtml_headings_structure](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_headings_structure)
- [Try it Yourself: tryhtml_headings_size](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_headings_size)
- [HTML headings tag reference](https://www.w3schools.com/tags/tag_hn.asp)
- [MDN: Heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)

</details>

<details>
  <summary>HTML Paragraphs</summary>

## Introduction

A **paragraph** (`<p>`) is a block of text that **starts on a new line**. Browsers add **margin** around it. Extra spaces and line breaks in the source **collapse**. Use `<hr>` for a thematic break, `<br>` for a line break inside a paragraph, and `<pre>` when you must keep the source layout (poems, code).

## Detailed Explanation

- [x] **HTML paragraphs**
  - `<p>` defines a paragraph.
  - A paragraph always starts on a **new line**.
  - Browsers add **white space (margin)** before and after it.
  - Sandbox: `code_sandbox/html-paragraphs/index.html`.

<img alt="html-paragraphs result" src="./code_sandbox/snaps/html-paragraphs-result.png" />

- [x] **HTML display (whitespace)**
  - You cannot be sure how HTML will look: screen size and window size change the wrap.
  - Extra **spaces** or **lines** in the source do **not** change the display.
  - The browser **removes extra spaces and lines**; many spaces or newlines count as **one space**.
  - Sandbox: `code_sandbox/html-paragraphs/display.html`.

<img alt="html-paragraphs whitespace result" src="./code_sandbox/snaps/html-paragraphs-01-result.png" />

- [x] **HTML horizontal rules**
  - `<hr>` is a **thematic break**, usually shown as a horizontal line.
  - Use it to **separate** content or mark a change.
  - `<hr>` is **empty** (no end tag).
  - Sandbox: `code_sandbox/html-paragraphs/hr.html`.

<img alt="html-paragraphs hr result" src="./code_sandbox/snaps/html-paragraphs-02-result.png" />

- [x] **HTML line breaks**
  - `<br>` starts a **new line** without a new paragraph.
  - `<br>` is **empty** (no end tag).
  - Sandbox: `code_sandbox/html-paragraphs/br.html`.

<img alt="html-paragraphs br result" src="./code_sandbox/snaps/html-paragraphs-03-result.png" />

- [x] **The poem problem**
  - A poem in `<p>` with blank lines in the source still **renders on one flow** (one paragraph).
  - Sandbox: `code_sandbox/html-paragraphs/poem.html`.

<img alt="html-paragraphs poem-in-p result" src="./code_sandbox/snaps/html-paragraphs-04-result.png" />

- [x] **Solution: `<pre>`**
  - `<pre>` is **preformatted** text: spaces and line breaks in the source are **kept**.
  - Browsers typically show it in a **monospace** font.
  - Sandbox: `code_sandbox/html-paragraphs/pre.html`.

<img alt="html-paragraphs pre result" src="./code_sandbox/snaps/html-paragraphs-05-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the six paragraph examples: two `<p>`s, collapsed whitespace, `<hr>`, `<br>`, poem in `<p>`, poem in `<pre>`.

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-paragraphs` file.
- [ ] Success: two spaced paragraphs; extra source spaces collapsed; two `hr` lines; three-line `<br>` paragraph; poem as one flow in `<p>`; poem layout kept in `<pre>`.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-paragraphs/`
- [ ] `http://127.0.0.1:8766/html-paragraphs/display.html`
- [ ] `http://127.0.0.1:8766/html-paragraphs/hr.html`
- [ ] `http://127.0.0.1:8766/html-paragraphs/br.html`
- [ ] `http://127.0.0.1:8766/html-paragraphs/poem.html`
- [ ] `http://127.0.0.1:8766/html-paragraphs/pre.html`

<img alt="html-paragraphs result" src="./code_sandbox/snaps/html-paragraphs-result.png" />

The paragraph examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-paragraphs/`.

</details>

<details>
  <summary>Code</summary>

## Code

Two paragraphs (`index.html`):

<img alt="html-paragraphs source" src="./code_sandbox/snaps/html-paragraphs-code.png" />

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

<img alt="html-paragraphs result" src="./code_sandbox/snaps/html-paragraphs-result.png" />

Collapsed whitespace (`display.html`):

<img alt="html-paragraphs whitespace source" src="./code_sandbox/snaps/html-paragraphs-01-code.png" />

```html
<p>
  This paragraph contains a lot of lines in the source code, but the browser
  ignores it.
</p>
```

<img alt="html-paragraphs whitespace result" src="./code_sandbox/snaps/html-paragraphs-01-result.png" />

Horizontal rules (`hr.html`):

<img alt="html-paragraphs hr source" src="./code_sandbox/snaps/html-paragraphs-02-code.png" />

```html
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr />
<h2>This is heading 2</h2>
<p>This is some other text.</p>
<hr />
```

<img alt="html-paragraphs hr result" src="./code_sandbox/snaps/html-paragraphs-02-result.png" />

Line breaks (`br.html`):

<img alt="html-paragraphs br source" src="./code_sandbox/snaps/html-paragraphs-03-code.png" />

```html
<p>This is<br />a paragraph<br />with line breaks.</p>
```

<img alt="html-paragraphs br result" src="./code_sandbox/snaps/html-paragraphs-03-result.png" />

Poem in `<p>` (`poem.html`):

<img alt="html-paragraphs poem source" src="./code_sandbox/snaps/html-paragraphs-04-code.png" />

```html
<p>
  My Bonnie lies over the ocean. My Bonnie lies over the sea. My Bonnie lies
  over the ocean. Oh, bring back my Bonnie to me.
</p>
```

<img alt="html-paragraphs poem-in-p result" src="./code_sandbox/snaps/html-paragraphs-04-result.png" />

Poem in `<pre>` (`pre.html`):

<img alt="html-paragraphs pre source" src="./code_sandbox/snaps/html-paragraphs-05-code.png" />

```html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

<img alt="html-paragraphs pre result" src="./code_sandbox/snaps/html-paragraphs-05-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `<p>` define, and where does it start?

<details>
<summary>Answer</summary>

- [x] A **paragraph**.
- [x] It always starts on a **new line**.
- [x] Browsers add **margin** before and after it.

</details>

### Question 2: Do extra spaces and blank lines in the HTML source show on the page?

<details>
<summary>Answer</summary>

- [x] **No.** The browser **collapses** extra spaces and lines.
- [x] Many spaces or newlines count as **one space**.

</details>

### Question 3: What is `<hr>` for?

<details>
<summary>Answer</summary>

- [x] A **thematic break**, usually a **horizontal rule**.
- [x] It **separates** content (or marks a change).
- [x] It is an **empty** tag (no end tag).

</details>

### Question 4: When do you use `<br>` instead of a new `<p>`?

<details>
<summary>Answer</summary>

- [x] When you want a **new line** without starting a **new paragraph**.
- [x] `<br>` is **empty** (no end tag).

</details>

### Question 5: Why does a poem in `<p>` appear as one block?

<details>
<summary>Answer</summary>

- [x] `<p>` **ignores** extra line breaks in the source.
- [x] The lines collapse into **one paragraph**.

</details>

### Question 6: How do you keep a poem’s line breaks?

<details>
<summary>Answer</summary>

- [x] Use the `<pre>` element (**preformatted** text).
- [x] Spaces and line breaks in the source are **preserved**.

</details>

### Question 7: Can you control wrapping by adding spaces in the HTML file?

<details>
<summary>Answer</summary>

- [x] **No.** Screen size and window size change the wrap.
- [x] Extra spaces in the source do **not** control the layout.

</details>

</details>

## Summary

`<p>` starts a new paragraph with automatic **margin**. Extra source **spaces/newlines collapse**. `<hr>` is an empty **thematic break**; `<br>` is an empty **line break**. A poem in `<p>` becomes one flow; `<pre>` keeps the layout.

## References

- [HTML Paragraphs (W3Schools)](https://www.w3schools.com/html/html_paragraphs.asp)
- [Try it Yourself: tryhtml_paragraphs1](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs1)
- [Try it Yourself: tryhtml_paragraphs2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs2)
- [Try it Yourself: tryhtml_headings_hr](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_headings_hr)
- [Try it Yourself: tryhtml_paragraphs](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs)
- [Try it Yourself: tryhtml_poem](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_poem)
- [Try it Yourself: tryhtml_pre](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_pre)
- [MDN: `<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
- [MDN: `<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
- [MDN: `<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
- [MDN: `<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)

</details>

<details>
  <summary>HTML Styles</summary>

## Introduction

The HTML **`style`** attribute adds CSS to an element: **color**, **font**, **size**, alignment, and more. The syntax is `<tagname style="property:value;">`. You will learn more CSS later; this chapter is the inline `style` attribute.

## Detailed Explanation

- [x] **The `style` attribute**
  - Setting the style of an HTML element can be done with **`style`**.
  - Syntax: `<tagname style="property:value;">`.
  - The **property** is a CSS property; the **value** is a CSS value.
  - Intro demo: normal, red, blue, and 50px text.
  - Sandbox: `code_sandbox/html-styles/index.html`.

<img alt="html-styles result" src="./code_sandbox/snaps/html-styles-result.png" />

- [x] **Background color (`background-color`)**
  - Defines the **background color** for an HTML element.
  - Page background: `<body style="background-color:powderblue;">`.
  - Sandbox: `code_sandbox/html-styles/background.html`.

<img alt="html-styles body background result" src="./code_sandbox/snaps/html-styles-01-result.png" />

- [x] **Background color on individual elements**
  - The same property can style **different** elements (`h1` powderblue, `p` tomato).
  - Sandbox: `code_sandbox/html-styles/background2.html`.

<img alt="html-styles element backgrounds result" src="./code_sandbox/snaps/html-styles-02-result.png" />

- [x] **Text color (`color`)**
  - Defines the **text color** for an HTML element.
  - Sandbox: `code_sandbox/html-styles/color.html`.

<img alt="html-styles text color result" src="./code_sandbox/snaps/html-styles-03-result.png" />

- [x] **Fonts (`font-family`)**
  - Defines the **font** for an HTML element (Verdana heading, Courier paragraph).
  - Sandbox: `code_sandbox/html-styles/font.html`.

<img alt="html-styles font-family result" src="./code_sandbox/snaps/html-styles-04-result.png" />

- [x] **Text size (`font-size`)**
  - Defines the **text size**. Percentages are relative to the parent (here `300%` / `160%`).
  - Sandbox: `code_sandbox/html-styles/size.html`.

<img alt="html-styles font-size result" src="./code_sandbox/snaps/html-styles-05-result.png" />

- [x] **Text alignment (`text-align`)**
  - Defines **horizontal** text alignment (`center` in the example).
  - Sandbox: `code_sandbox/html-styles/align.html`.

<img alt="html-styles text-align result" src="./code_sandbox/snaps/html-styles-06-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the seven style examples: intro colors/size, body background, element backgrounds, text color, font-family, font-size, and text-align.

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-styles` file.
- [ ] Success: red/blue/big intro; powderblue page; powderblue heading and tomato paragraph; blue heading and red paragraph; Verdana/Courier; larger percent sizes; centered heading and paragraph.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-styles/`
- [ ] `http://127.0.0.1:8766/html-styles/background.html`
- [ ] `http://127.0.0.1:8766/html-styles/background2.html`
- [ ] `http://127.0.0.1:8766/html-styles/color.html`
- [ ] `http://127.0.0.1:8766/html-styles/font.html`
- [ ] `http://127.0.0.1:8766/html-styles/size.html`
- [ ] `http://127.0.0.1:8766/html-styles/align.html`

<img alt="html-styles result" src="./code_sandbox/snaps/html-styles-result.png" />

The style examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-styles/`.

</details>

<details>
  <summary>Code</summary>

## Code

Intro colors and size (`index.html`):

<img alt="html-styles source" src="./code_sandbox/snaps/html-styles-code.png" />

```html
<p>I am normal</p>
<p style="color:red;">I am red</p>
<p style="color:blue;">I am blue</p>
<p style="font-size:50px;">I am big</p>
```

<img alt="html-styles result" src="./code_sandbox/snaps/html-styles-result.png" />

Page background (`background.html`):

<img alt="html-styles body background source" src="./code_sandbox/snaps/html-styles-01-code.png" />

```html
<body style="background-color:powderblue;">
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
```

<img alt="html-styles body background result" src="./code_sandbox/snaps/html-styles-01-result.png" />

Element backgrounds (`background2.html`):

<img alt="html-styles element backgrounds source" src="./code_sandbox/snaps/html-styles-02-code.png" />

```html
<h1 style="background-color:powderblue;">This is a heading</h1>
<p style="background-color:tomato;">This is a paragraph.</p>
```

<img alt="html-styles element backgrounds result" src="./code_sandbox/snaps/html-styles-02-result.png" />

Text color (`color.html`):

<img alt="html-styles text color source" src="./code_sandbox/snaps/html-styles-03-code.png" />

```html
<h1 style="color:blue;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```

<img alt="html-styles text color result" src="./code_sandbox/snaps/html-styles-03-result.png" />

Fonts (`font.html`):

<img alt="html-styles font-family source" src="./code_sandbox/snaps/html-styles-04-code.png" />

```html
<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>
```

<img alt="html-styles font-family result" src="./code_sandbox/snaps/html-styles-04-result.png" />

Text size (`size.html`):

<img alt="html-styles font-size source" src="./code_sandbox/snaps/html-styles-05-code.png" />

```html
<h1 style="font-size:300%;">This is a heading</h1>
<p style="font-size:160%;">This is a paragraph.</p>
```

<img alt="html-styles font-size result" src="./code_sandbox/snaps/html-styles-05-result.png" />

Text alignment (`align.html`):

<img alt="html-styles text-align source" src="./code_sandbox/snaps/html-styles-06-code.png" />

```html
<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>
```

<img alt="html-styles text-align result" src="./code_sandbox/snaps/html-styles-06-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the syntax of the HTML `style` attribute?

<details>
<summary>Answer</summary>

- [x] `<tagname style="property:value;">`.
- [x] The **property** is a CSS property; the **value** is a CSS value.

</details>

### Question 2: Which CSS property sets a page or element background color?

<details>
<summary>Answer</summary>

- [x] **`background-color`**.
- [x] Example: `<body style="background-color:powderblue;">`.

</details>

### Question 3: Which property sets text color?

<details>
<summary>Answer</summary>

- [x] **`color`**.
- [x] Example: `<h1 style="color:blue;">`.

</details>

### Question 4: Which property chooses the font?

<details>
<summary>Answer</summary>

- [x] **`font-family`**.
- [x] Example: `font-family:verdana` or `font-family:courier`.

</details>

### Question 5: How do you change text size with the style attribute?

<details>
<summary>Answer</summary>

- [x] Use **`font-size`**.
- [x] The chapter uses percentages such as `300%` and `160%`.

</details>

### Question 6: How do you center text?

<details>
<summary>Answer</summary>

- [x] Use **`text-align:center`**.
- [x] It sets **horizontal** alignment.

</details>

### Question 7: Is inline `style` the only way to style HTML?

<details>
<summary>Answer</summary>

- [x] **No.** This chapter uses the **`style` attribute**.
- [x] You will learn more about **CSS** later in the tutorial.

</details>

</details>

## Summary

Use the **`style`** attribute for styling HTML elements. Use **`background-color`** for backgrounds, **`color`** for text colors, **`font-family`** for fonts, **`font-size`** for sizes, and **`text-align`** for alignment.

## References

- [HTML Styles (W3Schools)](https://www.w3schools.com/html/html_styles.asp)
- [Try it Yourself: tryhtml_styles_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_intro)
- [Try it Yourself: tryhtml_styles_background-color](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_background-color)
- [Try it Yourself: tryhtml_styles_background-color2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_background-color2)
- [Try it Yourself: tryhtml_styles_color](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_color)
- [Try it Yourself: tryhtml_styles_font-family](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_font-family)
- [Try it Yourself: tryhtml_styles_font-size](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_font-size)
- [Try it Yourself: tryhtml_styles_text-align](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_styles_text-align)
- [MDN: style](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style)
- [MDN: CSS background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)
- [MDN: CSS color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
- [MDN: CSS font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- [MDN: CSS font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
- [MDN: CSS text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)

</details>
<details>
  <summary>HTML Formatting</summary>

## Introduction

HTML has several elements for text with a **special meaning**: bold, important, italic, emphasized, small, marked, deleted, inserted, subscript, and superscript. Some tags change **look** (`<b>`, `<i>`); others add **meaning** (`<strong>`, `<em>`).

## Detailed Explanation

- [x] **Formatting elements**
  - `<b>` bold (no extra importance)
  - `<strong>` important (usually bold)
  - `<i>` italic / alternate voice or mood
  - `<em>` emphasized (usually italic; screen readers stress it)
  - `<small>` smaller text
  - `<mark>` marked / highlighted
  - `<del>` deleted (usually strikethrough)
  - `<ins>` inserted (usually underlined)
  - `<sub>` subscript (e.g. H₂O)
  - `<sup>` superscript (e.g. footnotes)
  - Intro demo: bold, italic, subscript, and superscript.
  - Sandbox: `code_sandbox/html-formatting/index.html`.

<img alt="html-formatting result" src="./code_sandbox/snaps/html-formatting-result.png" />

- [x] **`<b>` and `<strong>`**
  - `<b>` is **bold** without extra importance.
  - `<strong>` is **strong importance**; typically displayed bold.
  - Sandbox: `code_sandbox/html-formatting/b.html`, `strong.html`.

<img alt="html-formatting b result" src="./code_sandbox/snaps/html-formatting-01-result.png" />

<img alt="html-formatting strong result" src="./code_sandbox/snaps/html-formatting-02-result.png" />

- [x] **`<i>` and `<em>`**
  - `<i>` is an **alternate voice or mood** (technical term, other language, thought, ship name); typically italic.
  - `<em>` is **emphasized**; typically italic. A screen reader stresses the words.
  - Sandbox: `code_sandbox/html-formatting/i.html`, `em.html`.

<img alt="html-formatting i result" src="./code_sandbox/snaps/html-formatting-03-result.png" />

<img alt="html-formatting em result" src="./code_sandbox/snaps/html-formatting-04-result.png" />

- [x] **`<small>`**
  - Defines **smaller** text.
  - Sandbox: `code_sandbox/html-formatting/small.html`.

<img alt="html-formatting small result" src="./code_sandbox/snaps/html-formatting-05-result.png" />

- [x] **`<mark>`**
  - Defines text that should be **marked or highlighted**.
  - Sandbox: `code_sandbox/html-formatting/mark.html`.

<img alt="html-formatting mark result" src="./code_sandbox/snaps/html-formatting-06-result.png" />

- [x] **`<del>` and `<ins>`**
  - `<del>` is **deleted** text; browsers usually **strike through**.
  - `<ins>` is **inserted** text; browsers usually **underline**.
  - Sandbox: `code_sandbox/html-formatting/del.html`, `ins.html`.

<img alt="html-formatting del result" src="./code_sandbox/snaps/html-formatting-07-result.png" />

<img alt="html-formatting ins result" src="./code_sandbox/snaps/html-formatting-08-result.png" />

- [x] **`<sub>` and `<sup>`**
  - `<sub>` sits **half a character below** the line (chemical formulas).
  - `<sup>` sits **half a character above** the line (footnotes).
  - Sandbox: `code_sandbox/html-formatting/sub.html`, `sup.html`.

<img alt="html-formatting sub result" src="./code_sandbox/snaps/html-formatting-09-result.png" />

<img alt="html-formatting sup result" src="./code_sandbox/snaps/html-formatting-10-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the formatting examples: intro combo, then each tag (`b`, `strong`, `i`, `em`, `small`, `mark`, `del`, `ins`, `sub`, `sup`).

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-formatting` file.
- [ ] Success: bold/italic/sub/sup intro; bold vs important; italic vs emphasized; smaller text; yellow highlight on “milk”; strikethrough “blue”; strikethrough plus underlined “red”; subscript; superscript.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-formatting/`
- [ ] `http://127.0.0.1:8766/html-formatting/b.html`
- [ ] `http://127.0.0.1:8766/html-formatting/strong.html`
- [ ] `http://127.0.0.1:8766/html-formatting/i.html`
- [ ] `http://127.0.0.1:8766/html-formatting/em.html`
- [ ] `http://127.0.0.1:8766/html-formatting/small.html`
- [ ] `http://127.0.0.1:8766/html-formatting/mark.html`
- [ ] `http://127.0.0.1:8766/html-formatting/del.html`
- [ ] `http://127.0.0.1:8766/html-formatting/ins.html`
- [ ] `http://127.0.0.1:8766/html-formatting/sub.html`
- [ ] `http://127.0.0.1:8766/html-formatting/sup.html`

<img alt="html-formatting result" src="./code_sandbox/snaps/html-formatting-result.png" />

The formatting examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-formatting/`.

</details>

<details>
  <summary>Code</summary>

## Code

Intro (`index.html`):

<img alt="html-formatting source" src="./code_sandbox/snaps/html-formatting-code.png" />

```html
<p><b>This text is bold</b></p>
<p><i>This text is italic</i></p>
<p>This is<sub> subscript</sub> and <sup>superscript</sup></p>
```

<img alt="html-formatting result" src="./code_sandbox/snaps/html-formatting-result.png" />

Bold (`b.html`):

<img alt="html-formatting b source" src="./code_sandbox/snaps/html-formatting-01-code.png" />

```html
<b>This text is bold</b>
```

<img alt="html-formatting b result" src="./code_sandbox/snaps/html-formatting-01-result.png" />

Strong (`strong.html`):

<img alt="html-formatting strong source" src="./code_sandbox/snaps/html-formatting-02-code.png" />

```html
<strong>This text is important!</strong>
```

<img alt="html-formatting strong result" src="./code_sandbox/snaps/html-formatting-02-result.png" />

Italic (`i.html`):

<img alt="html-formatting i source" src="./code_sandbox/snaps/html-formatting-03-code.png" />

```html
<i>This text is italic</i>
```

<img alt="html-formatting i result" src="./code_sandbox/snaps/html-formatting-03-result.png" />

Emphasized (`em.html`):

<img alt="html-formatting em source" src="./code_sandbox/snaps/html-formatting-04-code.png" />

```html
<em>This text is emphasized</em>
```

<img alt="html-formatting em result" src="./code_sandbox/snaps/html-formatting-04-result.png" />

Small (`small.html`):

<img alt="html-formatting small source" src="./code_sandbox/snaps/html-formatting-05-code.png" />

```html
<small>This is some smaller text.</small>
```

<img alt="html-formatting small result" src="./code_sandbox/snaps/html-formatting-05-result.png" />

Mark (`mark.html`):

<img alt="html-formatting mark source" src="./code_sandbox/snaps/html-formatting-06-code.png" />

```html
<p>Do not forget to buy <mark>milk</mark> today.</p>
```

<img alt="html-formatting mark result" src="./code_sandbox/snaps/html-formatting-06-result.png" />

Deleted (`del.html`):

<img alt="html-formatting del source" src="./code_sandbox/snaps/html-formatting-07-code.png" />

```html
<p>My favorite color is <del>blue</del> red.</p>
```

<img alt="html-formatting del result" src="./code_sandbox/snaps/html-formatting-07-result.png" />

Inserted (`ins.html`):

<img alt="html-formatting ins source" src="./code_sandbox/snaps/html-formatting-08-code.png" />

```html
<p>My favorite color is <del>blue</del> <ins>red</ins>.</p>
```

<img alt="html-formatting ins result" src="./code_sandbox/snaps/html-formatting-08-result.png" />

Subscript (`sub.html`):

<img alt="html-formatting sub source" src="./code_sandbox/snaps/html-formatting-09-code.png" />

```html
<p>This is <sub>subscripted</sub> text.</p>
```

<img alt="html-formatting sub result" src="./code_sandbox/snaps/html-formatting-09-result.png" />

Superscript (`sup.html`):

<img alt="html-formatting sup source" src="./code_sandbox/snaps/html-formatting-10-code.png" />

```html
<p>This is <sup>superscripted</sup> text.</p>
```

<img alt="html-formatting sup result" src="./code_sandbox/snaps/html-formatting-10-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is the difference between `<b>` and `<strong>`?

<details>
<summary>Answer</summary>

- [x] `<b>` is **bold** without extra importance.
- [x] `<strong>` marks **strong importance** (usually displayed bold).

</details>

### Question 2: What is the difference between `<i>` and `<em>`?

<details>
<summary>Answer</summary>

- [x] `<i>` is an **alternate voice or mood** (typically italic).
- [x] `<em>` is **emphasized** text (typically italic).
- [x] A screen reader **stresses** words in `<em>`.

</details>

### Question 3: What does `<mark>` do?

<details>
<summary>Answer</summary>

- [x] It **marks or highlights** text.
- [x] Example: “Do not forget to buy **milk** today.”

</details>

### Question 4: How do browsers usually show `<del>` and `<ins>`?

<details>
<summary>Answer</summary>

- [x] `<del>`: **strikethrough** (deleted).
- [x] `<ins>`: **underline** (inserted).

</details>

### Question 5: When do you use `<sub>` vs `<sup>`?

<details>
<summary>Answer</summary>

- [x] `<sub>`: **below** the line (chemical formulas such as H₂O).
- [x] `<sup>`: **above** the line (footnotes).

</details>

### Question 6: What does `<small>` define?

<details>
<summary>Answer</summary>

- [x] **Smaller** text.

</details>

### Question 7: Name the ten formatting elements from this chapter.

<details>
<summary>Answer</summary>

- [x] `<b>`, `<strong>`, `<i>`, `<em>`, `<small>`, `<mark>`, `<del>`, `<ins>`, `<sub>`, `<sup>`.

</details>

</details>

## Summary

Use formatting tags for **meaning** and look: `<b>`/`<strong>`, `<i>`/`<em>`, `<small>`, `<mark>`, `<del>`/`<ins>`, `<sub>`/`<sup>`. Prefer `<strong>` and `<em>` when importance or emphasis is the point.

## References

- [HTML Text Formatting (W3Schools)](https://www.w3schools.com/html/html_formatting.asp)
- [Try it Yourself: tryhtml_formatting_intro](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_intro)
- [Try it Yourself: tryhtml_formatting_b](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_b)
- [Try it Yourself: tryhtml_formatting_strong](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_strong)
- [Try it Yourself: tryhtml_formatting_i](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_i)
- [Try it Yourself: tryhtml_formatting_em](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_em)
- [Try it Yourself: tryhtml_formatting_small](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_small)
- [Try it Yourself: tryhtml_formatting_mark](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_mark)
- [Try it Yourself: tryhtml_formatting_del](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_del)
- [Try it Yourself: tryhtml_formatting_del_ins](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_del_ins)
- [Try it Yourself: tryhtml_formatting_sub](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_sub)
- [Try it Yourself: tryhtml_formatting_sup](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_sup)
- [MDN: `<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
- [MDN: `<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
- [MDN: `<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
- [MDN: `<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
- [MDN: `<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
- [MDN: `<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
- [MDN: `<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
- [MDN: `<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
- [MDN: `<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)

</details>
<details>
  <summary>HTML Quotations</summary>

## Introduction

This chapter covers **quotation and citation** elements: `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, and `<bdo>`. They mark quotes, abbreviations, contact info, work titles, and text direction.

## Detailed Explanation

- [x] **`<blockquote>` for quotations**
  - Defines a section **quoted from another source**.
  - Browsers usually **indent** it.
  - Optional `cite` URL (here WWF).
  - Sandbox: `code_sandbox/html-quotations/index.html`.

<img alt="html-quotations blockquote result" src="./code_sandbox/snaps/html-quotations-result.png" />

- [x] **`<q>` for short quotations**
  - Defines a **short** quotation.
  - Browsers normally insert **quotation marks**.
  - Sandbox: `code_sandbox/html-quotations/q.html`.

<img alt="html-quotations q result" src="./code_sandbox/snaps/html-quotations-02-result.png" />

- [x] **`<abbr>` for abbreviations**
  - Defines an **abbreviation or acronym** (HTML, CSS, Mr., Dr., ASAP, ATM).
  - Helps browsers, translation systems, and search engines.
  - Use the global **`title`** attribute so the description shows on **mouse over**.
  - Sandbox: `code_sandbox/html-quotations/abbr.html`.

<img alt="html-quotations abbr result" src="./code_sandbox/snaps/html-quotations-03-result.png" />

- [x] **`<address>` for contact information**
  - Contact info for the **author/owner** of a document or article (email, URL, physical address, phone, social handle).
  - Usually **italic**. Browsers add a **line break** before and after.
  - Sandbox: `code_sandbox/html-quotations/address.html`.

<img alt="html-quotations address result" src="./code_sandbox/snaps/html-quotations-04-result.png" />

- [x] **`<cite>` for work title**
  - Title of a **creative work** (book, poem, song, movie, painting, sculpture).
  - A person’s name is **not** the title of a work.
  - Usually **italic**.
  - Sandbox: `code_sandbox/html-quotations/cite.html`.

<img alt="html-quotations cite result" src="./code_sandbox/snaps/html-quotations-05-result.png" />

- [x] **`<bdo>` for bi-directional override**
  - BDO = **Bi-Directional Override**.
  - Overrides the current **text direction** (`dir="rtl"` in the example).
  - Sandbox: `code_sandbox/html-quotations/bdo.html`.

<img alt="html-quotations bdo result" src="./code_sandbox/snaps/html-quotations-06-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the quotation examples: indented WWF blockquote, short `<q>` with quote marks, WHO abbreviation, italic address, _The Scream_ citation, and RTL `<bdo>`.

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-quotations` file.
- [ ] Success: indented WWF quote; quoted WWF goal; dotted WHO (tooltip “World Health Organization”); italic John Doe address; italic _The Scream_; reversed RTL sentence.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-quotations/`
- [ ] `http://127.0.0.1:8766/html-quotations/q.html`
- [ ] `http://127.0.0.1:8766/html-quotations/abbr.html`
- [ ] `http://127.0.0.1:8766/html-quotations/address.html`
- [ ] `http://127.0.0.1:8766/html-quotations/cite.html`
- [ ] `http://127.0.0.1:8766/html-quotations/bdo.html`

<img alt="html-quotations result" src="./code_sandbox/snaps/html-quotations-result.png" />

The quotation examples match the chapter.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-quotations/`.

</details>

<details>
  <summary>Code</summary>

## Code

Intro / blockquote (`index.html`):

<img alt="html-quotations intro" src="./code_sandbox/snaps/html-quotations-code.png" />

<img alt="html-quotations blockquote source" src="./code_sandbox/snaps/html-quotations-01-code.png" />

```html
<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
  For 60 years, WWF has worked to help people and nature thrive. As the world's
  leading conservation organization, WWF works in nearly 100 countries. At every
  level, we collaborate with people around the world to develop and deliver
  innovative solutions that protect communities, wildlife, and the places in
  which they live.
</blockquote>
```

<img alt="html-quotations blockquote result" src="./code_sandbox/snaps/html-quotations-result.png" />

Short quotation (`q.html`):

<img alt="html-quotations q source" src="./code_sandbox/snaps/html-quotations-02-code.png" />

```html
<p>
  WWF's goal is to:
  <q>Build a future where people live in harmony with nature.</q>
</p>
```

<img alt="html-quotations q result" src="./code_sandbox/snaps/html-quotations-02-result.png" />

Abbreviation (`abbr.html`):

<img alt="html-quotations abbr source" src="./code_sandbox/snaps/html-quotations-03-code.png" />

```html
<p>
  The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.
</p>
```

<img alt="html-quotations abbr result" src="./code_sandbox/snaps/html-quotations-03-result.png" />

Address (`address.html`):

<img alt="html-quotations address source" src="./code_sandbox/snaps/html-quotations-04-code.png" />

```html
<address>
  Written by John Doe.<br />
  Visit us at:<br />
  Example.com<br />
  Box 564, Disneyland<br />
  USA
</address>
```

<img alt="html-quotations address result" src="./code_sandbox/snaps/html-quotations-04-result.png" />

Cite (`cite.html`):

<img alt="html-quotations cite source" src="./code_sandbox/snaps/html-quotations-05-code.png" />

```html
<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>
```

<img alt="html-quotations cite result" src="./code_sandbox/snaps/html-quotations-05-result.png" />

Bi-directional override (`bdo.html`):

<img alt="html-quotations bdo source" src="./code_sandbox/snaps/html-quotations-06-code.png" />

```html
<bdo dir="rtl">This text will be written from right to left</bdo>
```

<img alt="html-quotations bdo result" src="./code_sandbox/snaps/html-quotations-06-result.png" />

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `<blockquote>` do, and how do browsers show it?

<details>
<summary>Answer</summary>

- [x] It marks a section **quoted from another source**.
- [x] Browsers usually **indent** it.
- [x] You can add a **`cite`** URL for the source.

</details>

### Question 2: How is `<q>` different from `<blockquote>`?

<details>
<summary>Answer</summary>

- [x] `<q>` is a **short** (inline) quotation.
- [x] Browsers normally add **quotation marks**.

</details>

### Question 3: Why use `<abbr>` with `title`?

<details>
<summary>Answer</summary>

- [x] It marks an **abbreviation or acronym**.
- [x] **`title`** shows the full description on **mouse over**.
- [x] It can help browsers, translation systems, and search engines.

</details>

### Question 4: What belongs in `<address>`?

<details>
<summary>Answer</summary>

- [x] **Contact information** for the author/owner of a document or article.
- [x] Email, URL, physical address, phone, social handle, etc.
- [x] Usually **italic**, with a line break before and after.

</details>

### Question 5: What should `<cite>` wrap?

<details>
<summary>Answer</summary>

- [x] The **title of a creative work**.
- [x] A person’s name is **not** the title of a work.
- [x] Usually rendered in **italic**.

</details>

### Question 6: What does `<bdo dir="rtl">` do?

<details>
<summary>Answer</summary>

- [x] **BDO** means Bi-Directional Override.
- [x] It **overrides** the current text direction (here **right-to-left**).

</details>

### Question 7: Name the six quotation/citation elements from this chapter.

<details>
<summary>Answer</summary>

- [x] `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, `<bdo>`.

</details>

</details>

## Summary

Use `<blockquote>` for a sourced block quote (usually indented), `<q>` for a short quote with marks, `<abbr title="...">` for acronyms, `<address>` for contact info, `<cite>` for a work’s title, and `<bdo>` to override text direction.

## References

- [HTML Quotation Elements (W3Schools)](https://www.w3schools.com/html/html_quotation_elements.asp)
- [Try it Yourself: tryhtml_formatting_intro2](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_intro2)
- [Try it Yourself: tryhtml_formatting_blockquote](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_blockquote)
- [Try it Yourself: tryhtml_formatting_q](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_q)
- [Try it Yourself: tryhtml_formatting_abbr](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_abbr)
- [Try it Yourself: tryhtml_formatting_address](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_address)
- [Try it Yourself: tryhtml_formatting_cite](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_cite)
- [Try it Yourself: tryhtml_formatting_bdo](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_formatting_bdo)
- [MDN: `<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
- [MDN: `<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
- [MDN: `<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
- [MDN: `<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
- [MDN: `<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
- [MDN: `<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)

</details>
<details>
  <summary>HTML Comments</summary>

## Introduction

HTML **comments** are **not displayed** in the browser. They document the source, hold reminders, and can **hide** content (temporarily, for debugging, or in the middle of a line). Syntax: `<!-- Write your comments here -->`. There is an **exclamation point** in the start tag, not the end tag.

## Detailed Explanation

- [x] **Comment syntax**
  - `<!-- Write your comments here -->`
  - `!` is only on the **start** tag.
  - Comments do **not** show in the browser; they document the source.

<img alt="html-comments syntax" src="./code_sandbox/snaps/html-comments-code.png" />

- [x] **Add comments (notifications and reminders)**
  - Place notes in the HTML: `<!-- This is a comment -->` and `<!-- Remember to add more information here -->`.
  - Only the paragraph is visible.
  - Sandbox: `code_sandbox/html-comments/index.html`.

<img alt="html-comments add result" src="./code_sandbox/snaps/html-comments-result.png" />

- [x] **Hide content**
  - Comment out markup to hide it **temporarily**.
  - Everything between `<!--` and `-->` is hidden from display.
  - Useful for **debugging**: comment out lines one at a time to find errors.
  - Sandbox: `code_sandbox/html-comments/hide.html` (one paragraph commented out).

<img alt="html-comments hide result" src="./code_sandbox/snaps/html-comments-02-result.png" />

- [x] **Hide more than one line**
  - A whole block (paragraph + image) can sit inside one comment.
  - Sandbox: `code_sandbox/html-comments/hide-block.html`.

<img alt="html-comments hide-block result" src="./code_sandbox/snaps/html-comments-03-result.png" />

- [x] **Hide inline content**
  - Comments can hide a **part of a line**.
  - `This <!-- great text --> is a paragraph.` displays as “This is a paragraph.”
  - Sandbox: `code_sandbox/html-comments/inline.html`.

<img alt="html-comments inline result" src="./code_sandbox/snaps/html-comments-04-result.png" />

<details>
  <summary>Lab</summary>

## Lab

Run the comment examples: reminders around a paragraph, a hidden extra paragraph, a hidden image block, and an inline hidden phrase.

### **Overview**

- [ ] Serve `code_sandbox` and open each `html-comments` file.
- [ ] Success: one visible paragraph (comments hidden); two paragraphs with the middle one commented out; two paragraphs with the image block commented out; “This is a paragraph.” without “great text”.

### **Task 1: Serve and open**

- [ ] From `Personal/Files/html/code_sandbox`:

```bash
python -m http.server 8766 --bind 127.0.0.1
```

- [ ] `http://127.0.0.1:8766/html-comments/`
- [ ] `http://127.0.0.1:8766/html-comments/hide.html`
- [ ] `http://127.0.0.1:8766/html-comments/hide-block.html`
- [ ] `http://127.0.0.1:8766/html-comments/inline.html`

<img alt="html-comments result" src="./code_sandbox/snaps/html-comments-result.png" />

The comment examples match the chapter.

</details>

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
  <summary>Code</summary>

## Code

Syntax:

<img alt="html-comments syntax source" src="./code_sandbox/snaps/html-comments-code.png" />

```html
<!-- Write your comments here -->
```

Add comments (`index.html`):

<img alt="html-comments add source" src="./code_sandbox/snaps/html-comments-01-code.png" />

```html
<!-- This is a comment -->

<p>This is a paragraph.</p>

<!-- Remember to add more information here -->
```

<img alt="html-comments add result" src="./code_sandbox/snaps/html-comments-result.png" />

Hide content (`hide.html`):

<img alt="html-comments hide source" src="./code_sandbox/snaps/html-comments-02-code.png" />

```html
<p>This is a paragraph.</p>

<!-- <p>This is another paragraph </p> -->

<p>This is a paragraph too.</p>
```

<img alt="html-comments hide result" src="./code_sandbox/snaps/html-comments-02-result.png" />

Hide a section (`hide-block.html`):

<img alt="html-comments hide-block source" src="./code_sandbox/snaps/html-comments-03-code.png" />

```html
<p>This is a paragraph.</p>
<!--
<p>Look at this cool image:</p>
<img border="0" src="pic_trulli.jpg" alt="Trulli">
-->
<p>This is a paragraph too.</p>
```

<img alt="html-comments hide-block result" src="./code_sandbox/snaps/html-comments-03-result.png" />

Hide inline (`inline.html`):

<img alt="html-comments inline source" src="./code_sandbox/snaps/html-comments-04-code.png" />

```html
<p>
  This
  <!-- great text -->
  is a paragraph.
</p>
```

<img alt="html-comments inline result" src="./code_sandbox/snaps/html-comments-04-result.png" />

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

</details>
