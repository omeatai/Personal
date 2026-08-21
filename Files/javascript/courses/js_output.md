# JS Output

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript can **display data** in several ways: **`innerHTML`**, **`innerText`**, **`document.write()`**, **`window.alert()`**, **`console.log()`**, and (for printing the window) **`window.print()`**. This section shows each method and when **not** to use `document.write()`.

This section has **5** examples:

- [x] **Example 1:** Using `innerHTML` [View](#js-output-example-01)
- [x] **Example 2:** Using `innerText` [View](#js-output-example-02)
- [x] **Example 3:** Using `document.write()` [View](#js-output-example-03)
- [x] **Example 4:** Using `window.alert()` [View](#js-output-example-04)
- [x] **Example 5:** Using `console.log()` [View](#js-output-example-05)

## Detailed Explanation

- [x] **JavaScript has four everyday ways to "display" data**
  - Into an **HTML element** with **`innerHTML`** or **`innerText`**.
  - Into the **HTML output stream** with **`document.write()`**.
  - Into an **alert box** with **`window.alert()`**.
  - Into the **browser console** with **`console.log()`**.
- [x] **Common access pattern**
  - Most on-page output starts with **`document.getElementById(id)`** to grab an element by its `id`, then assigns a property.

<a id="js-output-example-01"></a>

### **Example 1: Using `innerHTML`**

- [x] `innerHTML` sets the element's content and **parses it as HTML**, so `"<h2>Hello World</h2>"` renders as a real heading.
- [x] Changing `innerHTML` is the **most common** way to display data in a page.
- [x] The target `<p id="demo">` starts empty and is filled by the script during load.

Sandbox: `code_sandbox/js-output/index.html`

```html
<h1>My First Web Page</h1>
<p>My First Paragraph</p>
<p id="demo"></p>
<script>
  document.getElementById("demo").innerHTML = "<h2>Hello World</h2>";
</script>
```

![js-output example 1 source](../code_sandbox/snaps/js-output-01-code.png)

![js-output example 1 result](../code_sandbox/snaps/js-output-01-result.png)

- [x] **Outcome:** the empty paragraph becomes a large bold **Hello World** heading (the `<h2>` tags were parsed, not shown literally).

<a id="js-output-example-02"></a>

### **Example 2: Using `innerText`**

- [x] `innerText` sets the element's **plain text**; any HTML in the string would show up **literally**, not rendered.
- [x] Rule of thumb: use **`innerHTML`** to insert markup, **`innerText`** when you only want text.

Sandbox: `code_sandbox/js-output/innertext.html`

```html
<h1>My First Web Page</h1>
<p>My First Paragraph</p>
<p id="demo"></p>
<script>
  document.getElementById("demo").innerText = "Hello World";
</script>
```

![js-output example 2 source](../code_sandbox/snaps/js-output-02-code.png)

![js-output example 2 result](../code_sandbox/snaps/js-output-02-result.png)

- [x] **Outcome:** the paragraph shows plain, normal-sized **Hello World** — compare with Example 1's big heading to see the `innerHTML` vs `innerText` difference.

<a id="js-output-example-03"></a>

### **Example 3: Using `document.write()`**

- [x] `document.write()` writes straight into the HTML output **while the page is parsing** — here it prints `5 + 6`, i.e. **11**.
- [x] **Warning:** calling `document.write()` **after** the page has finished loading (e.g. from a button) **erases the whole document** and replaces it with the written value.
- [x] Because of that, `document.write()` should be used **only for quick testing**.

Sandbox: `code_sandbox/js-output/write.html`

```html
<h1>My First Web Page</h1>
<p>My first paragraph.</p>
<script>
  document.write(5 + 6);
</script>

<!-- After load this wipes the page: -->
<button type="button" onclick="document.write(5 + 6)">Try it</button>
```

![js-output example 3 source](../code_sandbox/snaps/js-output-03-code.png)

![js-output example 3 result](../code_sandbox/snaps/js-output-03-result.png)

- [x] **Outcome:** during load the number **11** appears under the paragraph. If you instead clicked a **Try it** button after load, the entire page would be replaced by a bare **11**.

<a id="js-output-example-04"></a>

### **Example 4: Using `window.alert()`**

- [x] `window.alert(5 + 6)` pops a modal **alert box** showing **11**.
- [x] The **`window`** keyword is **optional** — `alert(5 + 6)` is identical, because `window` is the **global scope object** and its methods are available unqualified.
- [x] The alert is a **native browser dialog**, so the snap below shows the trigger page; the dialog itself is described in the outcome.

Sandbox: `code_sandbox/js-output/alert.html`

```html
<h1>My First Web Page</h1>
<p>My first paragraph.</p>
<script>
  window.alert(5 + 6);
  // the window keyword is optional:
  alert(5 + 6);
</script>
```

![js-output example 4 source](../code_sandbox/snaps/js-output-04-code.png)

![js-output example 4 result](../code_sandbox/snaps/js-output-04-result.png)

- [x] **Outcome:** clicking **Show alert (5 + 6)** (or loading the auto-run version) opens a native dialog reading **11**; the page underneath is unchanged.

<a id="js-output-example-05"></a>

### **Example 5: Using `console.log()`**

- [x] `console.log()` writes to the **browser console** (DevTools), the standard tool for **debugging** — it does **not** change the page.
- [x] To make the value visible in a screenshot, the sandbox **mirrors** the logged value into an on-page box; the real `console.log(5 + 6)` still runs.

Sandbox: `code_sandbox/js-output/console.html`

```html
<script>
  console.log(5 + 6);
</script>
```

![js-output example 5 source](../code_sandbox/snaps/js-output-05-code.png)

![js-output example 5 result](../code_sandbox/snaps/js-output-05-result.png)

- [x] **Outcome:** the browser console logs **11**; the mirrored on-page box shows **> 11** so you can see the value in the snapshot.

### **JavaScript Print**

- [x] JavaScript has **no** print object and cannot access output devices.
- [x] The one exception is **`window.print()`**, which opens the browser's print dialog for the current window: `<button onclick="window.print()">Print this page</button>`.
- [x] This opens the OS/browser print dialog (not screenshotted here), so it is documented as code only.
- [x] **Page exercise —** _Which is NOT correct output syntax?_ → **`body.html()`** (there is no such method; the valid ones are `window.alert()`, `console.log()`, `document.write()`).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-output/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the main ways JavaScript can display data?

<details>
<summary>Answer</summary>

- [x] **`innerHTML`** / **`innerText`** on an HTML element.
- [x] **`document.write()`**.
- [x] **`window.alert()`**.
- [x] **`console.log()`**.

</details>

### Question 2: How do you change an element’s HTML content?

<details>
<summary>Answer</summary>

- [x] `document.getElementById(id)` to access the element.
- [x] Set the **`innerHTML`** property.

</details>

### Question 3: When should you use `innerHTML` vs `innerText`?

<details>
<summary>Answer</summary>

- [x] **`innerHTML`** when you want to change an **HTML element**.
- [x] **`innerText`** when you only want to change **plain text**.

</details>

### Question 4: What is the most common way to display data in HTML?

<details>
<summary>Answer</summary>

- [x] Changing the **`innerHTML`** property of an HTML element.

</details>

### Question 5: What happens if you call `document.write()` after the page has loaded?

<details>
<summary>Answer</summary>

- [x] It **deletes all existing HTML**.
- [x] Use `document.write()` **only for testing**.

</details>

### Question 6: Can you omit `window` in `window.alert()`?

<details>
<summary>Answer</summary>

- [x] **Yes.** `alert(5 + 6)` works.
- [x] **`window`** is the **global scope** object, so the keyword is optional.

</details>

### Question 7: What is `console.log()` for?

<details>
<summary>Answer</summary>

- [x] **Debugging** in the browser.
- [x] It displays data in the **console**.

</details>

### Question 8: Can JavaScript print to a printer as a general output device?

<details>
<summary>Answer</summary>

- [x] JavaScript has **no** general print object or print methods for output devices.
- [x] The exception is **`window.print()`**, which prints the **current window**.

</details>

</details>

## Summary

Display data with **`innerHTML`** (most common, can inject HTML), **`innerText`** (plain text), **`document.write()`** (testing only; after load it **wipes** the page), **`alert()`** / **`window.alert()`**, and **`console.log()`** for debugging. **`window.print()`** prints the current window. `window` is the global object, so its methods can be called without the prefix.

## References

- [JS Output (W3Schools)](https://www.w3schools.com/js/js_output.asp)
- [Try it Yourself: tryjs_output_innerhtml](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_innerhtml)
- [Try it Yourself: tryjs_output_innertext](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_innertext)
- [Try it Yourself: tryjs_output_write](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_write)
- [Try it Yourself: tryjs_output_write_over](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_write_over)
- [Try it Yourself: tryjs_output_alert](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_alert)
- [Try it Yourself: tryjs_output_console](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_console)
- [Try it Yourself: tryjs_output_print](https://www.w3schools.com/js/tryit.asp?filename=tryjs_output_print)
- [MDN: Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
- [MDN: Node.innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText)
- [MDN: Document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write)
