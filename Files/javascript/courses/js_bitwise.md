# JS Bitwise

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Bitwise operators (`& | ^ ~ << >> >>>`) work on **32-bit signed integers**, even though Numbers are 64-bit floats. Each operator (and each assignment form) has its own Example, plus decimal↔binary helpers. Four-bit unsigned tables on the page are teaching aids — in real JS, `~5` is **−6**, not 10.

This section has **15** examples:

- [x] **Example 1:** Bitwise AND `&` [View](#js-bitwise-example-01)
- [x] **Example 2:** Bitwise OR `|` [View](#js-bitwise-example-02)
- [x] **Example 3:** Bitwise XOR `^` [View](#js-bitwise-example-03)
- [x] **Example 4:** Bitwise NOT `~` [View](#js-bitwise-example-04)
- [x] **Example 5:** Zero-fill left shift `<<` [View](#js-bitwise-example-05)
- [x] **Example 6:** Sign-preserving right shift `>>` [View](#js-bitwise-example-06)
- [x] **Example 7:** Zero-fill right shift `>>>` [View](#js-bitwise-example-07)
- [x] **Example 8:** Left shift assignment `<<=` [View](#js-bitwise-example-08)
- [x] **Example 9:** Signed right shift assignment `>>=` [View](#js-bitwise-example-09)
- [x] **Example 10:** Unsigned right shift assignment `>>>=` [View](#js-bitwise-example-10)
- [x] **Example 11:** AND assignment `&=` [View](#js-bitwise-example-11)
- [x] **Example 12:** OR assignment `|=` [View](#js-bitwise-example-12)
- [x] **Example 13:** XOR assignment `^=` [View](#js-bitwise-example-13)
- [x] **Example 14:** Decimal to binary [View](#js-bitwise-example-14)
- [x] **Example 15:** Binary to decimal [View](#js-bitwise-example-15)

## Detailed Explanation

- [x] **32-bit two’s complement** — the leftmost bit is the sign.
- [x] **`>>` keeps the sign**; **`>>>` zero-fills** (and makes negatives large positives).
- [x] **Assignment forms** `&= |= ^= <<= >>= >>>=` update in place.

<a id="js-bitwise-example-01"></a>

### **Example 1: Bitwise AND `&`**

- [x] JavaScript bitwise ops convert to **32-bit signed integers**, then convert the result back to a Number.
- [x] **AND** sets a bit only if **both** bits are 1. Truth table: 1&1=1; anything with 0 is 0.
- [x] `5 & 1` → `0101 & 0001` → **0001** = **1**.

Sandbox: `code_sandbox/js-bitwise/and.html`

```javascript
let x = 5 & 1;
```

![js-bitwise example 1 source](../code_sandbox/snaps/js-bitwise-01-code.png)

![js-bitwise example 1 result](../code_sandbox/snaps/js-bitwise-01-result.png)

- [x] **Outcome:** x is **1**.

<a id="js-bitwise-example-02"></a>

### **Example 2: Bitwise OR `|`**

- [x] **OR** sets a bit if **either** bit is 1.
- [x] `5 | 1` → `0101 | 0001` → **0101** = **5**.

Sandbox: `code_sandbox/js-bitwise/or.html`

```javascript
let x = 5 | 1;
```

![js-bitwise example 2 source](../code_sandbox/snaps/js-bitwise-02-code.png)

![js-bitwise example 2 result](../code_sandbox/snaps/js-bitwise-02-result.png)

- [x] **Outcome:** x is **5**.

<a id="js-bitwise-example-03"></a>

### **Example 3: Bitwise XOR `^`**

- [x] **XOR** sets a bit if the bits are **different**.
- [x] `5 ^ 1` → `0101 ^ 0001` → **0100** = **4**.

Sandbox: `code_sandbox/js-bitwise/xor.html`

```javascript
let x = 5 ^ 1;
```

![js-bitwise example 3 source](../code_sandbox/snaps/js-bitwise-03-code.png)

![js-bitwise example 3 result](../code_sandbox/snaps/js-bitwise-03-result.png)

- [x] **Outcome:** x is **4**.

<a id="js-bitwise-example-04"></a>

### **Example 4: Bitwise NOT `~`**

- [x] 4-bit unsigned tables say `~5` is 10. JavaScript uses **32-bit two’s complement**, so **`~5` is −6**, not 10.
- [x] `~n` is equal to **`-(n + 1)`**.

Sandbox: `code_sandbox/js-bitwise/not.html`

```javascript
let x = ~5;
```

![js-bitwise example 4 source](../code_sandbox/snaps/js-bitwise-04-code.png)

![js-bitwise example 4 result](../code_sandbox/snaps/js-bitwise-04-result.png)

- [x] **Outcome:** x is **-6**.

<a id="js-bitwise-example-05"></a>

### **Example 5: Zero-fill left shift `<<`**

- [x] Pushes **zeros in from the right**; leftmost bits fall off.
- [x] `5 << 1` doubles 5 → **10**.

Sandbox: `code_sandbox/js-bitwise/left-shift.html`

```javascript
let x = 5 << 1;
```

![js-bitwise example 5 source](../code_sandbox/snaps/js-bitwise-05-code.png)

![js-bitwise example 5 result](../code_sandbox/snaps/js-bitwise-05-result.png)

- [x] **Outcome:** x is **10**.

<a id="js-bitwise-example-06"></a>

### **Example 6: Sign-preserving right shift `>>`**

- [x] Copies the **sign bit** in from the left (arithmetic shift).
- [x] `-5 >> 1` is **-3** (not a zero-filled 2).

Sandbox: `code_sandbox/js-bitwise/sign-right.html`

```javascript
let x = -5 >> 1;
```

![js-bitwise example 6 source](../code_sandbox/snaps/js-bitwise-06-code.png)

![js-bitwise example 6 result](../code_sandbox/snaps/js-bitwise-06-result.png)

- [x] **Outcome:** x is **-3**.

<a id="js-bitwise-example-07"></a>

### **Example 7: Zero-fill right shift `>>>`**

- [x] Pushes **zeros** in from the left (logical shift).
- [x] `5 >>> 1` is **2**. On negatives this yields a **large positive** 32-bit value.

Sandbox: `code_sandbox/js-bitwise/zero-right.html`

```javascript
let x = 5 >>> 1;
```

![js-bitwise example 7 source](../code_sandbox/snaps/js-bitwise-07-code.png)

![js-bitwise example 7 result](../code_sandbox/snaps/js-bitwise-07-result.png)

- [x] **Outcome:** `5 >>> 1` is **2**. `-5 >>> 1` is **2147483645** (extra clarifying row).

<a id="js-bitwise-example-08"></a>

### **Example 8: Left shift assignment `<<=`**

- [x] `x <<= y` means `x = x << y`.
- [x] `-100 << 5` shifts −100 left by 5.

Sandbox: `code_sandbox/js-bitwise/assign-left.html`

```javascript
let x = -100;
x <<= 5;
```

![js-bitwise example 8 source](../code_sandbox/snaps/js-bitwise-08-code.png)

![js-bitwise example 8 result](../code_sandbox/snaps/js-bitwise-08-result.png)

- [x] **Outcome:** x is **-3200**.

<a id="js-bitwise-example-09"></a>

### **Example 9: Signed right shift assignment `>>=`**

- [x] `x >>= y` means `x = x >> y` (keeps the sign).

Sandbox: `code_sandbox/js-bitwise/assign-right.html`

```javascript
let x = -100;
x >>= 5;
```

![js-bitwise example 9 source](../code_sandbox/snaps/js-bitwise-09-code.png)

![js-bitwise example 9 result](../code_sandbox/snaps/js-bitwise-09-result.png)

- [x] **Outcome:** x is **-4** (sign preserved).

<a id="js-bitwise-example-10"></a>

### **Example 10: Unsigned right shift assignment `>>>=`**

- [x] `x >>>= y` means `x = x >>> y` (zero fill).
- [x] On a negative start value this becomes a **large positive** number.

Sandbox: `code_sandbox/js-bitwise/assign-uright.html`

```javascript
let x = -100;
x >>>= 5;
```

![js-bitwise example 10 source](../code_sandbox/snaps/js-bitwise-10-code.png)

![js-bitwise example 10 result](../code_sandbox/snaps/js-bitwise-10-result.png)

- [x] **Outcome:** x is **134217724**.

<a id="js-bitwise-example-11"></a>

### **Example 11: AND assignment `&=`**

- [x] `x &= y` means `x = x & y`.
- [x] `10 & 5` → `1010 & 0101` → **0**.

Sandbox: `code_sandbox/js-bitwise/assign-and.html`

```javascript
let x = 10;
x &= 5;
```

![js-bitwise example 11 source](../code_sandbox/snaps/js-bitwise-11-code.png)

![js-bitwise example 11 result](../code_sandbox/snaps/js-bitwise-11-result.png)

- [x] **Outcome:** x is **0**.

<a id="js-bitwise-example-12"></a>

### **Example 12: OR assignment `|=`**

- [x] `x |= y` means `x = x | y`.
- [x] `10 | 5` → **15**.

Sandbox: `code_sandbox/js-bitwise/assign-or.html`

```javascript
let x = 10;
x |= 5;
```

![js-bitwise example 12 source](../code_sandbox/snaps/js-bitwise-12-code.png)

![js-bitwise example 12 result](../code_sandbox/snaps/js-bitwise-12-result.png)

- [x] **Outcome:** x is **15**.

<a id="js-bitwise-example-13"></a>

### **Example 13: XOR assignment `^=`**

- [x] `x ^= y` means `x = x ^ y`.
- [x] `10 ^ 5` → **15**.

Sandbox: `code_sandbox/js-bitwise/assign-xor.html`

```javascript
let x = 10;
x ^= 5;
```

![js-bitwise example 13 source](../code_sandbox/snaps/js-bitwise-13-code.png)

![js-bitwise example 13 result](../code_sandbox/snaps/js-bitwise-13-result.png)

- [x] **Outcome:** x is **15**.

<a id="js-bitwise-example-14"></a>

### **Example 14: Decimal to binary**

- [x] `(dec >>> 0).toString(2)` treats the value as **unsigned 32-bit**, then prints binary.
- [x] `>>> 0` is a common trick to get an unsigned 32-bit view (important for negatives).

Sandbox: `code_sandbox/js-bitwise/dec2bin.html`

```javascript
function dec2bin(dec) {
  return (dec >>> 0).toString(2);
}
```

![js-bitwise example 14 source](../code_sandbox/snaps/js-bitwise-14-code.png)

![js-bitwise example 14 result](../code_sandbox/snaps/js-bitwise-14-result.png)

- [x] **Outcome:** `dec2bin(5)` is **101**. `dec2bin(-5)` is the 32-bit two’s complement string.

<a id="js-bitwise-example-15"></a>

### **Example 15: Binary to decimal**

- [x] `parseInt(bin, 2)` parses a **binary string** as base 2.

Sandbox: `code_sandbox/js-bitwise/bin2dec.html`

```javascript
function bin2dec(bin) {
  return parseInt(bin, 2).toString(10);
}
```

![js-bitwise example 15 source](../code_sandbox/snaps/js-bitwise-15-code.png)

![js-bitwise example 15 result](../code_sandbox/snaps/js-bitwise-15-result.png)

- [x] **Outcome:** `"101"` → **5**; `"1111"` → **15**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-bitwise/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is `5 & 1`?

<details>
<summary>Answer</summary>

- [x] **1** — only bits set in both.

</details>

### Question 2: What is `5 | 1`?

<details>
<summary>Answer</summary>

- [x] **5**.

</details>

### Question 3: What is `5 ^ 1`?

<details>
<summary>Answer</summary>

- [x] **4**.

</details>

### Question 4: What is `~5` in JavaScript?

<details>
<summary>Answer</summary>

- [x] **-6**, not 10. `~n === -(n+1)`.

</details>

### Question 5: What is `5 << 1`?

<details>
<summary>Answer</summary>

- [x] **10**.

</details>

### Question 6: What is `-5 >> 1`?

<details>
<summary>Answer</summary>

- [x] **-3** (sign preserved).

</details>

### Question 7: What is `5 >>> 1`?

<details>
<summary>Answer</summary>

- [x] **2**.

</details>

### Question 8: What is `10 &= 5`?

<details>
<summary>Answer</summary>

- [x] **0**.

</details>

### Question 9: What is `10 | 5`?

<details>
<summary>Answer</summary>

- [x] **15**.

</details>

### Question 10: How do you convert 5 to binary?

<details>
<summary>Answer</summary>

- [x] `(5 >>> 0).toString(2)` → **101**.

</details>

### Question 11: How do you parse binary `"1111"`?

<details>
<summary>Answer</summary>

- [x] `parseInt("1111", 2)` → **15**.

</details>

### Question 12: Why does `~5` differ from the 4-bit table?

<details>
<summary>Answer</summary>

- [x] The table uses 4-bit **unsigned** bits. JS uses **32-bit signed** integers.

</details>

</details>

## Summary

Use `& | ^ ~` for bit masks and `<< >> >>>` to shift. Remember 32-bit signed conversion: `~5` is −6. `>>>` zero-fills. `dec >>> 0` plus `toString(2)` prints unsigned binary; `parseInt(s, 2)` parses it back.

## References

- [JS Bitwise (W3Schools)](https://www.w3schools.com/js/js_bitwise.asp)
- [MDN: Bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND)
- [MDN: Unsigned right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)
