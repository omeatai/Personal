# JS Date Set

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Set methods change parts of a Date object in place and return the new millisecond timestamp. Start from January 01, 2025 as the page does. setFullYear can set year only or year+month+day. Months are 0–11. setDate can add days through overflow (January 1 + 50 = February 20). setHours can also set minutes and seconds. Dates compare with > and <. setMilliseconds and setTime have no Tryit on the page; they still each get an Example. setTime(0) is the epoch.

This section has **12** examples:

- [x] **Example 1:** setFullYear(2020) on January 01, 2025 [View](#js-date-set-example-01)
- [x] **Example 2:** setFullYear(2020, 11, 3) [View](#js-date-set-example-02)
- [x] **Example 3:** setMonth(11) [View](#js-date-set-example-03)
- [x] **Example 4:** setDate(15) [View](#js-date-set-example-04)
- [x] **Example 5:** setDate(d.getDate() + 50) — add days [View](#js-date-set-example-05)
- [x] **Example 6:** setHours(22) [View](#js-date-set-example-06)
- [x] **Example 7:** setHours(22, 10, 20) [View](#js-date-set-example-07)
- [x] **Example 8:** setMinutes(30) [View](#js-date-set-example-08)
- [x] **Example 9:** setSeconds(30) [View](#js-date-set-example-09)
- [x] **Example 10:** Compare today vs January 14, 2100 [View](#js-date-set-example-10)
- [x] **Example 11:** setMilliseconds(500) — extra (table row, no Tryit) [View](#js-date-set-example-11)
- [x] **Example 12:** setTime(0) — epoch (extra; table row, no Tryit) [View](#js-date-set-example-12)

## Detailed Explanation

- [x] Set methods **mutate** the same Date. They use **local** fields (UTC setters live on the Methods reference page).
- [x] **Months 0–11.** `setFullYear(2020, 11, 3)` is **3 December 2020**.
- [x] `setDate(d.getDate() + n)` **adds days** and rolls the month/year automatically.
- [x] `setHours(h, min, sec)` can set more than the hour.
- [x] Compare Dates with **`>` / `<`**. January is month **0**.
- [x] `setTime(0)` is **1970-01-01T00:00:00.000Z** (local print may be **31 Dec 1969**).

<a id="js-date-set-example-01"></a>

### **Example 1: setFullYear(2020) on January 01, 2025**

- [x] `setFullYear(year)` sets the **local** year. Other fields stay put.
- [x] Start from `new Date("January 01, 2025")` as the page does.

Sandbox: `code_sandbox/js-date-set/set-full-year.html`

```javascript
const d = new Date("January 01, 2025");
d.setFullYear(2020);
```

![js-date-set example 1 source](../code_sandbox/snaps/js-date-set-01-code.png)

![js-date-set example 1 result](../code_sandbox/snaps/js-date-set-01-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 01 2020 00:00:00 GMT-0700**.

<a id="js-date-set-example-02"></a>

### **Example 2: setFullYear(2020, 11, 3)**

- [x] `setFullYear` can also set **month** and **day**.
- [x] Month **11** is **December** (0–11).

Sandbox: `code_sandbox/js-date-set/set-full-year-ymd.html`

```javascript
const d = new Date("January 01, 2025");
d.setFullYear(2020, 11, 3);
```

![js-date-set example 2 source](../code_sandbox/snaps/js-date-set-02-code.png)

![js-date-set example 2 result](../code_sandbox/snaps/js-date-set-02-result.png)

- [x] **Outcome:** After the set, d is **Thu Dec 03 2020 00:00:00 GMT-0700**.

<a id="js-date-set-example-03"></a>

### **Example 3: setMonth(11)**

- [x] `setMonth(month)` uses **0–11**. **11** is December.

Sandbox: `code_sandbox/js-date-set/set-month.html`

```javascript
const d = new Date("January 01, 2025");
d.setMonth(11);
```

![js-date-set example 3 source](../code_sandbox/snaps/js-date-set-03-code.png)

![js-date-set example 3 result](../code_sandbox/snaps/js-date-set-03-result.png)

- [x] **Outcome:** After the set, d is **Mon Dec 01 2025 00:00:00 GMT-0700**.

<a id="js-date-set-example-04"></a>

### **Example 4: setDate(15)**

- [x] `setDate(day)` sets the **day of month** (1–31), local.

Sandbox: `code_sandbox/js-date-set/set-date.html`

```javascript
const d = new Date("January 01, 2025");
d.setDate(15);
```

![js-date-set example 4 source](../code_sandbox/snaps/js-date-set-04-code.png)

![js-date-set example 4 result](../code_sandbox/snaps/js-date-set-04-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 15 2025 00:00:00 GMT-0700**.

<a id="js-date-set-example-05"></a>

### **Example 5: setDate(d.getDate() + 50) — add days**

- [x] You can **add days** with `setDate(d.getDate() + n)`.
- [x] Overflow into the next month/year is handled automatically.

Sandbox: `code_sandbox/js-date-set/set-date-add-50.html`

```javascript
const d = new Date("January 01, 2025");
d.setDate(d.getDate() + 50);
```

![js-date-set example 5 source](../code_sandbox/snaps/js-date-set-05-code.png)

![js-date-set example 5 result](../code_sandbox/snaps/js-date-set-05-result.png)

- [x] **Outcome:** January 1 + 50 days is **Thu Feb 20 2025 00:00:00 GMT-0700**.

<a id="js-date-set-example-06"></a>

### **Example 6: setHours(22)**

- [x] `setHours(hour)` sets the local hour **0–23**.

Sandbox: `code_sandbox/js-date-set/set-hours.html`

```javascript
const d = new Date("January 01, 2025");
d.setHours(22);
```

![js-date-set example 6 source](../code_sandbox/snaps/js-date-set-06-code.png)

![js-date-set example 6 result](../code_sandbox/snaps/js-date-set-06-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 01 2025 22:00:00 GMT-0700**.

<a id="js-date-set-example-07"></a>

### **Example 7: setHours(22, 10, 20)**

- [x] `setHours` can also set **minutes** and **seconds**.

Sandbox: `code_sandbox/js-date-set/set-hours-hms.html`

```javascript
const d = new Date("January 01, 2025");
d.setHours(22, 10, 20);
```

![js-date-set example 7 source](../code_sandbox/snaps/js-date-set-07-code.png)

![js-date-set example 7 result](../code_sandbox/snaps/js-date-set-07-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 01 2025 22:10:20 GMT-0700**.

<a id="js-date-set-example-08"></a>

### **Example 8: setMinutes(30)**

- [x] `setMinutes(min)` sets local minutes **0–59**.

Sandbox: `code_sandbox/js-date-set/set-minutes.html`

```javascript
const d = new Date("January 01, 2025");
d.setMinutes(30);
```

![js-date-set example 8 source](../code_sandbox/snaps/js-date-set-08-code.png)

![js-date-set example 8 result](../code_sandbox/snaps/js-date-set-08-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 01 2025 00:30:00 GMT-0700**.

<a id="js-date-set-example-09"></a>

### **Example 9: setSeconds(30)**

- [x] `setSeconds(sec)` sets local seconds **0–59**.

Sandbox: `code_sandbox/js-date-set/set-seconds.html`

```javascript
const d = new Date("January 01, 2025");
d.setSeconds(30);
```

![js-date-set example 9 source](../code_sandbox/snaps/js-date-set-09-code.png)

![js-date-set example 9 result](../code_sandbox/snaps/js-date-set-09-result.png)

- [x] **Outcome:** After the set, d is **Wed Jan 01 2025 00:00:30 GMT-0700**.

<a id="js-date-set-example-10"></a>

### **Example 10: Compare today vs January 14, 2100**

- [x] Date objects compare with **`>` / `<`** (they use their millisecond values).
- [x] January is month **0**. `setFullYear(2100, 0, 14)` is January 14, 2100.

Sandbox: `code_sandbox/js-date-set/compare-today-2100.html`

```javascript
let text = "";
const today = new Date();
const someday = new Date();
someday.setFullYear(2100, 0, 14);
if (someday > today) {
  text = "Today is before January 14, 2100.";
} else {
  text = "Today is after January 14, 2100.";
}
```

![js-date-set example 10 source](../code_sandbox/snaps/js-date-set-10-code.png)

![js-date-set example 10 result](../code_sandbox/snaps/js-date-set-10-result.png)

- [x] **Outcome:** text is **"Today is before January 14, 2100."** (the snap’s `today` is the **browser's current local** time).

<a id="js-date-set-example-11"></a>

### **Example 11: setMilliseconds(500) — extra (table row, no Tryit)**

- [x] `setMilliseconds(ms)` sets local milliseconds **0–999**.
- [x] No Tryit on the page — still run it. `toString()` may hide ms; print `getMilliseconds()`.

Sandbox: `code_sandbox/js-date-set/set-milliseconds.html`

```javascript
const d = new Date("January 01, 2025");
d.setMilliseconds(500);
```

![js-date-set example 11 source](../code_sandbox/snaps/js-date-set-11-code.png)

![js-date-set example 11 result](../code_sandbox/snaps/js-date-set-11-result.png)

- [x] **Outcome:** `getMilliseconds()` is **500**. ISO is **2025-01-01T07:00:00.500Z**.

<a id="js-date-set-example-12"></a>

### **Example 12: setTime(0) — epoch (extra; table row, no Tryit)**

- [x] `setTime(ms)` sets the instant as milliseconds since **1 January 1970 UTC**.
- [x] **0** is the epoch. Local `toString()` may show **31 December 1969** in US zones.

Sandbox: `code_sandbox/js-date-set/set-time-epoch.html`

```javascript
const d = new Date("January 01, 2025");
d.setTime(0);
```

![js-date-set example 12 source](../code_sandbox/snaps/js-date-set-12-code.png)

![js-date-set example 12 result](../code_sandbox/snaps/js-date-set-12-result.png)

- [x] **Outcome:** `getTime()` is **0**. ISO is **1970-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 1969 17:00:00 GMT-0700**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-date-set/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `setFullYear(2020)` do to January 01, 2025?

<details>
<summary>Answer</summary>

- [x] The date becomes **January 1, 2020** local midnight.

</details>

### Question 2: What is `setFullYear(2020, 11, 3)`?

<details>
<summary>Answer</summary>

- [x] **December 3, 2020.** Month **11** is December.

</details>

### Question 3: What is `setMonth(11)` on January 1, 2025?

<details>
<summary>Answer</summary>

- [x] **December 1, 2025**.

</details>

### Question 4: What is `setDate(15)` on that start date?

<details>
<summary>Answer</summary>

- [x] **January 15, 2025**.

</details>

### Question 5: What is `setDate(d.getDate() + 50)` from January 1?

<details>
<summary>Answer</summary>

- [x] **February 20, 2025**. Overflow is automatic.

</details>

### Question 6: What does `setHours(22, 10, 20)` set?

<details>
<summary>Answer</summary>

- [x] Hour **22**, minutes **10**, seconds **20** on the same local day.

</details>

### Question 7: How do you compare dates?

<details>
<summary>Answer</summary>

- [x] With **`>` / `<`** (millisecond instants).
- [x] In 2026, today is **before** January 14, 2100.

</details>

### Question 8: What month number is January when setting?

<details>
<summary>Answer</summary>

- [x] **0.** December is **11**.

</details>

### Question 9: Did setMilliseconds have a Tryit?

<details>
<summary>Answer</summary>

- [x] **No.** Still run: `setMilliseconds(500)` → `getMilliseconds()` **500**.

</details>

### Question 10: What is `setTime(0)`?

<details>
<summary>Answer</summary>

- [x] The **epoch**. ISO **1970-01-01T00:00:00.000Z**.
- [x] Local print here is **Wed Dec 31 1969 17:00:00 GMT-0700**.

</details>

### Question 11: Do set methods return a new Date?

<details>
<summary>Answer</summary>

- [x] They mutate **the same object** and return the new **ms** timestamp (this sandbox prints the Date after the set).

</details>

</details>

## Summary

Mutate a Date with setFullYear, setMonth, setDate, and the time setters. Months start at zero. Adding days through setDate overflows cleanly. setTime(0) is the epoch. Compare two Dates as instants.

## References

- [JS Date Set (W3Schools)](https://www.w3schools.com/js/js_date_methods_set.asp)
- [MDN: Date.prototype.setFullYear](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)
- [MDN: Date.prototype.setTime](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime)
