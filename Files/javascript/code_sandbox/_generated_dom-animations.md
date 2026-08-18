<details>
  <summary>DOM Animations</summary>

## Introduction

A JavaScript animation is a timer that changes inline styles a little at a time inside a positioned container.

This section has **5** examples:

- [x] **Example 1:** A basic web page for the animation [View](#dom-animations-example-01)
- [x] **Example 2:** Create an animation container [View](#dom-animations-example-02)
- [x] **Example 3:** Style the elements — relative container, absolute mover [View](#dom-animations-example-03)
- [x] **Example 4:** Animation code — setInterval and clearInterval [View](#dom-animations-example-04)
- [x] **Example 5:** Full animation — myMove() diagonal slide [View](#dom-animations-example-05)

## Detailed Explanation

- [x] Container `position:relative`, mover `position:absolute`.
- [x] `setInterval(frame, 5)` + `clearInterval` when done.
- [x] `myMove` increments `top` and `left` until `pos == 350`.

<a id="dom-animations-example-01"></a>

### **Example 1: A basic web page for the animation**

- [x] W3Schools starts with a heading and a placeholder: **My animation will go here**.
- [x] You need a page **structure** first; the moving box comes next.
- [x] Keep animation markup simple so the timer code is easy to see.

Sandbox: `code_sandbox/dom-animations/basic-page.html`

```html
<h2>My First JavaScript Animation</h2>
<div>My animation will go here</div>
```

<img alt="dom-animations example 1 source" src="./code_sandbox/snaps/dom-animations-01-code.png" />

<img alt="dom-animations example 1 result" src="./code_sandbox/snaps/dom-animations-01-result.png" />

- [x] **Outcome:** The page shows the title and the placeholder box area.

<a id="dom-animations-example-02"></a>

### **Example 2: Create an animation container**

- [x] All animations should be **relative to a container** so coordinates stay inside that box.
- [x] The moving element is a child of the container, not of the whole page.
- [x] Later CSS: container `position: relative`, mover `position: absolute`.

Sandbox: `code_sandbox/dom-animations/container.html`

```html
<div id="container">
  <div id="animate">My animation will go here</div>
</div>
```

<img alt="dom-animations example 2 source" src="./code_sandbox/snaps/dom-animations-02-code.png" />

<img alt="dom-animations example 2 result" src="./code_sandbox/snaps/dom-animations-02-result.png" />

- [x] **Outcome:** The red square lives **inside** the yellow `#container`.

<a id="dom-animations-example-03"></a>

### **Example 3: Style the elements — relative container, absolute mover**

- [x] Container: `position: relative` (and a size + background).
- [x] Mover: `position: absolute` so `top` / `left` are relative to the container.
- [x] W3Schools uses a **400×400** yellow field and a **50×50** red square (this snap uses 400×200 to fit).
- [x] Without relative/absolute, `top`/`left` will not animate inside the box.

Sandbox: `code_sandbox/dom-animations/style-relative-absolute.html`

```css
#container {
  width: 400px;
  height: 400px;
  position: relative;
  background: yellow;
}
#animate {
  width: 50px;
  height: 50px;
  position: absolute;
  background: red;
}
```

<img alt="dom-animations example 3 source" src="./code_sandbox/snaps/dom-animations-03-code.png" />

<img alt="dom-animations example 3 result" src="./code_sandbox/snaps/dom-animations-03-result.png" />

- [x] **Outcome:** Computed position of the container is **relative**; the square is **absolute**.

<a id="dom-animations-example-04"></a>

### **Example 4: Animation code — setInterval and clearInterval**

- [x] JS animation = **small style changes** on a timer so it looks continuous.
- [x] `id = setInterval(frame, 5)` calls `frame` every **5 ms**.
- [x] When the end test is true, **`clearInterval(id)`** stops the timer (or it runs forever).
- [x] Else, change `top`/`left` (or opacity, width, …).

Sandbox: `code_sandbox/dom-animations/interval-skeleton.html`

```javascript
id = setInterval(frame, 5);
function frame() {
  if (/* test for finished */) {
    clearInterval(id);
  } else {
    /* code to change the element style */
  }
}
```

<img alt="dom-animations example 4 source" src="./code_sandbox/snaps/dom-animations-04-code.png" />

<img alt="dom-animations example 4 result" src="./code_sandbox/snaps/dom-animations-04-result.png" />

- [x] **Outcome:** The sandbox starts a 5ms interval, increments a counter to 3, then **clears** it — the pattern of the skeleton.

<a id="dom-animations-example-05"></a>

### **Example 5: Full animation — myMove() diagonal slide**

- [x] `myMove` reads `#animate`, starts `pos` at 0, and every 5ms adds **1px** to `top` and `left`.
- [x] When `pos == 350` it **clears** the interval (50px box in a 400px field → 350px of travel).
- [x] `clearInterval(id)` at the start avoids stacking timers if you click Move twice.
- [x] The snapshot calls `myMove()` immediately and waits so you see the square **away from the origin**.

Sandbox: `code_sandbox/dom-animations/mymove.html`

```html
<button type="button" onclick="myMove()">Move</button>
<div id="container"><div id="animate"></div></div>
<script>
function myMove() {
  let id = null;
  const elem = document.getElementById("animate");
  let pos = 0;
  clearInterval(id);
  id = setInterval(frame, 5);
  function frame() {
    if (pos == 350) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.top = pos + "px";
      elem.style.left = pos + "px";
    }
  }
}
</script>
```

<img alt="dom-animations example 5 source" src="./code_sandbox/snaps/dom-animations-05-code.png" />

<img alt="dom-animations example 5 result" src="./code_sandbox/snaps/dom-animations-05-result.png" />

- [x] **Outcome:** After running, the red square has moved toward the bottom-right (`top`/`left` near **350px**, or mid-travel if the snap is early).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/dom-animations/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why wrap the mover in a container?

<details>
<summary>Answer</summary>

- [x] So `top`/`left` are **relative to that box**, not the whole page.

</details>

### Question 2: Which `position` values does W3Schools require?

<details>
<summary>Answer</summary>

- [x] Container **relative**, animated element **absolute**.

</details>

### Question 3: How is the animation scheduled?

<details>
<summary>Answer</summary>

- [x] **`setInterval(frame, 5)`** — a 5ms timer.

</details>

### Question 4: How do you stop it?

<details>
<summary>Answer</summary>

- [x] **`clearInterval(id)`** when the finish test is true.

</details>

### Question 5: What does `myMove` change each tick?

<details>
<summary>Answer</summary>

- [x] `elem.style.top` and `elem.style.left` by **+1px**.

</details>

### Question 6: Why `pos == 350`?

<details>
<summary>Answer</summary>

- [x] A 50px square in a 400px container travels **350px** before hitting the far edge.

</details>

### Question 7: Why `clearInterval` at the start of `myMove`?

<details>
<summary>Answer</summary>

- [x] So a second click does not start a **second** timer on the same element.

</details>

### Question 8: Is this the CSS `animation` property?

<details>
<summary>Answer</summary>

- [x] No — this page teaches **JavaScript timers** changing inline styles.

</details>

### Question 9: What if the interval is large, like 500ms?

<details>
<summary>Answer</summary>

- [x] The motion looks **jerky**, not continuous.

</details>

### Question 10: Can you animate `opacity` the same way?

<details>
<summary>Answer</summary>

- [x] Yes — any style you can set in JS, changed a little each frame.

</details>


</details>

## Summary

Position the box, then drive `top`/`left` (or any style) from a short interval until you clear it.

## References

- [DOM Animations](https://www.w3schools.com/js/js_htmldom_animate.asp)
- [MDN Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)

</details>
