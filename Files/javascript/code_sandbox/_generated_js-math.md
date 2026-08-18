<details>
  <summary>JS Math</summary>

## Introduction

Math is a static object: call Math.PI and Math.method(x) without constructing it. Eight constants cover e, π, roots, and log bases. round / ceil / floor / trunc convert to integers differently (especially on negatives). Trigonometry is in radians (degrees * PI / 180). min and max take an argument list. random is a sample in [0, 1). log is natural log; log2 and log10 are the named bases.

This section has **23** examples:

- [x] **Example 1:** Math.PI [View](#js-math-example-01)
- [x] **Example 2:** Eight Math constant properties [View](#js-math-example-02)
- [x] **Example 3:** Math.round(4.6) [View](#js-math-example-03)
- [x] **Example 4:** Math.round(4.5) [View](#js-math-example-04)
- [x] **Example 5:** Math.round(4.4) [View](#js-math-example-05)
- [x] **Example 6:** Math.ceil — round toward +∞ [View](#js-math-example-06)
- [x] **Example 7:** Math.floor — round toward −∞ [View](#js-math-example-07)
- [x] **Example 8:** Math.trunc — integer part [View](#js-math-example-08)
- [x] **Example 9:** Math.sign — −1 / 0 / 1 [View](#js-math-example-09)
- [x] **Example 10:** Math.pow(8, 2) [View](#js-math-example-10)
- [x] **Example 11:** Math.sqrt(64) [View](#js-math-example-11)
- [x] **Example 12:** Math.abs(-4.7) [View](#js-math-example-12)
- [x] **Example 13:** Math.sin(90°) via radians [View](#js-math-example-13)
- [x] **Example 14:** Math.cos(0°) via radians [View](#js-math-example-14)
- [x] **Example 15:** Math.min(0, 150, 30, 20, -8, -200) [View](#js-math-example-15)
- [x] **Example 16:** Math.max(0, 150, 30, 20, -8, -200) [View](#js-math-example-16)
- [x] **Example 17:** Math.random() — sample in [0, 1) [View](#js-math-example-17)
- [x] **Example 18:** Math.log(1) — natural log [View](#js-math-example-18)
- [x] **Example 19:** Math.log(2) [View](#js-math-example-19)
- [x] **Example 20:** Math.log(3) [View](#js-math-example-20)
- [x] **Example 21:** Math.log(10) — times to multiply e to get 10 [View](#js-math-example-21)
- [x] **Example 22:** Math.log2(8) [View](#js-math-example-22)
- [x] **Example 23:** Math.log10(1000) [View](#js-math-example-23)

## Detailed Explanation

- [x] **`Math` is static** — no `new Math()`.
- [x] **8 constants:** E, PI, SQRT2, SQRT1_2, LN2, LN10, LOG2E, LOG10E.
- [x] **Integers:** `round` nearest, `ceil` toward +∞, `floor` toward −∞, `trunc` toward 0. **`sign`** is −1 / 0 / 1.
- [x] **Trig in radians.** `sin(90 * PI/180)` is **1**.
- [x] `min` / `max` take a **list of arguments**. `random()` ∈ **[0, 1)**.
- [x] `log` is **ln**. `log2(8)` is **3**. `log10(1000)` is **3**.

<a id="js-math-example-01"></a>

### **Example 1: Math.PI**

- [x] `Math` is **static** — you never `new Math()`. Call properties on **`Math` itself**.
- [x] `Math.PI` is the circle constant **π**.

Sandbox: `code_sandbox/js-math/math-pi.html`

```javascript
Math.PI;
```

<img alt="js-math example 1 source" src="./code_sandbox/snaps/js-math-01-code.png" />

<img alt="js-math example 1 result" src="./code_sandbox/snaps/js-math-01-result.png" />

- [x] **Outcome:** `Math.PI` is **3.141592653589793**.

<a id="js-math-example-02"></a>

### **Example 2: Eight Math constant properties**

- [x] JavaScript exposes **8** constants: `E`, `PI`, `SQRT2`, `SQRT1_2`, `LN2`, `LN10`, `LOG2E`, `LOG10E`.
- [x] One Tryit prints all eight — keep them together (the **reference** page splits them per row).

Sandbox: `code_sandbox/js-math/math-constants.html`

```javascript
Math.E;
Math.PI;
Math.SQRT2;
Math.SQRT1_2;
Math.LN2;
Math.LN10;
Math.LOG2E;
Math.LOG10E;
```

<img alt="js-math example 2 source" src="./code_sandbox/snaps/js-math-02-code.png" />

<img alt="js-math example 2 result" src="./code_sandbox/snaps/js-math-02-result.png" />

- [x] **Outcome:** **E** 2.718281828459045, **PI** 3.141592653589793, **SQRT2** 1.4142135623730951, **SQRT1_2** 0.7071067811865476, **LN2** 0.6931471805599453, **LN10** 2.302585092994046, **LOG2E** 1.4426950408889634, **LOG10E** 0.4342944819032518.

<a id="js-math-example-03"></a>

### **Example 3: Math.round(4.6)**

- [x] `Math.round(x)` is the **nearest** integer (half rounds **away from 0** toward **+∞** for positives).

Sandbox: `code_sandbox/js-math/round-4-6.html`

```javascript
Math.round(4.6);
```

<img alt="js-math example 3 source" src="./code_sandbox/snaps/js-math-03-code.png" />

<img alt="js-math example 3 result" src="./code_sandbox/snaps/js-math-03-result.png" />

- [x] **Outcome:** **5**.

<a id="js-math-example-04"></a>

### **Example 4: Math.round(4.5)**

- [x] **4.5** is exactly halfway. Positive halves round **up** to **5**.

Sandbox: `code_sandbox/js-math/round-4-5.html`

```javascript
Math.round(4.5);
```

<img alt="js-math example 4 source" src="./code_sandbox/snaps/js-math-04-code.png" />

<img alt="js-math example 4 result" src="./code_sandbox/snaps/js-math-04-result.png" />

- [x] **Outcome:** **5**.

<a id="js-math-example-05"></a>

### **Example 5: Math.round(4.4)**

- [x] 4.4 is closer to **4** than to 5.

Sandbox: `code_sandbox/js-math/round-4-4.html`

```javascript
Math.round(4.4);
```

<img alt="js-math example 5 source" src="./code_sandbox/snaps/js-math-05-code.png" />

<img alt="js-math example 5 result" src="./code_sandbox/snaps/js-math-05-result.png" />

- [x] **Outcome:** **4**.

<a id="js-math-example-06"></a>

### **Example 6: Math.ceil — round toward +∞**

- [x] `Math.ceil(x)` rounds **up** (toward **+∞**). Negative values move toward zero’s less-negative integer.
- [x] Tryit uses `4.4`; the Example listing also has 4.9, 4.7, 4.2, and −4.2.

Sandbox: `code_sandbox/js-math/ceil.html`

```javascript
Math.ceil(4.4);
```

<img alt="js-math example 6 source" src="./code_sandbox/snaps/js-math-06-code.png" />

<img alt="js-math example 6 result" src="./code_sandbox/snaps/js-math-06-result.png" />

- [x] **Outcome:** 4.4 / 4.9 / 4.7 / 4.2 → **5**. **−4.2 → −4** (up toward +∞, not away from zero).

<a id="js-math-example-07"></a>

### **Example 7: Math.floor — round toward −∞**

- [x] `Math.floor(x)` rounds **down** (toward **−∞**).
- [x] Tryit uses `4.7`; the listing also has 4.9, 4.4, 4.2, and −4.2.

Sandbox: `code_sandbox/js-math/floor.html`

```javascript
Math.floor(4.7);
```

<img alt="js-math example 7 source" src="./code_sandbox/snaps/js-math-07-code.png" />

<img alt="js-math example 7 result" src="./code_sandbox/snaps/js-math-07-result.png" />

- [x] **Outcome:** Positive values → **4**. **−4.2 → −5** (down, more negative).

<a id="js-math-example-08"></a>

### **Example 8: Math.trunc — integer part**

- [x] `Math.trunc(x)` drops the fraction (**toward 0**). ES6.
- [x] Unlike `floor`, **−4.2** becomes **−4**, not −5.

Sandbox: `code_sandbox/js-math/trunc.html`

```javascript
Math.trunc(4.7);
```

<img alt="js-math example 8 source" src="./code_sandbox/snaps/js-math-08-code.png" />

<img alt="js-math example 8 result" src="./code_sandbox/snaps/js-math-08-result.png" />

- [x] **Outcome:** Positives → **4**. **−4.2 → −4**.

<a id="js-math-example-09"></a>

### **Example 9: Math.sign — −1 / 0 / 1**

- [x] `Math.sign(x)` is **1** (positive), **−1** (negative), or **0** (zero). ES6.
- [x] Tryit uses `Math.sign(4)`; the listing also has −4 and 0.

Sandbox: `code_sandbox/js-math/sign.html`

```javascript
Math.sign(4);
```

<img alt="js-math example 9 source" src="./code_sandbox/snaps/js-math-09-code.png" />

<img alt="js-math example 9 result" src="./code_sandbox/snaps/js-math-09-result.png" />

- [x] **Outcome:** **1**, **−1**, and **0**.

<a id="js-math-example-10"></a>

### **Example 10: Math.pow(8, 2)**

- [x] `Math.pow(x, y)` is **x to the power y**. Same idea as `x ** y`.

Sandbox: `code_sandbox/js-math/pow.html`

```javascript
Math.pow(8, 2);
```

<img alt="js-math example 10 source" src="./code_sandbox/snaps/js-math-10-code.png" />

<img alt="js-math example 10 result" src="./code_sandbox/snaps/js-math-10-result.png" />

- [x] **Outcome:** **64**.

<a id="js-math-example-11"></a>

### **Example 11: Math.sqrt(64)**

- [x] `Math.sqrt(x)` is the **square root**.

Sandbox: `code_sandbox/js-math/sqrt.html`

```javascript
Math.sqrt(64);
```

<img alt="js-math example 11 source" src="./code_sandbox/snaps/js-math-11-code.png" />

<img alt="js-math example 11 result" src="./code_sandbox/snaps/js-math-11-result.png" />

- [x] **Outcome:** **8**.

<a id="js-math-example-12"></a>

### **Example 12: Math.abs(-4.7)**

- [x] `Math.abs(x)` is the **absolute** (non-negative) value.

Sandbox: `code_sandbox/js-math/abs.html`

```javascript
Math.abs(-4.7);
```

<img alt="js-math example 12 source" src="./code_sandbox/snaps/js-math-12-code.png" />

<img alt="js-math example 12 result" src="./code_sandbox/snaps/js-math-12-result.png" />

- [x] **Outcome:** **4.7**.

<a id="js-math-example-13"></a>

### **Example 13: Math.sin(90°) via radians**

- [x] `Math.sin(x)` uses **radians**, not degrees.
- [x] Degrees → radians: **`degrees * Math.PI / 180`**.

Sandbox: `code_sandbox/js-math/sin-90deg.html`

```javascript
Math.sin(90 * Math.PI / 180);
```

<img alt="js-math example 13 source" src="./code_sandbox/snaps/js-math-13-code.png" />

<img alt="js-math example 13 result" src="./code_sandbox/snaps/js-math-13-result.png" />

- [x] **Outcome:** **1** (sine of 90°).

<a id="js-math-example-14"></a>

### **Example 14: Math.cos(0°) via radians**

- [x] `Math.cos(x)` is also in **radians**. 0° is **0** radians.

Sandbox: `code_sandbox/js-math/cos-0deg.html`

```javascript
Math.cos(0 * Math.PI / 180);
```

<img alt="js-math example 14 source" src="./code_sandbox/snaps/js-math-14-code.png" />

<img alt="js-math example 14 result" src="./code_sandbox/snaps/js-math-14-result.png" />

- [x] **Outcome:** **1** (cosine of 0°).

<a id="js-math-example-15"></a>

### **Example 15: Math.min(0, 150, 30, 20, -8, -200)**

- [x] `Math.min(...)` is the **lowest** argument (not an array — pass a list).

Sandbox: `code_sandbox/js-math/min.html`

```javascript
Math.min(0, 150, 30, 20, -8, -200);
```

<img alt="js-math example 15 source" src="./code_sandbox/snaps/js-math-15-code.png" />

<img alt="js-math example 15 result" src="./code_sandbox/snaps/js-math-15-result.png" />

- [x] **Outcome:** **-200**.

<a id="js-math-example-16"></a>

### **Example 16: Math.max(0, 150, 30, 20, -8, -200)**

- [x] `Math.max(...)` is the **highest** argument.

Sandbox: `code_sandbox/js-math/max.html`

```javascript
Math.max(0, 150, 30, 20, -8, -200);
```

<img alt="js-math example 16 source" src="./code_sandbox/snaps/js-math-16-code.png" />

<img alt="js-math example 16 result" src="./code_sandbox/snaps/js-math-16-result.png" />

- [x] **Outcome:** **150**.

<a id="js-math-example-17"></a>

### **Example 17: Math.random() — sample in [0, 1)**

- [x] `Math.random()` is **≥ 0** and **< 1**. It is **not** an integer.
- [x] Each run is a new sample. The snap is one draw, not a constant.

Sandbox: `code_sandbox/js-math/random.html`

```javascript
Math.random();
```

<img alt="js-math example 17 source" src="./code_sandbox/snaps/js-math-17-code.png" />

<img alt="js-math example 17 result" src="./code_sandbox/snaps/js-math-17-result.png" />

- [x] **Outcome:** The snap shows a **sample** in **[0, 1)**. Re-run for another value. Never **1**. The boolean check on a second draw is **true**.

<a id="js-math-example-18"></a>

### **Example 18: Math.log(1) — natural log**

- [x] `Math.log(x)` is **ln(x)** (base **e**). `Math.log(1)` is **0** because e⁰ = 1.

Sandbox: `code_sandbox/js-math/log-1.html`

```javascript
Math.log(1);
```

<img alt="js-math example 18 source" src="./code_sandbox/snaps/js-math-18-code.png" />

<img alt="js-math example 18 result" src="./code_sandbox/snaps/js-math-18-result.png" />

- [x] **Outcome:** **0**.

<a id="js-math-example-19"></a>

### **Example 19: Math.log(2)**

- [x] `Math.log(2)` is **ln(2)** — the same value as **`Math.LN2`**.

Sandbox: `code_sandbox/js-math/log-2.html`

```javascript
Math.log(2);
```

<img alt="js-math example 19 source" src="./code_sandbox/snaps/js-math-19-code.png" />

<img alt="js-math example 19 result" src="./code_sandbox/snaps/js-math-19-result.png" />

- [x] **Outcome:** **0.6931471805599453** (equals `Math.LN2`).

<a id="js-math-example-20"></a>

### **Example 20: Math.log(3)**

- [x] Natural log of 3 — how many times to multiply **e** to get 3.

Sandbox: `code_sandbox/js-math/log-3.html`

```javascript
Math.log(3);
```

<img alt="js-math example 20 source" src="./code_sandbox/snaps/js-math-20-code.png" />

<img alt="js-math example 20 result" src="./code_sandbox/snaps/js-math-20-result.png" />

- [x] **Outcome:** **1.0986122886681096**.

<a id="js-math-example-21"></a>

### **Example 21: Math.log(10) — times to multiply e to get 10**

- [x] The page asks: how many times must we multiply **`Math.E`** to get **10**?
- [x] That is **ln(10)**, also **`Math.LN10`**.

Sandbox: `code_sandbox/js-math/log-10.html`

```javascript
Math.log(10);
```

<img alt="js-math example 21 source" src="./code_sandbox/snaps/js-math-21-code.png" />

<img alt="js-math example 21 result" src="./code_sandbox/snaps/js-math-21-result.png" />

- [x] **Outcome:** **2.302585092994046** (equals `Math.LN10`).

<a id="js-math-example-22"></a>

### **Example 22: Math.log2(8)**

- [x] `Math.log2(x)` is log base **2**. How many times to multiply **2** to get **8**?

Sandbox: `code_sandbox/js-math/log2-8.html`

```javascript
Math.log2(8);
```

<img alt="js-math example 22 source" src="./code_sandbox/snaps/js-math-22-code.png" />

<img alt="js-math example 22 result" src="./code_sandbox/snaps/js-math-22-result.png" />

- [x] **Outcome:** **3** (2³ = 8).

<a id="js-math-example-23"></a>

### **Example 23: Math.log10(1000)**

- [x] `Math.log10(x)` is log base **10**. How many times to multiply **10** to get **1000**?

Sandbox: `code_sandbox/js-math/log10-1000.html`

```javascript
Math.log10(1000);
```

<img alt="js-math example 23 source" src="./code_sandbox/snaps/js-math-23-code.png" />

<img alt="js-math example 23 result" src="./code_sandbox/snaps/js-math-23-result.png" />

- [x] **Outcome:** **3** (10³ = 1000).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-math/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Do you write `new Math()`?

<details>
<summary>Answer</summary>

- [x] **No.** All properties are **static** on `Math`.

</details>

### Question 2: What is `Math.PI`?

<details>
<summary>Answer</summary>

- [x] **3.141592653589793**.

</details>

### Question 3: What are the eight constants?

<details>
<summary>Answer</summary>

- [x] **E, PI, SQRT2, SQRT1_2, LN2, LN10, LOG2E, LOG10E**.

</details>

### Question 4: `Math.round(4.6)`, `(4.5)`, `(4.4)`?

<details>
<summary>Answer</summary>

- [x] **5**, **5**, **4**.

</details>

### Question 5: `Math.ceil(-4.2)` vs `Math.floor(-4.2)` vs `Math.trunc(-4.2)`?

<details>
<summary>Answer</summary>

- [x] ceil **−4**, floor **−5**, trunc **−4**.

</details>

### Question 6: What is `Math.sign(-4)`?

<details>
<summary>Answer</summary>

- [x] **−1**. Zero → **0**. Positive → **1**.

</details>

### Question 7: `Math.pow(8,2)` and `Math.sqrt(64)`?

<details>
<summary>Answer</summary>

- [x] **64** and **8**.

</details>

### Question 8: How do you take sine of 90 degrees?

<details>
<summary>Answer</summary>

- [x] `Math.sin(90 * Math.PI / 180)` → **1**.

</details>

### Question 9: `Math.min` / `Math.max` of `0, 150, 30, 20, -8, -200`?

<details>
<summary>Answer</summary>

- [x] min **−200**, max **150**.

</details>

### Question 10: What range is `Math.random()`?

<details>
<summary>Answer</summary>

- [x] **[0, 1)** — the snap is a sample, never **1**.

</details>

### Question 11: `Math.log(1)` and `Math.log(10)`?

<details>
<summary>Answer</summary>

- [x] **0** and **2.302585092994046** (`LN10`).

</details>

### Question 12: `Math.log2(8)` and `Math.log10(1000)`?

<details>
<summary>Answer</summary>

- [x] **3** and **3**.

</details>


</details>

## Summary

Use Math without constructing it. Pick round/ceil/floor/trunc by rounding direction. Convert degrees to radians for sin/cos. min/max take a list. random is [0, 1). log is ln; use log2/log10 for those bases.

## References

- [JS Math (W3Schools)](https://www.w3schools.com/js/js_math.asp)
- [MDN: Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
- [MDN: Math.random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)

</details>
