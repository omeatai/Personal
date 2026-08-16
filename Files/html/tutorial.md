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
  - Web pages *can* be built with professional HTML editors.
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
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
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

<p>This is a paragraph
<p>This is a paragraph

</body>
</html>
```

<img alt="html-elements omitted end tags result" src="./code_sandbox/snaps/html-elements-01-result.png" />

Line break: `code_sandbox/html-elements/br.html`

<img alt="html-elements br source" src="./code_sandbox/snaps/html-elements-02-code.png" />

```html
<p>This is a <br> paragraph with a line break.</p>
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



