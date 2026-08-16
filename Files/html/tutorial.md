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

