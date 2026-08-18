<details>
  <summary>Manage Events</summary>

## Introduction

Event management is adding listeners, removing them with the same function, and blocking defaults with `preventDefault`.

This section has **4** examples:

- [x] **Example 1:** Adding events [View](#manage-events-example-01)
- [x] **Example 2:** Removing events [View](#manage-events-example-02)
- [x] **Example 3:** You must pass the same named function to remove [View](#manage-events-example-03)
- [x] **Example 4:** Blocking events — preventDefault on a link [View](#manage-events-example-04)

## Detailed Explanation

- [x] Named functions can be removed.
- [x] Anonymous functions cannot be removed unless you kept the reference.
- [x] `preventDefault` stops navigation/submit.

<a id="manage-events-example-01"></a>

### **Example 1: Adding events**

- [x] `addEventListener("click", myFunction)` registers a **named** function.
- [x] Named functions can be removed later; anonymous functions cannot (unless you kept the reference).
- [x] The snapshot clicks **Click** and prints **Clicked!**.

Sandbox: `code_sandbox/manage-events/add.html`

```html
<button type="button" id="btn">Click</button>
<p id="out"></p>
<script>
const btn = document.getElementById("btn");
btn.addEventListener("click", myFunction);
function myFunction() {
  document.getElementById("out").innerHTML = "Clicked!";
}
</script>
```

<img alt="manage-events example 1 source" src="./code_sandbox/snaps/manage-events-01-code.png" />

<img alt="manage-events example 1 result" src="./code_sandbox/snaps/manage-events-01-result.png" />

- [x] **Outcome:** The output is **Clicked!**.

<a id="manage-events-example-02"></a>

### **Example 2: Removing events**

- [x] `removeEventListener` needs the **same function object** you added.
- [x] W3Schools: Add attaches `myFunction` to Test; Remove detaches it.
- [x] The snapshot Adds, clicks Test (**Hello!**), Removes, clicks again (no second Hello).

Sandbox: `code_sandbox/manage-events/remove.html`

```html
<button type="button" id="add">Add</button>
<button type="button" id="remove">Remove</button>
<button type="button" id="test">Test click</button>
<p id="out"></p>
```

<img alt="manage-events example 2 source" src="./code_sandbox/snaps/manage-events-02-code.png" />

<img alt="manage-events example 2 result" src="./code_sandbox/snaps/manage-events-02-result.png" />

- [x] **Outcome:** After add → test → remove → test, the log is a **single** Hello! — the second click did nothing.

<a id="manage-events-example-03"></a>

### **Example 3: You must pass the same named function to remove**

- [x] `removeEventListener("click", function(){…})` does **not** remove a previously added anonymous function — they are different objects.
- [x] Store the function in a `const` / `function` declaration and pass that variable both times.
- [x] This example shows a failed remove (anonymous) vs a successful remove (named).

Sandbox: `code_sandbox/manage-events/same-function-note.html`

```html
<button type="button" id="b">Click</button>
```

<img alt="manage-events example 3 source" src="./code_sandbox/snaps/manage-events-03-code.png" />

<img alt="manage-events example 3 result" src="./code_sandbox/snaps/manage-events-03-result.png" />

- [x] **Outcome:** Named remove works: only **one** tick is logged after the second click is detached.

<a id="manage-events-example-04"></a>

### **Example 4: Blocking events — preventDefault on a link**

- [x] `event.preventDefault()` stops the **browser’s default** (navigate, submit, check a checkbox).
- [x] The W3Schools link “Go to W3Schools” is blocked; the page prints **Link blocked!** instead of leaving.
- [x] It does **not** stop other listeners unless you also `stopPropagation` / `stopImmediatePropagation`.

Sandbox: `code_sandbox/manage-events/preventdefault.html`

```html
<a id="link" href="https://www.w3schools.com">Go to W3Schools</a>
<p id="out"></p>
<script>
const link = document.getElementById("link");
link.addEventListener("click", function (event) {
  event.preventDefault();
  document.getElementById("out").innerHTML = "Link blocked!";
});
</script>
```

<img alt="manage-events example 4 source" src="./code_sandbox/snaps/manage-events-04-code.png" />

<img alt="manage-events example 4 result" src="./code_sandbox/snaps/manage-events-04-result.png" />

- [x] **Outcome:** The click does not navigate. The paragraph reads **Link blocked!**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/manage-events/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you add a click listener?

<details>
<summary>Answer</summary>

- [x] `element.addEventListener("click", handler)`.

</details>

### Question 2: How do you remove it?

<details>
<summary>Answer</summary>

- [x] `element.removeEventListener("click", handler)` with the **same function**.

</details>

### Question 3: Why can’t you remove an inline anonymous listener?

<details>
<summary>Answer</summary>

- [x] You don’t have the **same function object** to pass to `removeEventListener`.

</details>

### Question 4: In the Add/Remove demo, what does Remove do?

<details>
<summary>Answer</summary>

- [x] It stops **Test click** from running `myFunction`.

</details>

### Question 5: What does `preventDefault` do on a link?

<details>
<summary>Answer</summary>

- [x] Stops **navigation** so you can handle the click in JS.

</details>

### Question 6: Does `preventDefault` stop bubbling?

<details>
<summary>Answer</summary>

- [x] **No**. Use `stopPropagation` for that.

</details>

### Question 7: Can you add the same named function twice?

<details>
<summary>Answer</summary>

- [x] Yes — it can run **twice** unless you guard or remove first.

</details>

### Question 8: Should the Add button use an anonymous function?

<details>
<summary>Answer</summary>

- [x] Yes for the Add/Remove *wiring*; the **test** handler itself must stay **named** so it can be removed.

</details>

### Question 9: What happens if you click Test before Add?

<details>
<summary>Answer</summary>

- [x] Nothing — the listener is not attached yet.

</details>

### Question 10: Is `return false` in an HTML `onclick` the same as `preventDefault`?

<details>
<summary>Answer</summary>

- [x] In HTML `onclick`, `return false` prevents default **and** stops bubbling. In `addEventListener`, `return false` does **not** — call the methods.

</details>


</details>

## Summary

Add with `addEventListener`, remove with the same function, and call `preventDefault` when the browser action should not happen.

## References

- [Manage Events](https://www.w3schools.com/js/js_events_management.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

</details>
