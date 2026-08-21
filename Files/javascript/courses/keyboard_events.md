# Keyboard Events

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Keyboard events are `keydown` and `keyup`. Read `event.key` for meaning and `event.code` for the physical key.

This section has **6** examples:

- [x] **Example 1:** keydown — event.key [View](#keyboard-events-example-01)
- [x] **Example 2:** event.key — value of the key [View](#keyboard-events-example-02)
- [x] **Example 3:** event.code — physical key [View](#keyboard-events-example-03)
- [x] **Example 4:** Modifier keys — ctrlKey, shiftKey, altKey, metaKey [View](#keyboard-events-example-04)
- [x] **Example 5:** Using event.code === "Enter" [View](#keyboard-events-example-05)
- [x] **Example 6:** keyup and deprecated keypress [View](#keyboard-events-example-06)

## Detailed Explanation

- [x] `keypress` is deprecated.
- [x] `key` vs `code` (Z vs KeyZ).
- [x] Modifier flags for shortcuts.

<a id="keyboard-events-example-01"></a>

### **Example 1: keydown — event.key**

- [x] `keydown` fires when a key is pressed (and repeats).
- [x] `event.key` is the **character/name** and depends on layout and Shift (`z` vs `Z`).
- [x] Listen on an input or on `document` depending on whether you need a focused field.

Sandbox: `code_sandbox/keyboard-events/keydown-key.html`

```html
<input id="k">
<p id="out"></p>
<script>
const k = document.getElementById("k");
k.addEventListener("keydown", function (event) {
  document.getElementById("out").innerHTML = "You pressed: " + event.key;
});
</script>
```

<img alt="keyboard-events example 1 source" src="../code_sandbox/snaps/keyboard-events-01-code.png" />

<img alt="keyboard-events example 1 result" src="../code_sandbox/snaps/keyboard-events-01-result.png" />

- [x] **Outcome:** Pressing **Z** shows **You pressed: Z**.

<a id="keyboard-events-example-02"></a>

### **Example 2: event.key — value of the key**

- [x] Table row: `event.key` returns the key value; with Shift it can be **Z** instead of **z**.
- [x] Language layouts can change `key` (`"z"` vs another letter on the same physical key).
- [x] Use `key` when you care about **meaning** (Enter, Escape, the letter typed).

Sandbox: `code_sandbox/keyboard-events/key-property.html`

```html
<script>
const event = new KeyboardEvent("keydown", { key: "z" });
</script>
```

<img alt="keyboard-events example 2 source" src="../code_sandbox/snaps/keyboard-events-02-code.png" />

<img alt="keyboard-events example 2 result" src="../code_sandbox/snaps/keyboard-events-02-result.png" />

- [x] **Outcome:** A synthetic event with `key: "z"` reports **z**.

<a id="keyboard-events-example-03"></a>

### **Example 3: event.code — physical key**

- [x] `event.code` is the **physical key** (`"KeyZ"`) and stays the same across layouts.
- [x] When pressing Z, `code` is always **KeyZ** even if `key` is another character.
- [x] Use `code` for game-style WASD that should not move when the user has a different layout.

Sandbox: `code_sandbox/keyboard-events/code-property.html`

```html
<script>
const event = new KeyboardEvent("keydown", { key: "z", code: "KeyZ" });
</script>
```

<img alt="keyboard-events example 3 source" src="../code_sandbox/snaps/keyboard-events-03-code.png" />

<img alt="keyboard-events example 3 result" src="../code_sandbox/snaps/keyboard-events-03-result.png" />

- [x] **Outcome:** `event.code` is **KeyZ**.

<a id="keyboard-events-example-04"></a>

### **Example 4: Modifier keys — ctrlKey, shiftKey, altKey, metaKey**

- [x] Boolean flags on the KeyboardEvent tell you if Ctrl / Shift / Alt / Meta (Cmd) were held.
- [x] Shortcuts such as Ctrl+S check `event.ctrlKey && event.key === "s"` (and usually `preventDefault`).
- [x] `metaKey` is the Command key on macOS.

Sandbox: `code_sandbox/keyboard-events/modifiers.html`

```html
<script>
const event = new KeyboardEvent("keydown", { key: "s", ctrlKey: true });
</script>
```

<img alt="keyboard-events example 4 source" src="../code_sandbox/snaps/keyboard-events-04-code.png" />

<img alt="keyboard-events example 4 result" src="../code_sandbox/snaps/keyboard-events-04-result.png" />

- [x] **Outcome:** A Ctrl+S event has **ctrlKey true** and **key s**.

<a id="keyboard-events-example-05"></a>

### **Example 5: Using event.code === "Enter"**

- [x] W3Schools listens for `event.code === "Enter"` on an input.
- [x] `Enter` is the code for the main Enter key (`NumpadEnter` is separate).
- [x] The snapshot dispatches Enter and writes **Enter was pressed!**.

Sandbox: `code_sandbox/keyboard-events/enter-code.html`

```html
<input id="in01">
<p id="out"></p>
<script>
const in01 = document.getElementById("in01");
in01.addEventListener("keydown", function (event) {
  if (event.code === "Enter") {
    document.getElementById("out").innerHTML = "Enter was pressed!";
  }
});
</script>
```

<img alt="keyboard-events example 5 source" src="../code_sandbox/snaps/keyboard-events-05-code.png" />

<img alt="keyboard-events example 5 result" src="../code_sandbox/snaps/keyboard-events-05-result.png" />

- [x] **Outcome:** The output paragraph is **Enter was pressed!**.

<a id="keyboard-events-example-06"></a>

### **Example 6: keyup and deprecated keypress**

- [x] `keyup` fires when the key is **released** (no repeat).
- [x] `keypress` fired only for **character** keys, not Alt/Backspace, and is **deprecated**.
- [x] Use `keydown` or `keyup` in new code.

Sandbox: `code_sandbox/keyboard-events/keyup-and-keypress.html`

```html
<input id="k">
```

<img alt="keyboard-events example 6 source" src="../code_sandbox/snaps/keyboard-events-06-code.png" />

<img alt="keyboard-events example 6 result" src="../code_sandbox/snaps/keyboard-events-06-result.png" />

- [x] **Outcome:** `keyup` for **a** is logged. `keypress` is marked deprecated.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/keyboard-events/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Which keyboard events should you use?

<details>
<summary>Answer</summary>

- [x] **`keydown`** and **`keyup`**. Avoid **`keypress`**.

</details>

### Question 2: `event.key` for Shift+Z?

<details>
<summary>Answer</summary>

- [x] Typically **`Z`** (the produced character), not `z`.

</details>

### Question 3: `event.code` for that same press?

<details>
<summary>Answer</summary>

- [x] **`KeyZ`** — physical key, layout-independent.

</details>

### Question 4: How do you detect Ctrl+S?

<details>
<summary>Answer</summary>

- [x] `event.ctrlKey && event.key.toLowerCase() === "s"` (and usually `preventDefault`).

</details>

### Question 5: What is `metaKey`?

<details>
<summary>Answer</summary>

- [x] The **Command** key on Apple keyboards (Windows key on some others).

</details>

### Question 6: How does the W3Schools Enter demo detect Enter?

<details>
<summary>Answer</summary>

- [x] `event.code === "Enter"`.

</details>

### Question 7: Does `keydown` repeat?

<details>
<summary>Answer</summary>

- [x] Yes, if the key is **held**.

</details>

### Question 8: Does `keyup` repeat?

<details>
<summary>Answer</summary>

- [x] No — it fires once on **release**.

</details>

### Question 9: Why did `keypress` skip Backspace?

<details>
<summary>Answer</summary>

- [x] It only fired for **character** keys. That is one reason it was deprecated.

</details>

### Question 10: Should shortcuts listen on `window` or an input?

<details>
<summary>Answer</summary>

- [x] On **`window`/`document`** for app-wide shortcuts; on the **input** for field-specific keys.

</details>


</details>

## Summary

Listen for `keydown`/`keyup`, branch on `key` or `code`, and check `ctrlKey`/`shiftKey`/`altKey`/`metaKey` for chords.

## References

- [Keyboard Events](https://www.w3schools.com/js/js_events_keyboard.asp)
- [MDN EventTarget.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
