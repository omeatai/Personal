# JS Math Reference

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

The Math reference table (revised July 2025) lists every constant and method as its own row. Each row is its own Example with a real return value. f16round is IEEE binary16 rounding — the table’s “rounded downwards to the nearest integer” text is incorrect (that is floor). hypot and imul are standard Math methods that are not on this table; they still each get an Example. random remains a [0, 1) sample.

This section has **44** examples:

- [x] **Example 1:** Math.abs(-4.7) [View](#js-math-reference-example-01)
- [x] **Example 2:** Math.acos(0.5) [View](#js-math-reference-example-02)
- [x] **Example 3:** Math.acosh(2) [View](#js-math-reference-example-03)
- [x] **Example 4:** Math.asin(0.5) [View](#js-math-reference-example-04)
- [x] **Example 5:** Math.asinh(1) [View](#js-math-reference-example-05)
- [x] **Example 6:** Math.atan(1) [View](#js-math-reference-example-06)
- [x] **Example 7:** Math.atan2(8, 4) [View](#js-math-reference-example-07)
- [x] **Example 8:** Math.atanh(0.5) [View](#js-math-reference-example-08)
- [x] **Example 9:** Math.cbrt(8) [View](#js-math-reference-example-09)
- [x] **Example 10:** Math.ceil(4.4) [View](#js-math-reference-example-10)
- [x] **Example 11:** Math.clz32(1) [View](#js-math-reference-example-11)
- [x] **Example 12:** Math.cos(0) [View](#js-math-reference-example-12)
- [x] **Example 13:** Math.cosh(0) [View](#js-math-reference-example-13)
- [x] **Example 14:** Math.E [View](#js-math-reference-example-14)
- [x] **Example 15:** Math.exp(1) [View](#js-math-reference-example-15)
- [x] **Example 16:** Math.expm1(1) [View](#js-math-reference-example-16)
- [x] **Example 17:** Math.f16round(1.337) [View](#js-math-reference-example-17)
- [x] **Example 18:** Math.floor(4.7) [View](#js-math-reference-example-18)
- [x] **Example 19:** Math.fround(1.337) [View](#js-math-reference-example-19)
- [x] **Example 20:** Math.LN2 [View](#js-math-reference-example-20)
- [x] **Example 21:** Math.LN10 [View](#js-math-reference-example-21)
- [x] **Example 22:** Math.log(2) [View](#js-math-reference-example-22)
- [x] **Example 23:** Math.log10(1000) [View](#js-math-reference-example-23)
- [x] **Example 24:** Math.LOG10E [View](#js-math-reference-example-24)
- [x] **Example 25:** Math.log1p(1) [View](#js-math-reference-example-25)
- [x] **Example 26:** Math.log2(8) [View](#js-math-reference-example-26)
- [x] **Example 27:** Math.LOG2E [View](#js-math-reference-example-27)
- [x] **Example 28:** Math.max(0, 150, 30, 20, -8, -200) [View](#js-math-reference-example-28)
- [x] **Example 29:** Math.min(0, 150, 30, 20, -8, -200) [View](#js-math-reference-example-29)
- [x] **Example 30:** Math.PI [View](#js-math-reference-example-30)
- [x] **Example 31:** Math.pow(8, 2) [View](#js-math-reference-example-31)
- [x] **Example 32:** Math.random() [View](#js-math-reference-example-32)
- [x] **Example 33:** Math.round(4.5) [View](#js-math-reference-example-33)
- [x] **Example 34:** Math.sign(-4) [View](#js-math-reference-example-34)
- [x] **Example 35:** Math.sin(Math.PI / 2) [View](#js-math-reference-example-35)
- [x] **Example 36:** Math.sinh(1) [View](#js-math-reference-example-36)
- [x] **Example 37:** Math.sqrt(64) [View](#js-math-reference-example-37)
- [x] **Example 38:** Math.SQRT1_2 [View](#js-math-reference-example-38)
- [x] **Example 39:** Math.SQRT2 [View](#js-math-reference-example-39)
- [x] **Example 40:** Math.tan(Math.PI / 4) [View](#js-math-reference-example-40)
- [x] **Example 41:** Math.tanh(1) [View](#js-math-reference-example-41)
- [x] **Example 42:** Math.trunc(4.7) [View](#js-math-reference-example-42)
- [x] **Example 43:** Math.hypot(3, 4) — extra (not on the July 2025 table) [View](#js-math-reference-example-43)
- [x] **Example 44:** Math.imul(2, 4) — extra (not on the July 2025 table) [View](#js-math-reference-example-44)

## Detailed Explanation

- [x] **Every table row is an Example** — constants and methods, not a bullet list of names.
- [x] Live table (July 2025): abs through trunc as listed on the page, including **E, LN2, LN10, LOG2E, LOG10E, PI, SQRT1_2, SQRT2** and **f16round / fround / clz32**.
- [x] **`f16round(1.337)` is 1.3369140625**, not an integer. The W3Schools description copies `floor` by mistake.
- [x] **`tan(π/4)` is 0.9999999999999999** (π is approximate), not exactly 1.
- [x] **`hypot` and `imul`** are extra (not on the live table) because they are standard `Math` methods named in the task list.

<a id="js-math-reference-example-01"></a>

### **Example 1: Math.abs(-4.7)**

- [x] `Math.abs(-4.7)` returns the absolute value of x.

Sandbox: `code_sandbox/js-math-reference/abs.html`

```javascript
Math.abs(-4.7);
```

![js-math-reference example 1 source](../code_sandbox/snaps/js-math-reference-01-code.png)

![js-math-reference example 1 result](../code_sandbox/snaps/js-math-reference-01-result.png)

- [x] **Outcome:** `Math.abs(-4.7)` is **4.7**.

<a id="js-math-reference-example-02"></a>

### **Example 2: Math.acos(0.5)**

- [x] `Math.acos(0.5)` returns the arccosine of x, in radians.
- [x] That is **π/3** (60°).

Sandbox: `code_sandbox/js-math-reference/acos.html`

```javascript
Math.acos(0.5);
```

![js-math-reference example 2 source](../code_sandbox/snaps/js-math-reference-02-code.png)

![js-math-reference example 2 result](../code_sandbox/snaps/js-math-reference-02-result.png)

- [x] **Outcome:** `Math.acos(0.5)` is **1.0471975511965979**.

<a id="js-math-reference-example-03"></a>

### **Example 3: Math.acosh(2)**

- [x] `Math.acosh(2)` returns the hyperbolic arccosine of x.

Sandbox: `code_sandbox/js-math-reference/acosh.html`

```javascript
Math.acosh(2);
```

![js-math-reference example 3 source](../code_sandbox/snaps/js-math-reference-03-code.png)

![js-math-reference example 3 result](../code_sandbox/snaps/js-math-reference-03-result.png)

- [x] **Outcome:** `Math.acosh(2)` is **1.3169578969248166**.

<a id="js-math-reference-example-04"></a>

### **Example 4: Math.asin(0.5)**

- [x] `Math.asin(0.5)` returns the arcsine of x, in radians.
- [x] That is **π/6** (30°).

Sandbox: `code_sandbox/js-math-reference/asin.html`

```javascript
Math.asin(0.5);
```

![js-math-reference example 4 source](../code_sandbox/snaps/js-math-reference-04-code.png)

![js-math-reference example 4 result](../code_sandbox/snaps/js-math-reference-04-result.png)

- [x] **Outcome:** `Math.asin(0.5)` is **0.5235987755982989**.

<a id="js-math-reference-example-05"></a>

### **Example 5: Math.asinh(1)**

- [x] `Math.asinh(1)` returns the hyperbolic arcsine of x.

Sandbox: `code_sandbox/js-math-reference/asinh.html`

```javascript
Math.asinh(1);
```

![js-math-reference example 5 source](../code_sandbox/snaps/js-math-reference-05-code.png)

![js-math-reference example 5 result](../code_sandbox/snaps/js-math-reference-05-result.png)

- [x] **Outcome:** `Math.asinh(1)` is **0.881373587019543**.

<a id="js-math-reference-example-06"></a>

### **Example 6: Math.atan(1)**

- [x] `Math.atan(1)` returns the arctangent of x in (−π/2, π/2) radians.
- [x] That is **π/4**.

Sandbox: `code_sandbox/js-math-reference/atan.html`

```javascript
Math.atan(1);
```

![js-math-reference example 6 source](../code_sandbox/snaps/js-math-reference-06-code.png)

![js-math-reference example 6 result](../code_sandbox/snaps/js-math-reference-06-result.png)

- [x] **Outcome:** `Math.atan(1)` is **0.7853981633974483**.

<a id="js-math-reference-example-07"></a>

### **Example 7: Math.atan2(8, 4)**

- [x] `Math.atan2(8, 4)` returns the arctangent of y/x, using the signs of both args (quadrant-aware).
- [x] Call is **`atan2(y, x)`** — y first.

Sandbox: `code_sandbox/js-math-reference/atan2.html`

```javascript
Math.atan2(8, 4);
```

![js-math-reference example 7 source](../code_sandbox/snaps/js-math-reference-07-code.png)

![js-math-reference example 7 result](../code_sandbox/snaps/js-math-reference-07-result.png)

- [x] **Outcome:** `Math.atan2(8, 4)` is **1.1071487177940904**.

<a id="js-math-reference-example-08"></a>

### **Example 8: Math.atanh(0.5)**

- [x] `Math.atanh(0.5)` returns the hyperbolic arctangent of x.

Sandbox: `code_sandbox/js-math-reference/atanh.html`

```javascript
Math.atanh(0.5);
```

![js-math-reference example 8 source](../code_sandbox/snaps/js-math-reference-08-code.png)

![js-math-reference example 8 result](../code_sandbox/snaps/js-math-reference-08-result.png)

- [x] **Outcome:** `Math.atanh(0.5)` is **0.5493061443340548**.

<a id="js-math-reference-example-09"></a>

### **Example 9: Math.cbrt(8)**

- [x] `Math.cbrt(8)` returns the cube root of x.

Sandbox: `code_sandbox/js-math-reference/cbrt.html`

```javascript
Math.cbrt(8);
```

![js-math-reference example 9 source](../code_sandbox/snaps/js-math-reference-09-code.png)

![js-math-reference example 9 result](../code_sandbox/snaps/js-math-reference-09-result.png)

- [x] **Outcome:** `Math.cbrt(8)` is **2**.

<a id="js-math-reference-example-10"></a>

### **Example 10: Math.ceil(4.4)**

- [x] `Math.ceil(4.4)` returns x rounded **up** (toward +∞) to an integer.

Sandbox: `code_sandbox/js-math-reference/ceil.html`

```javascript
Math.ceil(4.4);
```

![js-math-reference example 10 source](../code_sandbox/snaps/js-math-reference-10-code.png)

![js-math-reference example 10 result](../code_sandbox/snaps/js-math-reference-10-result.png)

- [x] **Outcome:** `Math.ceil(4.4)` is **5**.

<a id="js-math-reference-example-11"></a>

### **Example 11: Math.clz32(1)**

- [x] `Math.clz32(1)` returns the number of leading zero bits in the 32-bit binary form of x.
- [x] `1` is `...0001` in 32 bits, so **31** leading zeros.

Sandbox: `code_sandbox/js-math-reference/clz32.html`

```javascript
Math.clz32(1);
```

![js-math-reference example 11 source](../code_sandbox/snaps/js-math-reference-11-code.png)

![js-math-reference example 11 result](../code_sandbox/snaps/js-math-reference-11-result.png)

- [x] **Outcome:** `Math.clz32(1)` is **31**.

<a id="js-math-reference-example-12"></a>

### **Example 12: Math.cos(0)**

- [x] `Math.cos(0)` returns the cosine of x (radians).

Sandbox: `code_sandbox/js-math-reference/cos.html`

```javascript
Math.cos(0);
```

![js-math-reference example 12 source](../code_sandbox/snaps/js-math-reference-12-code.png)

![js-math-reference example 12 result](../code_sandbox/snaps/js-math-reference-12-result.png)

- [x] **Outcome:** `Math.cos(0)` is **1**.

<a id="js-math-reference-example-13"></a>

### **Example 13: Math.cosh(0)**

- [x] `Math.cosh(0)` returns the hyperbolic cosine of x.

Sandbox: `code_sandbox/js-math-reference/cosh.html`

```javascript
Math.cosh(0);
```

![js-math-reference example 13 source](../code_sandbox/snaps/js-math-reference-13-code.png)

![js-math-reference example 13 result](../code_sandbox/snaps/js-math-reference-13-result.png)

- [x] **Outcome:** `Math.cosh(0)` is **1**.

<a id="js-math-reference-example-14"></a>

### **Example 14: Math.E**

- [x] `Math.E` is Euler’s number e (base of natural logs).

Sandbox: `code_sandbox/js-math-reference/e.html`

```javascript
Math.E;
```

![js-math-reference example 14 source](../code_sandbox/snaps/js-math-reference-14-code.png)

![js-math-reference example 14 result](../code_sandbox/snaps/js-math-reference-14-result.png)

- [x] **Outcome:** `Math.E` is **2.718281828459045**.

<a id="js-math-reference-example-15"></a>

### **Example 15: Math.exp(1)**

- [x] `Math.exp(1)` returns **eˣ** (`Math.E ** x`).
- [x] Same as `Math.E`.

Sandbox: `code_sandbox/js-math-reference/exp.html`

```javascript
Math.exp(1);
```

![js-math-reference example 15 source](../code_sandbox/snaps/js-math-reference-15-code.png)

![js-math-reference example 15 result](../code_sandbox/snaps/js-math-reference-15-result.png)

- [x] **Outcome:** `Math.exp(1)` is **2.718281828459045**.

<a id="js-math-reference-example-16"></a>

### **Example 16: Math.expm1(1)**

- [x] `Math.expm1(1)` returns **eˣ − 1** (accurate near 0).

Sandbox: `code_sandbox/js-math-reference/expm1.html`

```javascript
Math.expm1(1);
```

![js-math-reference example 16 source](../code_sandbox/snaps/js-math-reference-16-code.png)

![js-math-reference example 16 result](../code_sandbox/snaps/js-math-reference-16-result.png)

- [x] **Outcome:** `Math.expm1(1)` is **1.718281828459045**.

<a id="js-math-reference-example-17"></a>

### **Example 17: Math.f16round(1.337)**

- [x] `Math.f16round(x)` rounds x to the nearest **IEEE 754 binary16** (half-precision) value.
- [x] The W3Schools table text (“rounded downwards to the nearest integer”) is **wrong** — that is `floor`.

Sandbox: `code_sandbox/js-math-reference/f16round.html`

```javascript
Math.f16round(1.337);
```

![js-math-reference example 17 source](../code_sandbox/snaps/js-math-reference-17-code.png)

![js-math-reference example 17 result](../code_sandbox/snaps/js-math-reference-17-result.png)

- [x] **Outcome:** **1.3369140625** (not an integer). Chrome implements this; Node 22 does not.

<a id="js-math-reference-example-18"></a>

### **Example 18: Math.floor(4.7)**

- [x] `Math.floor(4.7)` returns x rounded **down** (toward −∞) to an integer.

Sandbox: `code_sandbox/js-math-reference/floor.html`

```javascript
Math.floor(4.7);
```

![js-math-reference example 18 source](../code_sandbox/snaps/js-math-reference-18-code.png)

![js-math-reference example 18 result](../code_sandbox/snaps/js-math-reference-18-result.png)

- [x] **Outcome:** `Math.floor(4.7)` is **4**.

<a id="js-math-reference-example-19"></a>

### **Example 19: Math.fround(1.337)**

- [x] `Math.fround(1.337)` returns the nearest **32-bit** (single-precision) float.

Sandbox: `code_sandbox/js-math-reference/fround.html`

```javascript
Math.fround(1.337);
```

![js-math-reference example 19 source](../code_sandbox/snaps/js-math-reference-19-code.png)

![js-math-reference example 19 result](../code_sandbox/snaps/js-math-reference-19-result.png)

- [x] **Outcome:** `Math.fround(1.337)` is **1.3370000123977661**.

<a id="js-math-reference-example-20"></a>

### **Example 20: Math.LN2**

- [x] `Math.LN2` is ln(2), the natural log of 2.

Sandbox: `code_sandbox/js-math-reference/ln2.html`

```javascript
Math.LN2;
```

![js-math-reference example 20 source](../code_sandbox/snaps/js-math-reference-20-code.png)

![js-math-reference example 20 result](../code_sandbox/snaps/js-math-reference-20-result.png)

- [x] **Outcome:** `Math.LN2` is **0.6931471805599453**.

<a id="js-math-reference-example-21"></a>

### **Example 21: Math.LN10**

- [x] `Math.LN10` is ln(10), the natural log of 10.

Sandbox: `code_sandbox/js-math-reference/ln10.html`

```javascript
Math.LN10;
```

![js-math-reference example 21 source](../code_sandbox/snaps/js-math-reference-21-code.png)

![js-math-reference example 21 result](../code_sandbox/snaps/js-math-reference-21-result.png)

- [x] **Outcome:** `Math.LN10` is **2.302585092994046**.

<a id="js-math-reference-example-22"></a>

### **Example 22: Math.log(2)**

- [x] `Math.log(2)` returns the natural logarithm of x (ln x).

Sandbox: `code_sandbox/js-math-reference/log.html`

```javascript
Math.log(2);
```

![js-math-reference example 22 source](../code_sandbox/snaps/js-math-reference-22-code.png)

![js-math-reference example 22 result](../code_sandbox/snaps/js-math-reference-22-result.png)

- [x] **Outcome:** `Math.log(2)` is **0.6931471805599453**.

<a id="js-math-reference-example-23"></a>

### **Example 23: Math.log10(1000)**

- [x] `Math.log10(1000)` returns the base-10 logarithm of x.

Sandbox: `code_sandbox/js-math-reference/log10.html`

```javascript
Math.log10(1000);
```

![js-math-reference example 23 source](../code_sandbox/snaps/js-math-reference-23-code.png)

![js-math-reference example 23 result](../code_sandbox/snaps/js-math-reference-23-result.png)

- [x] **Outcome:** `Math.log10(1000)` is **3**.

<a id="js-math-reference-example-24"></a>

### **Example 24: Math.LOG10E**

- [x] `Math.LOG10E` is log₁₀(e).

Sandbox: `code_sandbox/js-math-reference/log10e.html`

```javascript
Math.LOG10E;
```

![js-math-reference example 24 source](../code_sandbox/snaps/js-math-reference-24-code.png)

![js-math-reference example 24 result](../code_sandbox/snaps/js-math-reference-24-result.png)

- [x] **Outcome:** `Math.LOG10E` is **0.4342944819032518**.

<a id="js-math-reference-example-25"></a>

### **Example 25: Math.log1p(1)**

- [x] `Math.log1p(1)` returns ln(1 + x) (accurate near 0).

Sandbox: `code_sandbox/js-math-reference/log1p.html`

```javascript
Math.log1p(1);
```

![js-math-reference example 25 source](../code_sandbox/snaps/js-math-reference-25-code.png)

![js-math-reference example 25 result](../code_sandbox/snaps/js-math-reference-25-result.png)

- [x] **Outcome:** `Math.log1p(1)` is **0.6931471805599453**.

<a id="js-math-reference-example-26"></a>

### **Example 26: Math.log2(8)**

- [x] `Math.log2(8)` returns the base-2 logarithm of x.

Sandbox: `code_sandbox/js-math-reference/log2.html`

```javascript
Math.log2(8);
```

![js-math-reference example 26 source](../code_sandbox/snaps/js-math-reference-26-code.png)

![js-math-reference example 26 result](../code_sandbox/snaps/js-math-reference-26-result.png)

- [x] **Outcome:** `Math.log2(8)` is **3**.

<a id="js-math-reference-example-27"></a>

### **Example 27: Math.LOG2E**

- [x] `Math.LOG2E` is log₂(e).

Sandbox: `code_sandbox/js-math-reference/log2e.html`

```javascript
Math.LOG2E;
```

![js-math-reference example 27 source](../code_sandbox/snaps/js-math-reference-27-code.png)

![js-math-reference example 27 result](../code_sandbox/snaps/js-math-reference-27-result.png)

- [x] **Outcome:** `Math.LOG2E` is **1.4426950408889634**.

<a id="js-math-reference-example-28"></a>

### **Example 28: Math.max(0, 150, 30, 20, -8, -200)**

- [x] `Math.max(0, 150, 30, 20, -8, -200)` returns the largest argument.

Sandbox: `code_sandbox/js-math-reference/max.html`

```javascript
Math.max(0, 150, 30, 20, -8, -200);
```

![js-math-reference example 28 source](../code_sandbox/snaps/js-math-reference-28-code.png)

![js-math-reference example 28 result](../code_sandbox/snaps/js-math-reference-28-result.png)

- [x] **Outcome:** `Math.max(0, 150, 30, 20, -8, -200)` is **150**.

<a id="js-math-reference-example-29"></a>

### **Example 29: Math.min(0, 150, 30, 20, -8, -200)**

- [x] `Math.min(0, 150, 30, 20, -8, -200)` returns the smallest argument.

Sandbox: `code_sandbox/js-math-reference/min.html`

```javascript
Math.min(0, 150, 30, 20, -8, -200);
```

![js-math-reference example 29 source](../code_sandbox/snaps/js-math-reference-29-code.png)

![js-math-reference example 29 result](../code_sandbox/snaps/js-math-reference-29-result.png)

- [x] **Outcome:** `Math.min(0, 150, 30, 20, -8, -200)` is **-200**.

<a id="js-math-reference-example-30"></a>

### **Example 30: Math.PI**

- [x] `Math.PI` is π (ratio of circumference to diameter).

Sandbox: `code_sandbox/js-math-reference/pi.html`

```javascript
Math.PI;
```

![js-math-reference example 30 source](../code_sandbox/snaps/js-math-reference-30-code.png)

![js-math-reference example 30 result](../code_sandbox/snaps/js-math-reference-30-result.png)

- [x] **Outcome:** `Math.PI` is **3.141592653589793**.

<a id="js-math-reference-example-31"></a>

### **Example 31: Math.pow(8, 2)**

- [x] `Math.pow(8, 2)` returns x to the power y.

Sandbox: `code_sandbox/js-math-reference/pow.html`

```javascript
Math.pow(8, 2);
```

![js-math-reference example 31 source](../code_sandbox/snaps/js-math-reference-31-code.png)

![js-math-reference example 31 result](../code_sandbox/snaps/js-math-reference-31-result.png)

- [x] **Outcome:** `Math.pow(8, 2)` is **64**.

<a id="js-math-reference-example-32"></a>

### **Example 32: Math.random()**

- [x] `Math.random()` returns a sample in **[0, 1)** (0 included, 1 excluded).
- [x] The snap is one draw — not a stable constant.

Sandbox: `code_sandbox/js-math-reference/random.html`

```javascript
Math.random();
```

![js-math-reference example 32 source](../code_sandbox/snaps/js-math-reference-32-code.png)

![js-math-reference example 32 result](../code_sandbox/snaps/js-math-reference-32-result.png)

- [x] **Outcome:** The snap shows a **sample** in **[0, 1)**. Re-running yields another number. Never **1**.

<a id="js-math-reference-example-33"></a>

### **Example 33: Math.round(4.5)**

- [x] `Math.round(4.5)` rounds x to the nearest integer (4.5 → 5).

Sandbox: `code_sandbox/js-math-reference/round.html`

```javascript
Math.round(4.5);
```

![js-math-reference example 33 source](../code_sandbox/snaps/js-math-reference-33-code.png)

![js-math-reference example 33 result](../code_sandbox/snaps/js-math-reference-33-result.png)

- [x] **Outcome:** `Math.round(4.5)` is **5**.

<a id="js-math-reference-example-34"></a>

### **Example 34: Math.sign(-4)**

- [x] `Math.sign(-4)` returns the sign of x: −1, 0, or 1.

Sandbox: `code_sandbox/js-math-reference/sign.html`

```javascript
Math.sign(-4);
```

![js-math-reference example 34 source](../code_sandbox/snaps/js-math-reference-34-code.png)

![js-math-reference example 34 result](../code_sandbox/snaps/js-math-reference-34-result.png)

- [x] **Outcome:** `Math.sign(-4)` is **-1**.

<a id="js-math-reference-example-35"></a>

### **Example 35: Math.sin(Math.PI / 2)**

- [x] `Math.sin(Math.PI / 2)` returns the sine of x (radians).

Sandbox: `code_sandbox/js-math-reference/sin.html`

```javascript
Math.sin(Math.PI / 2);
```

![js-math-reference example 35 source](../code_sandbox/snaps/js-math-reference-35-code.png)

![js-math-reference example 35 result](../code_sandbox/snaps/js-math-reference-35-result.png)

- [x] **Outcome:** `Math.sin(Math.PI / 2)` is **1**.

<a id="js-math-reference-example-36"></a>

### **Example 36: Math.sinh(1)**

- [x] `Math.sinh(1)` returns the hyperbolic sine of x.

Sandbox: `code_sandbox/js-math-reference/sinh.html`

```javascript
Math.sinh(1);
```

![js-math-reference example 36 source](../code_sandbox/snaps/js-math-reference-36-code.png)

![js-math-reference example 36 result](../code_sandbox/snaps/js-math-reference-36-result.png)

- [x] **Outcome:** `Math.sinh(1)` is **1.1752011936438014**.

<a id="js-math-reference-example-37"></a>

### **Example 37: Math.sqrt(64)**

- [x] `Math.sqrt(64)` returns the square root of x.

Sandbox: `code_sandbox/js-math-reference/sqrt.html`

```javascript
Math.sqrt(64);
```

![js-math-reference example 37 source](../code_sandbox/snaps/js-math-reference-37-code.png)

![js-math-reference example 37 result](../code_sandbox/snaps/js-math-reference-37-result.png)

- [x] **Outcome:** `Math.sqrt(64)` is **8**.

<a id="js-math-reference-example-38"></a>

### **Example 38: Math.SQRT1_2**

- [x] `Math.SQRT1_2` is √(1/2) = 1/√2.

Sandbox: `code_sandbox/js-math-reference/sqrt1-2.html`

```javascript
Math.SQRT1_2;
```

![js-math-reference example 38 source](../code_sandbox/snaps/js-math-reference-38-code.png)

![js-math-reference example 38 result](../code_sandbox/snaps/js-math-reference-38-result.png)

- [x] **Outcome:** `Math.SQRT1_2` is **0.7071067811865476**.

<a id="js-math-reference-example-39"></a>

### **Example 39: Math.SQRT2**

- [x] `Math.SQRT2` is √2.

Sandbox: `code_sandbox/js-math-reference/sqrt2.html`

```javascript
Math.SQRT2;
```

![js-math-reference example 39 source](../code_sandbox/snaps/js-math-reference-39-code.png)

![js-math-reference example 39 result](../code_sandbox/snaps/js-math-reference-39-result.png)

- [x] **Outcome:** `Math.SQRT2` is **1.4142135623730951**.

<a id="js-math-reference-example-40"></a>

### **Example 40: Math.tan(Math.PI / 4)**

- [x] `Math.tan(x)` is the tangent of x in **radians**. π/4 is 45°.
- [x] Floating-point π is not exact, so the result is **not** a clean `1`.

Sandbox: `code_sandbox/js-math-reference/tan.html`

```javascript
Math.tan(Math.PI / 4);
```

![js-math-reference example 40 source](../code_sandbox/snaps/js-math-reference-40-code.png)

![js-math-reference example 40 result](../code_sandbox/snaps/js-math-reference-40-result.png)

- [x] **Outcome:** **0.9999999999999999** (not exactly 1).

<a id="js-math-reference-example-41"></a>

### **Example 41: Math.tanh(1)**

- [x] `Math.tanh(1)` returns the hyperbolic tangent of x.

Sandbox: `code_sandbox/js-math-reference/tanh.html`

```javascript
Math.tanh(1);
```

![js-math-reference example 41 source](../code_sandbox/snaps/js-math-reference-41-code.png)

![js-math-reference example 41 result](../code_sandbox/snaps/js-math-reference-41-result.png)

- [x] **Outcome:** `Math.tanh(1)` is **0.7615941559557649**.

<a id="js-math-reference-example-42"></a>

### **Example 42: Math.trunc(4.7)**

- [x] `Math.trunc(4.7)` returns the integer part of x (toward 0).

Sandbox: `code_sandbox/js-math-reference/trunc.html`

```javascript
Math.trunc(4.7);
```

![js-math-reference example 42 source](../code_sandbox/snaps/js-math-reference-42-code.png)

![js-math-reference example 42 result](../code_sandbox/snaps/js-math-reference-42-result.png)

- [x] **Outcome:** `Math.trunc(4.7)` is **4**.

<a id="js-math-reference-example-43"></a>

### **Example 43: Math.hypot(3, 4) — extra (not on the July 2025 table)**

- [x] `Math.hypot(...)` is the square root of the sum of squares (Euclidean length).
- [x] **Not** a row on the live W3Schools table (revised July 2025). Still a standard `Math` method.

Sandbox: `code_sandbox/js-math-reference/hypot.html`

```javascript
Math.hypot(3, 4);
```

![js-math-reference example 43 source](../code_sandbox/snaps/js-math-reference-43-code.png)

![js-math-reference example 43 result](../code_sandbox/snaps/js-math-reference-43-result.png)

- [x] **Outcome:** **5** (3-4-5 triangle).

<a id="js-math-reference-example-44"></a>

### **Example 44: Math.imul(2, 4) — extra (not on the July 2025 table)**

- [x] `Math.imul(a, b)` is **32-bit integer** multiply (C-like `int32`).
- [x] **Not** a row on the live W3Schools table. Overflow wraps in 32-bit two’s complement.

Sandbox: `code_sandbox/js-math-reference/imul.html`

```javascript
Math.imul(2, 4);
Math.imul(0xffffffff, 5);
```

![js-math-reference example 44 source](../code_sandbox/snaps/js-math-reference-44-code.png)

![js-math-reference example 44 result](../code_sandbox/snaps/js-math-reference-44-result.png)

- [x] **Outcome:** `imul(2, 4)` is **8**. `imul(0xffffffff, 5)` is **−5** (32-bit wrap: −1 × 5).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-math-reference/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Is this page a catalog?

<details>
<summary>Answer</summary>

- [x] **Yes.** One Example **per table row**, not one snippet for many names.

</details>

### Question 2: What is `Math.E`?

<details>
<summary>Answer</summary>

- [x] **2.718281828459045**.

</details>

### Question 3: What is `Math.clz32(1)`?

<details>
<summary>Answer</summary>

- [x] **31** leading zeros in the 32-bit form of 1.

</details>

### Question 4: What does `f16round` actually do?

<details>
<summary>Answer</summary>

- [x] Nearest **binary16** float. `f16round(1.337)` is **1.3369140625**. It is **not** `floor`.

</details>

### Question 5: What is `Math.fround(1.337)`?

<details>
<summary>Answer</summary>

- [x] **1.3370000123977661** (IEEE 32-bit).

</details>

### Question 6: `atan2` argument order?

<details>
<summary>Answer</summary>

- [x] **`atan2(y, x)`** — y first. `atan2(8, 4)` is **1.1071487177940904**.

</details>

### Question 7: `Math.max` / `Math.min` of the page’s list?

<details>
<summary>Answer</summary>

- [x] **150** and **−200**.

</details>

### Question 8: What is `Math.sign(-4)`?

<details>
<summary>Answer</summary>

- [x] **−1**.

</details>

### Question 9: Why isn’t `tan(π/4)` exactly 1?

<details>
<summary>Answer</summary>

- [x] `Math.PI / 4` is not a perfect 45° in binary float → **0.9999999999999999**.

</details>

### Question 10: Are `hypot` and `imul` on the July 2025 table?

<details>
<summary>Answer</summary>

- [x] **No.** Still run: `hypot(3,4)` is **5**; `imul(2,4)` is **8**; `imul(0xffffffff, 5)` is **−5**.

</details>

### Question 11: What is `Math.random()` here?

<details>
<summary>Answer</summary>

- [x] A **sample in [0, 1)** — not a fixed number.

</details>

### Question 12: `exp(1)` vs `expm1(1)`?

<details>
<summary>Answer</summary>

- [x] **e** (2.718…) vs **e − 1** (1.718…).

</details>


</details>

## Summary

Treat the reference as a catalog: one run per row. Trust the engine’s number, not the f16round table sentence. trig is radians; atan2 is (y, x). hypot and imul exist even when omitted from this table.

## References

- [JS Math Reference (W3Schools)](https://www.w3schools.com/js/js_math_reference.asp)
- [MDN: Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
- [MDN: Math.f16round](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/f16round)
- [MDN: Math.hypot](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/hypot)
- [MDN: Math.imul](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/imul)
