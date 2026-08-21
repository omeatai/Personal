# JS Dates

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Date objects store an instant as milliseconds since 1 January 1970 UTC. new Date() captures now; the object does not keep ticking. You can pass a date string, a millisecond count, or 2–7 numbers (year, month, …). Months are 0–11. Extra months or days overflow instead of throwing. A single number is milliseconds, not a year. Years 0–99 become 19xx. Display helpers include toString, toDateString, toUTCString, and toISOString. Date string formats are the next chapter — not this one.

This section has **24** examples:

- [x] **Example 1:** new Date() — current date and time [View](#js-dates-example-01)
- [x] **Example 2:** new Date("2022-03-25") [View](#js-dates-example-02)
- [x] **Example 3:** new Date("October 13, 2014 11:13:00") [View](#js-dates-example-03)
- [x] **Example 4:** new Date(2018, 11, 24, 10, 33, 30, 0) — month 11 is December [View](#js-dates-example-04)
- [x] **Example 5:** new Date(2018, 15, ...) — month overflow to April 2019 [View](#js-dates-example-05)
- [x] **Example 6:** new Date(2019, 3, ...) — same as month overflow [View](#js-dates-example-06)
- [x] **Example 7:** new Date(2018, 5, 35, ...) — day overflow [View](#js-dates-example-07)
- [x] **Example 8:** new Date(2018, 6, 5, ...) — same as day overflow [View](#js-dates-example-08)
- [x] **Example 9:** 6 numbers: year through seconds [View](#js-dates-example-09)
- [x] **Example 10:** 5 numbers: year through minutes [View](#js-dates-example-10)
- [x] **Example 11:** 4 numbers: year, month, day, hours [View](#js-dates-example-11)
- [x] **Example 12:** 3 numbers: year, month, day [View](#js-dates-example-12)
- [x] **Example 13:** 2 numbers: year and month [View](#js-dates-example-13)
- [x] **Example 14:** 1 number: new Date(2018) is milliseconds, not year [View](#js-dates-example-14)
- [x] **Example 15:** new Date(99, 11, 24) → 1999 [View](#js-dates-example-15)
- [x] **Example 16:** new Date(9, 11, 24) → 1909 [View](#js-dates-example-16)
- [x] **Example 17:** new Date(100000000000) [View](#js-dates-example-17)
- [x] **Example 18:** new Date(-100000000000) [View](#js-dates-example-18)
- [x] **Example 19:** new Date(24*60*60\*1000) / 86400000 [View](#js-dates-example-19)
- [x] **Example 20:** new Date(0) — epoch [View](#js-dates-example-20)
- [x] **Example 21:** d.toString() [View](#js-dates-example-21)
- [x] **Example 22:** d.toDateString() [View](#js-dates-example-22)
- [x] **Example 23:** d.toUTCString() [View](#js-dates-example-23)
- [x] **Example 24:** d.toISOString() [View](#js-dates-example-24)

## Detailed Explanation

- [x] Date objects are **static**. Creating `new Date()` copies **now**; the object’s clock does **not** run.
- [x] **Nine constructors:** no-arg now, date string, 2–7 numbers, or milliseconds.
- [x] Months are **0–11**. Overflow months/days **roll** into later months/years (no error).
- [x] **One** argument = **milliseconds**, not a year. **0–99** years map to **19xx**.
- [x] Epoch is **1970-01-01T00:00:00.000Z**. One day = **86400000** ms.
- [x] Default print is **`toString()`** (local). Also: `toDateString`, `toUTCString`, `toISOString`.

<a id="js-dates-example-01"></a>

### **Example 1: new Date() — current date and time**

- [x] `new Date()` with **no arguments** is **now** (local timezone when printed).
- [x] The W3Schools page repeats this Tryit; included **once**.
- [x] Date objects are **static snapshots** — the clock on the object is not running.

Sandbox: `code_sandbox/js-dates/new-date-now.html`

```javascript
const d = new Date();
```

![js-dates example 1 source](../code_sandbox/snaps/js-dates-01-code.png)

![js-dates example 1 result](../code_sandbox/snaps/js-dates-01-result.png)

- [x] **Outcome:** The snap shows the **browser's current local date/time** when it was taken (not a fake clock).

<a id="js-dates-example-02"></a>

### **Example 2: new Date("2022-03-25")**

- [x] A date-only **ISO** string (`YYYY-MM-DD`) is parsed as **UTC midnight**.
- [x] Local display may be the **previous evening** in US time zones. The page repeats this Tryit; included once.

Sandbox: `code_sandbox/js-dates/date-iso-string.html`

```javascript
const d = new Date("2022-03-25");
```

![js-dates example 2 source](../code_sandbox/snaps/js-dates-02-code.png)

![js-dates example 2 result](../code_sandbox/snaps/js-dates-02-result.png)

- [x] **Outcome:** A Date for **2022-03-25** (UTC). The printed string uses the **browser local** zone.

<a id="js-dates-example-03"></a>

### **Example 3: new Date("October 13, 2014 11:13:00")**

- [x] A **date string** is parsed by the Date constructor.
- [x] This form is treated as **local** time in most engines.

Sandbox: `code_sandbox/js-dates/date-long-string.html`

```javascript
const d = new Date("October 13, 2014 11:13:00");
```

![js-dates example 3 source](../code_sandbox/snaps/js-dates-03-code.png)

![js-dates example 3 result](../code_sandbox/snaps/js-dates-03-result.png)

- [x] **Outcome:** **October 13, 2014, 11:13:00** local (string form).

<a id="js-dates-example-04"></a>

### **Example 4: new Date(2018, 11, 24, 10, 33, 30, 0) — month 11 is December**

- [x] Seven numbers: **year, month, day, hours, minutes, seconds, ms**.
- [x] Months are **0–11**. **11** means **December**, not November.

Sandbox: `code_sandbox/js-dates/seven-numbers.html`

```javascript
const d = new Date(2018, 11, 24, 10, 33, 30, 0);
```

![js-dates example 4 source](../code_sandbox/snaps/js-dates-04-code.png)

![js-dates example 4 result](../code_sandbox/snaps/js-dates-04-result.png)

- [x] **Outcome:** **December 24, 2018, 10:33:30** local time.

<a id="js-dates-example-05"></a>

### **Example 5: new Date(2018, 15, ...) — month overflow to April 2019**

- [x] A month **greater than 11** does not error; it **overflows** into the next year.
- [x] Month **15** is 12 + 3 → **April 2019** (month 3).

Sandbox: `code_sandbox/js-dates/month-overflow.html`

```javascript
const d = new Date(2018, 15, 24, 10, 33, 30);
```

![js-dates example 5 source](../code_sandbox/snaps/js-dates-05-code.png)

![js-dates example 5 result](../code_sandbox/snaps/js-dates-05-result.png)

- [x] **Outcome:** **April 24, 2019, 10:33:30** local (overflow from month 15).

<a id="js-dates-example-06"></a>

### **Example 6: new Date(2019, 3, ...) — same as month overflow**

- [x] This is the **same instant** as `new Date(2018, 15, 24, 10, 33, 30)`.
- [x] Month **3** is **April**.

Sandbox: `code_sandbox/js-dates/month-overflow-equiv.html`

```javascript
const d = new Date(2019, 3, 24, 10, 33, 30);
```

![js-dates example 6 source](../code_sandbox/snaps/js-dates-06-code.png)

![js-dates example 6 result](../code_sandbox/snaps/js-dates-06-result.png)

- [x] **Outcome:** **April 24, 2019, 10:33:30** local — same as the overflow example.

<a id="js-dates-example-07"></a>

### **Example 7: new Date(2018, 5, 35, ...) — day overflow**

- [x] A **day** past the end of the month also overflows.
- [x] June has 30 days (month **5**). Day **35** is 5 days into **July**.

Sandbox: `code_sandbox/js-dates/day-overflow.html`

```javascript
const d = new Date(2018, 5, 35, 10, 33, 30);
```

![js-dates example 7 source](../code_sandbox/snaps/js-dates-07-code.png)

![js-dates example 7 result](../code_sandbox/snaps/js-dates-07-result.png)

- [x] **Outcome:** **July 5, 2018, 10:33:30** local.

<a id="js-dates-example-08"></a>

### **Example 8: new Date(2018, 6, 5, ...) — same as day overflow**

- [x] Month **6** is **July**. Same instant as `new Date(2018, 5, 35, ...)`.

Sandbox: `code_sandbox/js-dates/day-overflow-equiv.html`

```javascript
const d = new Date(2018, 6, 5, 10, 33, 30);
```

![js-dates example 8 source](../code_sandbox/snaps/js-dates-08-code.png)

![js-dates example 8 result](../code_sandbox/snaps/js-dates-08-result.png)

- [x] **Outcome:** **July 5, 2018, 10:33:30** local — same as the day-overflow example.

<a id="js-dates-example-09"></a>

### **Example 9: 6 numbers: year through seconds**

- [x] Six numbers omit milliseconds (they default to **0**).

Sandbox: `code_sandbox/js-dates/six-numbers.html`

```javascript
const d = new Date(2018, 11, 24, 10, 33, 30);
```

![js-dates example 9 source](../code_sandbox/snaps/js-dates-09-code.png)

![js-dates example 9 result](../code_sandbox/snaps/js-dates-09-result.png)

- [x] **Outcome:** **December 24, 2018, 10:33:30** local.

<a id="js-dates-example-10"></a>

### **Example 10: 5 numbers: year through minutes**

- [x] Five numbers: seconds default to **0**.

Sandbox: `code_sandbox/js-dates/five-numbers.html`

```javascript
const d = new Date(2018, 11, 24, 10, 33);
```

![js-dates example 10 source](../code_sandbox/snaps/js-dates-10-code.png)

![js-dates example 10 result](../code_sandbox/snaps/js-dates-10-result.png)

- [x] **Outcome:** **December 24, 2018, 10:33:00** local.

<a id="js-dates-example-11"></a>

### **Example 11: 4 numbers: year, month, day, hours**

- [x] Four numbers: minutes and seconds default to **0**.

Sandbox: `code_sandbox/js-dates/four-numbers.html`

```javascript
const d = new Date(2018, 11, 24, 10);
```

![js-dates example 11 source](../code_sandbox/snaps/js-dates-11-code.png)

![js-dates example 11 result](../code_sandbox/snaps/js-dates-11-result.png)

- [x] **Outcome:** **December 24, 2018, 10:00:00** local.

<a id="js-dates-example-12"></a>

### **Example 12: 3 numbers: year, month, day**

- [x] Three numbers: time defaults to **00:00:00** local.

Sandbox: `code_sandbox/js-dates/three-numbers.html`

```javascript
const d = new Date(2018, 11, 24);
```

![js-dates example 12 source](../code_sandbox/snaps/js-dates-12-code.png)

![js-dates example 12 result](../code_sandbox/snaps/js-dates-12-result.png)

- [x] **Outcome:** **December 24, 2018** at local midnight.

<a id="js-dates-example-13"></a>

### **Example 13: 2 numbers: year and month**

- [x] Two numbers: day defaults to **1**.
- [x] You **cannot** omit month. One argument is milliseconds, not a year.

Sandbox: `code_sandbox/js-dates/two-numbers.html`

```javascript
const d = new Date(2018, 11);
```

![js-dates example 13 source](../code_sandbox/snaps/js-dates-13-code.png)

![js-dates example 13 result](../code_sandbox/snaps/js-dates-13-result.png)

- [x] **Outcome:** **December 1, 2018** at local midnight.

<a id="js-dates-example-14"></a>

### **Example 14: 1 number: new Date(2018) is milliseconds, not year**

- [x] **One** argument is **milliseconds since the epoch**, not the year 2018.
- [x] 2018 ms after 1970-01-01 UTC is still **1 January 1970**.

Sandbox: `code_sandbox/js-dates/one-number-ms.html`

```javascript
const d = new Date(2018);
```

![js-dates example 14 source](../code_sandbox/snaps/js-dates-14-code.png)

![js-dates example 14 result](../code_sandbox/snaps/js-dates-14-result.png)

- [x] **Outcome:** **~2 seconds after** 1970-01-01 UTC (2018 milliseconds), **not** the year 2018.

<a id="js-dates-example-15"></a>

### **Example 15: new Date(99, 11, 24) → 1999**

- [x] Years **0–99** are treated as **19xx** (previous century).
- [x] **99** means **1999**.

Sandbox: `code_sandbox/js-dates/year-99.html`

```javascript
const d = new Date(99, 11, 24);
```

![js-dates example 15 source](../code_sandbox/snaps/js-dates-15-code.png)

![js-dates example 15 result](../code_sandbox/snaps/js-dates-15-result.png)

- [x] **Outcome:** **December 24, 1999**. `getFullYear()` is **1999**.

<a id="js-dates-example-16"></a>

### **Example 16: new Date(9, 11, 24) → 1909**

- [x] **9** is **1909**, not 2009 and not year 9.

Sandbox: `code_sandbox/js-dates/year-9.html`

```javascript
const d = new Date(9, 11, 24);
```

![js-dates example 16 source](../code_sandbox/snaps/js-dates-16-code.png)

![js-dates example 16 result](../code_sandbox/snaps/js-dates-16-result.png)

- [x] **Outcome:** **December 24, 1909**. `getFullYear()` is **1909**.

<a id="js-dates-example-17"></a>

### **Example 17: new Date(100000000000)**

- [x] Dates are stored as **ms since 1 January 1970 UTC** (the epoch).
- [x] 100 000 000 000 ms is that many milliseconds **after** the epoch.

Sandbox: `code_sandbox/js-dates/ms-positive.html`

```javascript
const d = new Date(100000000000);
```

![js-dates example 17 source](../code_sandbox/snaps/js-dates-17-code.png)

![js-dates example 17 result](../code_sandbox/snaps/js-dates-17-result.png)

- [x] **Outcome:** About **3 March 1973** UTC (plus local offset when printed).

<a id="js-dates-example-18"></a>

### **Example 18: new Date(-100000000000)**

- [x] A **negative** millisecond value is **before** the epoch.

Sandbox: `code_sandbox/js-dates/ms-negative.html`

```javascript
const d = new Date(-100000000000);
```

![js-dates example 18 source](../code_sandbox/snaps/js-dates-18-code.png)

![js-dates example 18 result](../code_sandbox/snaps/js-dates-18-result.png)

- [x] **Outcome:** About **31 October 1966** UTC (plus local offset when printed).

<a id="js-dates-example-19"></a>

### **Example 19: new Date(24*60*60\*1000) / 86400000**

- [x] One day is **86 400 000** ms (`24 * 60 * 60 * 1000`).
- [x] The page Tryit shows both forms; they are the **same** instant.

Sandbox: `code_sandbox/js-dates/one-day-ms.html`

```javascript
const d1 = new Date(24 * 60 * 60 * 1000);
const d2 = new Date(86400000);
```

![js-dates example 19 source](../code_sandbox/snaps/js-dates-19-code.png)

![js-dates example 19 result](../code_sandbox/snaps/js-dates-19-result.png)

- [x] **Outcome:** Both are **one day after** the epoch. The two constructors match.

<a id="js-dates-example-20"></a>

### **Example 20: new Date(0) — epoch**

- [x] **Zero time** is 1 January 1970 00:00:00 **UTC**.
- [x] Local `toString()` may show **31 December 1969** in US time zones.

Sandbox: `code_sandbox/js-dates/epoch-zero.html`

```javascript
const d = new Date(0);
```

![js-dates example 20 source](../code_sandbox/snaps/js-dates-20-code.png)

![js-dates example 20 result](../code_sandbox/snaps/js-dates-20-result.png)

- [x] **Outcome:** **Epoch.** `toISOString()` is **1970-01-01T00:00:00.000Z**.

<a id="js-dates-example-21"></a>

### **Example 21: d.toString()**

- [x] HTML and string conversion use **`toString()`** by default.
- [x] Includes **local** date, time, and time zone.

Sandbox: `code_sandbox/js-dates/to-string.html`

```javascript
const d = new Date();
d.toString();
```

![js-dates example 21 source](../code_sandbox/snaps/js-dates-21-code.png)

![js-dates example 21 result](../code_sandbox/snaps/js-dates-21-result.png)

- [x] **Outcome:** The snap shows the **browser's current local date/time** via **toString()**.

<a id="js-dates-example-22"></a>

### **Example 22: d.toDateString()**

- [x] `toDateString()` is a **shorter** readable date (no time).

Sandbox: `code_sandbox/js-dates/to-date-string.html`

```javascript
const d = new Date();
d.toDateString();
```

![js-dates example 22 source](../code_sandbox/snaps/js-dates-22-code.png)

![js-dates example 22 result](../code_sandbox/snaps/js-dates-22-result.png)

- [x] **Outcome:** The snap shows the **browser's current local date** (date part only).

<a id="js-dates-example-23"></a>

### **Example 23: d.toUTCString()**

- [x] `toUTCString()` formats the same instant in **UTC** (GMT).

Sandbox: `code_sandbox/js-dates/to-utc-string.html`

```javascript
const d = new Date();
d.toUTCString();
```

![js-dates example 23 source](../code_sandbox/snaps/js-dates-23-code.png)

![js-dates example 23 result](../code_sandbox/snaps/js-dates-23-result.png)

- [x] **Outcome:** The snap shows the **browser's current** instant as a **UTC** string.

<a id="js-dates-example-24"></a>

### **Example 24: d.toISOString()**

- [x] `toISOString()` is the **ISO 8601** UTC form (`...Z`).

Sandbox: `code_sandbox/js-dates/to-iso-string.html`

```javascript
const d = new Date();
d.toISOString();
```

![js-dates example 24 source](../code_sandbox/snaps/js-dates-24-code.png)

![js-dates example 24 result](../code_sandbox/snaps/js-dates-24-result.png)

- [x] **Outcome:** The snap shows the **browser's current** instant as **ISO UTC**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-dates/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does a Date object keep ticking?

<details>
<summary>Answer</summary>

- [x] **No.** It is a **snapshot**. The computer clock still ticks.

</details>

### Question 2: What is `new Date()`?

<details>
<summary>Answer</summary>

- [x] The **current** date and time in the **browser**. Snaps are not a fake clock.

</details>

### Question 3: What month is `11` in `new Date(2018, 11, 24, …)`?

<details>
<summary>Answer</summary>

- [x] **December.** Months are **0–11**.

</details>

### Question 4: What is `new Date(2018, 15, 24, 10, 33, 30)`?

<details>
<summary>Answer</summary>

- [x] **April 24, 2019** — month 15 overflows. Same as `new Date(2019, 3, 24, …)`.

</details>

### Question 5: What is `new Date(2018, 5, 35, …)`?

<details>
<summary>Answer</summary>

- [x] **July 5, 2018** — day 35 overflows June. Same as `new Date(2018, 6, 5, …)`.

</details>

### Question 6: What does one argument `new Date(2018)` mean?

<details>
<summary>Answer</summary>

- [x] **2018 milliseconds** after the epoch, **not** the year 2018.

</details>

### Question 7: What year is `new Date(99, 11, 24)`?

<details>
<summary>Answer</summary>

- [x] **1999**.

</details>

### Question 8: What year is `new Date(9, 11, 24)`?

<details>
<summary>Answer</summary>

- [x] **1909**.

</details>

### Question 9: What is `new Date(0)`?

<details>
<summary>Answer</summary>

- [x] The **epoch**: 1 January 1970 00:00:00 UTC.
- [x] Local `toString()` may show **31 Dec 1969** in US zones.

</details>

### Question 10: How many ms is one day?

<details>
<summary>Answer</summary>

- [x] **86400000**. `24 * 60 * 60 * 1000` is the same.

</details>

### Question 11: `toString` vs `toDateString` vs `toUTCString` vs `toISOString`?

<details>
<summary>Answer</summary>

- [x] **toString**: local date+time+zone.
- [x] **toDateString**: local date only.
- [x] **toUTCString**: UTC / GMT text.
- [x] **toISOString**: ISO 8601 UTC with `Z`.

</details>

### Question 12: Is `YYYY-MM-DD` local midnight?

<details>
<summary>Answer</summary>

- [x] **No.** Date-only ISO is **UTC midnight**, which can print as the **previous local evening**.

</details>

</details>

## Summary

Create dates with new Date, remember months start at zero, and expect overflow instead of errors. One number is milliseconds. Two-digit years are 19xx. The object is a frozen snapshot of an instant; formatting methods only change how that instant is printed.

## References

- [JS Dates (W3Schools)](https://www.w3schools.com/js/js_dates.asp)
- [MDN: Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
