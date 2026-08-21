# JS Timers

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Timers schedule a function for later: setTimeout once, setInterval repeatedly, and clearTimeout / clearInterval to cancel. They do not pause JavaScript. The delay is a minimum, callbacks still run on the main thread, and you must pass the function name — not a call with parentheses. Extra arguments after the delay go to the callback. This section avoids infinite loops and oversized busy-waits so screenshots can finish.

This section has **17** examples:

- [x] **Example 1:** The four timer functions [View](#js-timers-example-01)
- [x] **Example 2:** setTimeout myFunction 3000 → Hello! [View](#js-timers-example-02)
- [x] **Example 3:** Correct vs incorrect: pass the name, not myFunction() [View](#js-timers-example-03)
- [x] **Example 4:** Anonymous setTimeout 3000 [View](#js-timers-example-04)
- [x] **Example 5:** Start / End / Timer order [View](#js-timers-example-05)
- [x] **Example 6:** Zero delay still Start End Timer [View](#js-timers-example-06)
- [x] **Example 7:** Delay is a minimum (busy loop) [View](#js-timers-example-07)
- [x] **Example 8:** clearTimeout — Timer stopped [View](#js-timers-example-08)
- [x] **Example 9:** setInterval showTime [View](#js-timers-example-09)
- [x] **Example 10:** Start / stop clock (clearInterval) [View](#js-timers-example-10)
- [x] **Example 11:** Passing extra args: setTimeout(showMessage, 2000, "Hello", "John") [View](#js-timers-example-11)
- [x] **Example 12:** Repeated setTimeout (two ticks then stop) [View](#js-timers-example-12)
- [x] **Example 13:** Countdown (auto start) [View](#js-timers-example-13)
- [x] **Example 14:** Avoid strings as timer code [View](#js-timers-example-14)
- [x] **Example 15:** Long callback still blocks the page [View](#js-timers-example-15)
- [x] **Example 16:** Common mistake: calling with () [View](#js-timers-example-16)
- [x] **Example 17:** Slideshow with text labels (nature / snow / mountains) [View](#js-timers-example-17)

## Detailed Explanation

- [x] `setTimeout(fn, ms)` once; `setInterval(fn, ms)` repeat; `clear*` cancel using the returned **id**.
- [x] Timers **do not pause** the rest of the script. Order is **Start End Timer**, even with delay 0.
- [x] Pass **`fn`**, not **`fn()`**. Do not pass a **string** of code.
- [x] The delay is a **minimum**. A busy loop or a long callback still **blocks** the page.

<a id="js-timers-example-01"></a>

### **Example 1: The four timer functions**

- [x] `setTimeout()` runs a function **once** after a delay.
- [x] `setInterval()` runs a function **repeatedly**.
- [x] `clearTimeout()` / `clearInterval()` cancel those timers.

Sandbox: `code_sandbox/js-timers/four-timer-functions.html`

```javascript
setTimeout(fn, ms);
setInterval(fn, ms);
clearTimeout(id);
clearInterval(id);
```

![js-timers example 1 source](../code_sandbox/snaps/js-timers-01-code.png)

![js-timers example 1 result](../code_sandbox/snaps/js-timers-01-result.png)

- [x] **Outcome:** The table is listed. A 0 ms timeout then writes **ready** to show setTimeout works.

<a id="js-timers-example-02"></a>

### **Example 2: setTimeout myFunction 3000 → Hello!**

- [x] `setTimeout(myFunction, 3000)` runs **once** after **3000** ms (3 seconds).
- [x] Pass the **function name**, not `myFunction()`.

Sandbox: `code_sandbox/js-timers/settimeout-hello.html`

```javascript
setTimeout(myFunction, 3000);
function myFunction() {
  myDisplayer("Hello!");
}
```

![js-timers example 2 source](../code_sandbox/snaps/js-timers-02-code.png)

![js-timers example 2 result](../code_sandbox/snaps/js-timers-02-result.png)

- [x] **Outcome:** #demo shows **Hello!** after the delay.

<a id="js-timers-example-03"></a>

### **Example 3: Correct vs incorrect: pass the name, not myFunction()**

- [x] **Correct:** `setTimeout(myFunction, 3000)` — the engine calls it later.
- [x] **Incorrect:** `setTimeout(myFunction(), 3000)` — it runs **immediately**, and `undefined` is passed as the callback.

Sandbox: `code_sandbox/js-timers/pass-name-vs-call.html`

```javascript
setTimeout(myFunction, 3000); // correct
setTimeout(myFunction(), 3000); // incorrect — runs now
```

![js-timers example 3 source](../code_sandbox/snaps/js-timers-03-code.png)

![js-timers example 3 result](../code_sandbox/snaps/js-timers-03-result.png)

- [x] **Outcome:** The incorrect call runs **immediately**. The correct call would wait.

<a id="js-timers-example-04"></a>

### **Example 4: Anonymous setTimeout 3000**

- [x] You can pass an **anonymous** function as the callback.

Sandbox: `code_sandbox/js-timers/anonymous-timeout.html`

```javascript
setTimeout(function () {
  myDisplayer("Hello!");
}, 3000);
```

![js-timers example 4 source](../code_sandbox/snaps/js-timers-04-code.png)

![js-timers example 4 result](../code_sandbox/snaps/js-timers-04-result.png)

- [x] **Outcome:** #demo shows **Hello!**.

<a id="js-timers-example-05"></a>

### **Example 5: Start / End / Timer order**

- [x] `setTimeout` does **not** pause JavaScript.
- [x] The next statement runs immediately, so the order is **Start End Timer**.

Sandbox: `code_sandbox/js-timers/start-end-timer.html`

```javascript
myDisplayer("Start");
setTimeout(function () {
  myDisplayer("Timer");
}, 3000);
myDisplayer("End");
```

![js-timers example 5 source](../code_sandbox/snaps/js-timers-05-code.png)

![js-timers example 5 result](../code_sandbox/snaps/js-timers-05-result.png)

- [x] **Outcome:** Final accumulated order: **Start End Timer**.

<a id="js-timers-example-06"></a>

### **Example 6: Zero delay still Start End Timer**

- [x] A delay of **0** does not mean “run now”.
- [x] The callback waits until the **current task** finishes, so you still get **Start End Timer**.

Sandbox: `code_sandbox/js-timers/zero-delay.html`

```javascript
myDisplayer("Start");
setTimeout(function () {
  myDisplayer("Timer");
}, 0);
myDisplayer("End");
```

![js-timers example 6 source](../code_sandbox/snaps/js-timers-06-code.png)

![js-timers example 6 result](../code_sandbox/snaps/js-timers-06-result.png)

- [x] **Outcome:** Order is still **Start End Timer**.

<a id="js-timers-example-07"></a>

### **Example 7: Delay is a minimum (busy loop)**

- [x] The delay is the **earliest** the callback may run.
- [x] The W3Schools page uses `let i = 4e9` (too slow for a screenshot). This demo uses **`4e7`** so the snap can finish.

Sandbox: `code_sandbox/js-timers/delay-is-minimum.html`

```javascript
setTimeout(function () {
  myDisplayer("Timer finished");
}, 1000);
let i = 4e7; // page used 4e9
while (--i > 0);
```

![js-timers example 7 source](../code_sandbox/snaps/js-timers-07-code.png)

![js-timers example 7 result](../code_sandbox/snaps/js-timers-07-result.png)

- [x] **Outcome:** After the loop, #demo shows **Timer finished**. The callback waited for the busy loop, not just 1000 ms.

<a id="js-timers-example-08"></a>

### **Example 8: clearTimeout — Timer stopped**

- [x] `setTimeout` returns an **id**. Pass it to `clearTimeout` to cancel.
- [x] This demo auto-starts then auto-stops so the snap shows **Timer stopped**.

Sandbox: `code_sandbox/js-timers/cleartimeout.html`

```javascript
let timer;
function startTimer() {
  timer = setTimeout(function () {
    document.getElementById("demo").innerHTML = "Finished";
  }, 5000);
}
function stopTimer() {
  clearTimeout(timer);
  document.getElementById("demo").innerHTML = "Timer stopped";
}
```

![js-timers example 8 source](../code_sandbox/snaps/js-timers-08-code.png)

![js-timers example 8 result](../code_sandbox/snaps/js-timers-08-result.png)

- [x] **Outcome:** #demo shows **Timer stopped** (the 5 s timeout never finished).

<a id="js-timers-example-09"></a>

### **Example 9: setInterval showTime**

- [x] `setInterval(showTime, 1000)` runs **every second**.
- [x] Unlike `setTimeout`, it keeps repeating until you clear it.

Sandbox: `code_sandbox/js-timers/setinterval-showtime.html`

```javascript
setInterval(showTime, 1000);
function showTime() {
  const date = new Date();
  myDisplayer(date.toLocaleTimeString());
}
```

![js-timers example 9 source](../code_sandbox/snaps/js-timers-09-code.png)

![js-timers example 9 result](../code_sandbox/snaps/js-timers-09-result.png)

- [x] **Outcome:** A clock time appears in #demo.

<a id="js-timers-example-10"></a>

### **Example 10: Start / stop clock (clearInterval)**

- [x] `setInterval` returns an id. `clearInterval` **stops** it.
- [x] Guard with `if (!timer)` so you do not start **multiple** intervals.
- [x] Auto-started so the snap shows a time.

Sandbox: `code_sandbox/js-timers/start-stop-clock.html`

```javascript
let timer;
function startClock() {
  if (!timer) {
    timer = setInterval(showTime, 1000);
  }
}
function showTime() {
  const date = new Date();
  document.getElementById("demo").innerHTML = date.toLocaleTimeString();
}
function stopClock() {
  clearInterval(timer);
  timer = undefined;
}
```

![js-timers example 10 source](../code_sandbox/snaps/js-timers-10-code.png)

![js-timers example 10 result](../code_sandbox/snaps/js-timers-10-result.png)

- [x] **Outcome:** The clock is running; Stop Clock would call `clearInterval`.

<a id="js-timers-example-11"></a>

### **Example 11: Passing extra args: setTimeout(showMessage, 2000, "Hello", "John")**

- [x] Extra arguments after the delay are passed **into the callback**.
- [x] `setTimeout(showMessage, 2000, "Hello", "John")` → greeting and name.

Sandbox: `code_sandbox/js-timers/passing-extra-args.html`

```javascript
setTimeout(showMessage, 2000, "Hello", "John");
function showMessage(greeting, name) {
  document.getElementById("demo").innerHTML = greeting + " " + name;
}
```

![js-timers example 11 source](../code_sandbox/snaps/js-timers-11-code.png)

![js-timers example 11 result](../code_sandbox/snaps/js-timers-11-result.png)

- [x] **Outcome:** #demo shows **Hello John**.

<a id="js-timers-example-12"></a>

### **Example 12: Repeated setTimeout (two ticks then stop)**

- [x] Call `setTimeout` again from the callback to **repeat after the work finishes**.
- [x] This demo runs **2 ticks** then stops so the screenshot does not loop forever.

Sandbox: `code_sandbox/js-timers/repeated-settimeout.html`

```javascript
function repeat() {
  myDisplayer("Hello");
  setTimeout(repeat, 1000);
}
repeat();
```

![js-timers example 12 source](../code_sandbox/snaps/js-timers-12-code.png)

![js-timers example 12 result](../code_sandbox/snaps/js-timers-12-result.png)

- [x] **Outcome:** #demo shows **Hello (tick 2)** after two runs, then stops.

<a id="js-timers-example-13"></a>

### **Example 13: Countdown (auto start)**

- [x] A countdown uses `setInterval`, then `clearInterval` at **0**.
- [x] Auto-started so the snap shows a **decreased** count.

Sandbox: `code_sandbox/js-timers/countdown.html`

```javascript
let timer;
function startCountdown() {
  clearInterval(timer);
  let count = 10;
  myDisplayer(count);
  timer = setInterval(function () {
    count--;
    myDisplayer(count);
    if (count === 0) {
      clearInterval(timer);
      myDisplayer("Finished!");
    }
  }, 1000);
}
```

![js-timers example 13 source](../code_sandbox/snaps/js-timers-13-code.png)

![js-timers example 13 result](../code_sandbox/snaps/js-timers-13-result.png)

- [x] **Outcome:** Count has decreased from 10 (about 6 after ~4 s of virtual time).

<a id="js-timers-example-14"></a>

### **Example 14: Avoid strings as timer code**

- [x] **Not recommended:** `setTimeout("myFunction()", 1000)` — the engine `eval`s a string.
- [x] **Recommended:** `setTimeout(myFunction, 1000)` — pass the function. Safer, clearer, easier to debug (and CSP-friendly).
- [x] Both forms can run the function; the string form is still a bad habit.

Sandbox: `code_sandbox/js-timers/avoid-strings.html`

```javascript
setTimeout("myFunction()", 1000); // not recommended
setTimeout(myFunction, 1000); // recommended
```

![js-timers example 14 source](../code_sandbox/snaps/js-timers-14-code.png)

![js-timers example 14 result](../code_sandbox/snaps/js-timers-14-result.png)

- [x] **Outcome:** Both callbacks run `myFunction`. Prefer the function reference.

<a id="js-timers-example-15"></a>

### **Example 15: Long callback still blocks the page**

- [x] The delay only postpones **when** the callback starts.
- [x] Once it starts, a long loop still **freezes** the page. Demo uses **`4e7`**, not the page's `4e9`.

Sandbox: `code_sandbox/js-timers/long-callback-blocks.html`

```javascript
setTimeout(function () {
  let i = 4e7; // page used 4e9
  while (--i > 0);
  document.getElementById("demo").innerHTML = "Finished";
}, 1000);
```

![js-timers example 15 source](../code_sandbox/snaps/js-timers-15-code.png)

![js-timers example 15 result](../code_sandbox/snaps/js-timers-15-result.png)

- [x] **Outcome:** #demo shows **Finished** after the delayed (smaller) loop.

<a id="js-timers-example-16"></a>

### **Example 16: Common mistake: calling with ()**

- [x] `setTimeout(myFunction(), 1000)` invokes the function **now**.
- [x] Remove the parentheses: `setTimeout(myFunction, 1000)`.

Sandbox: `code_sandbox/js-timers/mistake-call-with-parens.html`

```javascript
setTimeout(myFunction(), 1000); // wrong
setTimeout(myFunction, 1000); // right
```

![js-timers example 16 source](../code_sandbox/snaps/js-timers-16-code.png)

![js-timers example 16 result](../code_sandbox/snaps/js-timers-16-result.png)

- [x] **Outcome:** Wrong form: **ran immediately**. Right form waits.

<a id="js-timers-example-17"></a>

### **Example 17: Slideshow with text labels (nature / snow / mountains)**

- [x] W3Schools cycles images every 3 s. This demo cycles **text labels** — no external images.
- [x] Auto-started. `%` wraps the index after the last slide. `if (!timer)` prevents duplicate intervals.

Sandbox: `code_sandbox/js-timers/slideshow-text.html`

```javascript
const images = ["nature", "snow", "mountains"];
let index = 0;
let timer;
function showNextSlide() {
  index = (index + 1) % images.length;
  document.getElementById("slide").textContent = images[index];
}
function startSlides() {
  if (!timer) {
    timer = setInterval(showNextSlide, 1000);
  }
}
```

![js-timers example 17 source](../code_sandbox/snaps/js-timers-17-code.png)

![js-timers example 17 result](../code_sandbox/snaps/js-timers-17-result.png)

- [x] **Outcome:** The label cycles **nature → snow → mountains**. Interval here is **1000** ms so the snap shows a change (the page used **3000** ms).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-timers/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `setTimeout(myFunction, 3000)` show after 3 s?

<details>
<summary>Answer</summary>

- [x] **Hello!**

</details>

### Question 2: Why is `setTimeout(myFunction(), 3000)` wrong?

<details>
<summary>Answer</summary>

- [x] It **calls immediately**. `undefined` is scheduled as the callback.

</details>

### Question 3: What is the order of Start, setTimeout 3000, End?

<details>
<summary>Answer</summary>

- [x] **Start End Timer** — timeout does not pause the script.

</details>

### Question 4: What if the delay is 0?

<details>
<summary>Answer</summary>

- [x] Still **Start End Timer**. Zero means “as soon as this task finishes”, not “now”.

</details>

### Question 5: Is the delay exact?

<details>
<summary>Answer</summary>

- [x] It is a **minimum**. A busy loop can make the callback late.
- [x] This demo used **4e7**, not the page’s **4e9**.

</details>

### Question 6: How do you cancel a timeout?

<details>
<summary>Answer</summary>

- [x] Save the id, then **`clearTimeout(id)`**. This snap shows **Timer stopped**.

</details>

### Question 7: What does `setInterval(showTime, 1000)` do?

<details>
<summary>Answer</summary>

- [x] Updates a clock about **every second** until cleared.

</details>

### Question 8: How do you stop an interval?

<details>
<summary>Answer</summary>

- [x] **`clearInterval(id)`**. Guard `if (!timer)` so you do not start two of them.

</details>

### Question 9: What does `setTimeout(showMessage, 2000, "Hello", "John")` show?

<details>
<summary>Answer</summary>

- [x] **Hello John** — extra args are passed to the callback.

</details>

### Question 10: Repeated `setTimeout` vs `setInterval`?

<details>
<summary>Answer</summary>

- [x] Repeated timeout waits until the **callback finishes** before scheduling the next delay.
- [x] Interval keeps a fixed schedule.

</details>

### Question 11: Why avoid `setTimeout("myFunction()", 1000)`?

<details>
<summary>Answer</summary>

- [x] It **eval**s a string: harder to debug, worse for CSP, no closure of locals.
- [x] Pass the **function** instead.

</details>

### Question 12: Does a timer run the callback off the main thread?

<details>
<summary>Answer</summary>

- [x] **No.** Waiting is outside JS; the callback still **blocks** the page when it runs.

</details>

### Question 13: What wraps a slideshow index?

<details>
<summary>Answer</summary>

- [x] **`index = (index + 1) % images.length`**.
- [x] This demo cycles **nature / snow / mountains** as text, not remote images.

</details>

### Question 14: What are the four timer functions?

<details>
<summary>Answer</summary>

- [x] **setTimeout**, **setInterval**, **clearTimeout**, **clearInterval**.

</details>

</details>

## Summary

Schedule work with setTimeout and setInterval, cancel with the matching clear function, pass the function rather than calling it, and treat delays as minimums. Extra arguments after the delay go to the callback. Keep callbacks short so the page stays responsive.

## References

- [JS Timers (W3Schools)](https://www.w3schools.com/js/js_timers.asp)
- [MDN: setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)
- [MDN: setInterval](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)
- [MDN: clearTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearTimeout)
- [MDN: clearInterval](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearInterval)
