# JS Date Get

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Get methods read pieces of an existing Date as local time unless the name starts with UTC. new Date() is now; getFullYear, getMonth (0–11), getDate (day of month), getDay (weekday, Sunday = 0), and the time getters return local fields. Date-only ISO like 2021-03-25 is UTC midnight, so in Mountain time getDate is 24, getHours is 18, and getDay is Wednesday — not the UTC Thursday the 25th. getTime and Date.now count milliseconds since 1 January 1970 UTC. getYear is deprecated. The UTC table has no Tryits on the page; each row still has its own Example on the same fixed Date.

This section has **36** examples:

- [x] **Example 1:** new Date() — current time [View](#js-date-get-example-01)
- [x] **Example 2:** getFullYear() on "2021-03-25" [View](#js-date-get-example-02)
- [x] **Example 3:** getFullYear() on now [View](#js-date-get-example-03)
- [x] **Example 4:** getMonth() on "2021-03-25" [View](#js-date-get-example-04)
- [x] **Example 5:** getMonth() on now [View](#js-date-get-example-05)
- [x] **Example 6:** months[d.getMonth()] on "2021-03-25" [View](#js-date-get-example-06)
- [x] **Example 7:** months[d.getMonth()] on now [View](#js-date-get-example-07)
- [x] **Example 8:** getDate() on "2021-03-25" [View](#js-date-get-example-08)
- [x] **Example 9:** getDate() on now [View](#js-date-get-example-09)
- [x] **Example 10:** getHours() on "2021-03-25" [View](#js-date-get-example-10)
- [x] **Example 11:** getHours() on now [View](#js-date-get-example-11)
- [x] **Example 12:** getMinutes() on "2021-03-25" [View](#js-date-get-example-12)
- [x] **Example 13:** getMinutes() on now [View](#js-date-get-example-13)
- [x] **Example 14:** getSeconds() on "2021-03-25" [View](#js-date-get-example-14)
- [x] **Example 15:** getSeconds() on now [View](#js-date-get-example-15)
- [x] **Example 16:** getMilliseconds() on "2021-03-25" [View](#js-date-get-example-16)
- [x] **Example 17:** getMilliseconds() on now [View](#js-date-get-example-17)
- [x] **Example 18:** getDay() on "2021-03-25" [View](#js-date-get-example-18)
- [x] **Example 19:** getDay() on now [View](#js-date-get-example-19)
- [x] **Example 20:** days[d.getDay()] on "2021-03-25" [View](#js-date-get-example-20)
- [x] **Example 21:** days[d.getDay()] on now [View](#js-date-get-example-21)
- [x] **Example 22:** getTime() on "1970-01-01" [View](#js-date-get-example-22)
- [x] **Example 23:** getTime() on "2021-03-25" [View](#js-date-get-example-23)
- [x] **Example 24:** getTime() on now [View](#js-date-get-example-24)
- [x] **Example 25:** Date.now() [View](#js-date-get-example-25)
- [x] **Example 26:** Years since 1970 (page formula) [View](#js-date-get-example-26)
- [x] **Example 27:** getTimezoneOffset() [View](#js-date-get-example-27)
- [x] **Example 28:** getYear() — deprecated; use getFullYear() [View](#js-date-get-example-28)
- [x] **Example 29:** getUTCDate() [View](#js-date-get-example-29)
- [x] **Example 30:** getUTCFullYear() [View](#js-date-get-example-30)
- [x] **Example 31:** getUTCMonth() [View](#js-date-get-example-31)
- [x] **Example 32:** getUTCDay() [View](#js-date-get-example-32)
- [x] **Example 33:** getUTCHours() [View](#js-date-get-example-33)
- [x] **Example 34:** getUTCMinutes() [View](#js-date-get-example-34)
- [x] **Example 35:** getUTCSeconds() [View](#js-date-get-example-35)
- [x] **Example 36:** getUTCMilliseconds() [View](#js-date-get-example-36)

## Detailed Explanation

- [x] Get methods return **local** time unless the name is **`getUTC*`**.
- [x] **Months 0–11**, **weekdays 0–6** (Sunday first). Name arrays index those numbers.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day. On `"2021-03-25"` this zone: `getDate()` **24**, `getHours()` **18**, `getDay()` **3** (Wednesday).
- [x] `getTime()` / `Date.now()` are ms since **1970-01-01T00:00:00.000Z**. `getTime()` on that ISO date-only string is **0**.
- [x] `Date.now()` is **static** — not `d.now()`.
- [x] **`getYear()` is deprecated.** This engine returned **121** for 2021. Use **`getFullYear()`**.

<a id="js-date-get-example-01"></a>

### **Example 1: new Date() — current time**

- [x] `new Date()` returns a Date for **now** (local when printed).
- [x] The object is a **snapshot** — its clock does not keep ticking.

Sandbox: `code_sandbox/js-date-get/new-date-now.html`

```javascript
const d = new Date();
```

![js-date-get example 1 source](../code_sandbox/snaps/js-date-get-01-code.png)

![js-date-get example 1 result](../code_sandbox/snaps/js-date-get-01-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** date/time (not a hardcoded fake clock).

<a id="js-date-get-example-02"></a>

### **Example 2: getFullYear() on "2021-03-25"**

- [x] `getFullYear()` is a **four-digit** local year.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day.

Sandbox: `code_sandbox/js-date-get/get-full-year-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getFullYear();
```

![js-date-get example 2 source](../code_sandbox/snaps/js-date-get-02-code.png)

![js-date-get example 2 result](../code_sandbox/snaps/js-date-get-02-result.png)

- [x] **Outcome:** `getFullYear()` is **2021**. Local print is **Wed Mar 24 2021 18:00:00 GMT-0600** — year did not roll back.

<a id="js-date-get-example-03"></a>

### **Example 3: getFullYear() on now**

- [x] Same method on **`new Date()`** (current local year).

Sandbox: `code_sandbox/js-date-get/get-full-year-now.html`

```javascript
const d = new Date();
d.getFullYear();
```

![js-date-get example 3 source](../code_sandbox/snaps/js-date-get-03-code.png)

![js-date-get example 3 result](../code_sandbox/snaps/js-date-get-03-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** four-digit year.

<a id="js-date-get-example-04"></a>

### **Example 4: getMonth() on "2021-03-25"**

- [x] `getMonth()` is **0–11**. January is **0**, March is **2**, December is **11**.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day.

Sandbox: `code_sandbox/js-date-get/get-month-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getMonth();
```

![js-date-get example 4 source](../code_sandbox/snaps/js-date-get-04-code.png)

![js-date-get example 4 result](../code_sandbox/snaps/js-date-get-04-result.png)

- [x] **Outcome:** `getMonth()` is **2** (March). Local calendar day is the **24th**, still in March.

<a id="js-date-get-example-05"></a>

### **Example 5: getMonth() on now**

- [x] Current local month as **0–11**.

Sandbox: `code_sandbox/js-date-get/get-month-now.html`

```javascript
const d = new Date();
d.getMonth();
```

![js-date-get example 5 source](../code_sandbox/snaps/js-date-get-05-code.png)

![js-date-get example 5 result](../code_sandbox/snaps/js-date-get-05-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** month number (0–11).

<a id="js-date-get-example-06"></a>

### **Example 6: months[d.getMonth()] on "2021-03-25"**

- [x] Index a **names** array with `getMonth()` to print the month word.

Sandbox: `code_sandbox/js-date-get/month-name-fixed.html`

```javascript
const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const d = new Date("2021-03-25");
let month = months[d.getMonth()];
```

![js-date-get example 6 source](../code_sandbox/snaps/js-date-get-06-code.png)

![js-date-get example 6 result](../code_sandbox/snaps/js-date-get-06-result.png)

- [x] **Outcome:** month is **"March"** (index **2**), even though local `getDate()` is **24**.

<a id="js-date-get-example-07"></a>

### **Example 7: months[d.getMonth()] on now**

- [x] Same names array on the **current** date.

Sandbox: `code_sandbox/js-date-get/month-name-now.html`

```javascript
const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const d = new Date();
let month = months[d.getMonth()];
```

![js-date-get example 7 source](../code_sandbox/snaps/js-date-get-07-code.png)

![js-date-get example 7 result](../code_sandbox/snaps/js-date-get-07-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** month **name**.

<a id="js-date-get-example-08"></a>

### **Example 8: getDate() on "2021-03-25"**

- [x] `getDate()` is the **day of the month** (1–31), **local**.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day. The page’s Tryit can look like the 25th in UTC zones.

Sandbox: `code_sandbox/js-date-get/get-date-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getDate();
```

![js-date-get example 8 source](../code_sandbox/snaps/js-date-get-08-code.png)

![js-date-get example 8 result](../code_sandbox/snaps/js-date-get-08-result.png)

- [x] **Outcome:** `getDate()` is **24**, not 25. `2021-03-25` is UTC midnight = **March 24, 18:00** Mountain.

<a id="js-date-get-example-09"></a>

### **Example 9: getDate() on now**

- [x] Current local **day of month** (1–31).

Sandbox: `code_sandbox/js-date-get/get-date-now.html`

```javascript
const d = new Date();
d.getDate();
```

![js-date-get example 9 source](../code_sandbox/snaps/js-date-get-09-code.png)

![js-date-get example 9 result](../code_sandbox/snaps/js-date-get-09-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** day of the month.

<a id="js-date-get-example-10"></a>

### **Example 10: getHours() on "2021-03-25"**

- [x] `getHours()` is **0–23**, **local**.
- [x] UTC midnight is evening the day before in US zones.

Sandbox: `code_sandbox/js-date-get/get-hours-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getHours();
```

![js-date-get example 10 source](../code_sandbox/snaps/js-date-get-10-code.png)

![js-date-get example 10 result](../code_sandbox/snaps/js-date-get-10-result.png)

- [x] **Outcome:** `getHours()` is **18** (6 PM Mountain), not 0. UTC hours would be **0** (`getUTCHours()`).

<a id="js-date-get-example-11"></a>

### **Example 11: getHours() on now**

- [x] Current local hour **0–23**.

Sandbox: `code_sandbox/js-date-get/get-hours-now.html`

```javascript
const d = new Date();
d.getHours();
```

![js-date-get example 11 source](../code_sandbox/snaps/js-date-get-11-code.png)

![js-date-get example 11 result](../code_sandbox/snaps/js-date-get-11-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** hour.

<a id="js-date-get-example-12"></a>

### **Example 12: getMinutes() on "2021-03-25"**

- [x] `getMinutes()` is **0–59**, **local**.

Sandbox: `code_sandbox/js-date-get/get-minutes-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getMinutes();
```

![js-date-get example 12 source](../code_sandbox/snaps/js-date-get-12-code.png)

![js-date-get example 12 result](../code_sandbox/snaps/js-date-get-12-result.png)

- [x] **Outcome:** `getMinutes()` is **0** (UTC midnight has zero minutes).

<a id="js-date-get-example-13"></a>

### **Example 13: getMinutes() on now**

- [x] Current local minutes **0–59**.

Sandbox: `code_sandbox/js-date-get/get-minutes-now.html`

```javascript
const d = new Date();
d.getMinutes();
```

![js-date-get example 13 source](../code_sandbox/snaps/js-date-get-13-code.png)

![js-date-get example 13 result](../code_sandbox/snaps/js-date-get-13-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** minutes.

<a id="js-date-get-example-14"></a>

### **Example 14: getSeconds() on "2021-03-25"**

- [x] `getSeconds()` is **0–59**, **local**.

Sandbox: `code_sandbox/js-date-get/get-seconds-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getSeconds();
```

![js-date-get example 14 source](../code_sandbox/snaps/js-date-get-14-code.png)

![js-date-get example 14 result](../code_sandbox/snaps/js-date-get-14-result.png)

- [x] **Outcome:** `getSeconds()` is **0**.

<a id="js-date-get-example-15"></a>

### **Example 15: getSeconds() on now**

- [x] Current local seconds **0–59**.

Sandbox: `code_sandbox/js-date-get/get-seconds-now.html`

```javascript
const d = new Date();
d.getSeconds();
```

![js-date-get example 15 source](../code_sandbox/snaps/js-date-get-15-code.png)

![js-date-get example 15 result](../code_sandbox/snaps/js-date-get-15-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** seconds.

<a id="js-date-get-example-16"></a>

### **Example 16: getMilliseconds() on "2021-03-25"**

- [x] `getMilliseconds()` is **0–999**, **local**.

Sandbox: `code_sandbox/js-date-get/get-milliseconds-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getMilliseconds();
```

![js-date-get example 16 source](../code_sandbox/snaps/js-date-get-16-code.png)

![js-date-get example 16 result](../code_sandbox/snaps/js-date-get-16-result.png)

- [x] **Outcome:** `getMilliseconds()` is **0**.

<a id="js-date-get-example-17"></a>

### **Example 17: getMilliseconds() on now**

- [x] Current local milliseconds **0–999**.

Sandbox: `code_sandbox/js-date-get/get-milliseconds-now.html`

```javascript
const d = new Date();
d.getMilliseconds();
```

![js-date-get example 17 source](../code_sandbox/snaps/js-date-get-17-code.png)

![js-date-get example 17 result](../code_sandbox/snaps/js-date-get-17-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** milliseconds.

<a id="js-date-get-example-18"></a>

### **Example 18: getDay() on "2021-03-25"**

- [x] `getDay()` is the **weekday** **0–6**. **0 is Sunday** (not Monday).
- [x] UTC March 25 2021 was **Thursday** (4). Local March 24 was **Wednesday** (3).

Sandbox: `code_sandbox/js-date-get/get-day-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getDay();
```

![js-date-get example 18 source](../code_sandbox/snaps/js-date-get-18-code.png)

![js-date-get example 18 result](../code_sandbox/snaps/js-date-get-18-result.png)

- [x] **Outcome:** `getDay()` is **3** (Wednesday) because local time is **March 24**, not the UTC Thursday.

<a id="js-date-get-example-19"></a>

### **Example 19: getDay() on now**

- [x] Current local weekday number **0–6** (Sunday = 0).

Sandbox: `code_sandbox/js-date-get/get-day-now.html`

```javascript
const d = new Date();
d.getDay();
```

![js-date-get example 19 source](../code_sandbox/snaps/js-date-get-19-code.png)

![js-date-get example 19 result](../code_sandbox/snaps/js-date-get-19-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** weekday number.

<a id="js-date-get-example-20"></a>

### **Example 20: days[d.getDay()] on "2021-03-25"**

- [x] Index a weekday-names array with `getDay()`.

Sandbox: `code_sandbox/js-date-get/day-name-fixed.html`

```javascript
const days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];
const d = new Date("2021-03-25");
let day = days[d.getDay()];
```

![js-date-get example 20 source](../code_sandbox/snaps/js-date-get-20-code.png)

![js-date-get example 20 result](../code_sandbox/snaps/js-date-get-20-result.png)

- [x] **Outcome:** day is **"Wednesday"** (local Mar 24), not Thursday (UTC Mar 25).

<a id="js-date-get-example-21"></a>

### **Example 21: days[d.getDay()] on now**

- [x] Same names array on **now**.

Sandbox: `code_sandbox/js-date-get/day-name-now.html`

```javascript
const days = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];
const d = new Date();
let day = days[d.getDay()];
```

![js-date-get example 21 source](../code_sandbox/snaps/js-date-get-21-code.png)

![js-date-get example 21 result](../code_sandbox/snaps/js-date-get-21-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** weekday **name**.

<a id="js-date-get-example-22"></a>

### **Example 22: getTime() on "1970-01-01"**

- [x] `getTime()` is milliseconds since **1 January 1970 UTC** (the epoch).
- [x] `"1970-01-01"` is UTC midnight, so the count is **0** even if local print is Dec 31 1969.

Sandbox: `code_sandbox/js-date-get/get-time-epoch.html`

```javascript
const d = new Date("1970-01-01");
d.getTime();
```

![js-date-get example 22 source](../code_sandbox/snaps/js-date-get-22-code.png)

![js-date-get example 22 result](../code_sandbox/snaps/js-date-get-22-result.png)

- [x] **Outcome:** `getTime()` is **0**. ISO is **1970-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 1969 17:00:00 GMT-0700**.

<a id="js-date-get-example-23"></a>

### **Example 23: getTime() on "2021-03-25"**

- [x] Milliseconds from the epoch to this UTC midnight.

Sandbox: `code_sandbox/js-date-get/get-time-fixed.html`

```javascript
const d = new Date("2021-03-25");
d.getTime();
```

![js-date-get example 23 source](../code_sandbox/snaps/js-date-get-23-code.png)

![js-date-get example 23 result](../code_sandbox/snaps/js-date-get-23-result.png)

- [x] **Outcome:** `getTime()` is **1616630400000** (`2021-03-25T00:00:00.000Z`).

<a id="js-date-get-example-24"></a>

### **Example 24: getTime() on now**

- [x] `getTime()` on `new Date()` is the current epoch offset (ms).

Sandbox: `code_sandbox/js-date-get/get-time-now.html`

```javascript
const d = new Date();
d.getTime();
```

![js-date-get example 24 source](../code_sandbox/snaps/js-date-get-24-code.png)

![js-date-get example 24 result](../code_sandbox/snaps/js-date-get-24-result.png)

- [x] **Outcome:** The snap shows the **browser's current** millisecond timestamp (not a fake clock).

<a id="js-date-get-example-25"></a>

### **Example 25: Date.now()**

- [x] `Date.now()` is a **static** method: milliseconds since the epoch **right now**.
- [x] There is no `myDate.now()` — the syntax is always **`Date.now()`**.

Sandbox: `code_sandbox/js-date-get/date-now.html`

```javascript
let ms = Date.now();
```

![js-date-get example 25 source](../code_sandbox/snaps/js-date-get-25-code.png)

![js-date-get example 25 result](../code_sandbox/snaps/js-date-get-25-result.png)

- [x] **Outcome:** The snap shows the **browser's current** `Date.now()` value.

<a id="js-date-get-example-26"></a>

### **Example 26: Years since 1970 (page formula)**

- [x] The page approximates years as **365-day** chunks (no leap days).
- [x] `Math.round(Date.now() / year)` is a rough year count, not a calendar year.

Sandbox: `code_sandbox/js-date-get/years-since-1970.html`

```javascript
const minute = 1000 * 60;
const hour = minute * 60;
const day = hour * 24;
const year = day * 365;
let years = Math.round(Date.now() / year);
```

![js-date-get example 26 source](../code_sandbox/snaps/js-date-get-26-code.png)

![js-date-get example 26 result](../code_sandbox/snaps/js-date-get-26-result.png)

- [x] **Outcome:** The snap shows the **browser's current** rounded 365-day year count since 1970 (about **56** in 2026). It is not `getFullYear() - 1970`.

<a id="js-date-get-example-27"></a>

### **Example 27: getTimezoneOffset()**

- [x] `getTimezoneOffset()` is **minutes** to add to **local** time to get **UTC**.
- [x] West of UTC the value is **positive** (Mountain daylight = **360**).

Sandbox: `code_sandbox/js-date-get/get-timezone-offset.html`

```javascript
const d = new Date();
let diff = d.getTimezoneOffset();
```

![js-date-get example 27 source](../code_sandbox/snaps/js-date-get-27-code.png)

![js-date-get example 27 result](../code_sandbox/snaps/js-date-get-27-result.png)

- [x] **Outcome:** The snap shows the **browser's current local** offset in minutes (this Mountain daylight zone prints **360**).

<a id="js-date-get-example-28"></a>

### **Example 28: getYear() — deprecated; use getFullYear()**

- [x] **Deprecated.** Old engines used `getYear()` (often **year − 1900**).
- [x] **Do not use it.** Use **`getFullYear()`**.

Sandbox: `code_sandbox/js-date-get/get-year-deprecated.html`

```javascript
const d = new Date("2021-03-25");
d.getYear();
d.getFullYear();
```

![js-date-get example 28 source](../code_sandbox/snaps/js-date-get-28-code.png)

![js-date-get example 28 result](../code_sandbox/snaps/js-date-get-28-result.png)

- [x] **Outcome:** `getYear()` is **121** (2021 − 1900). `getFullYear()` is **2021**. Do **not** use `getYear()`.

<a id="js-date-get-example-29"></a>

### **Example 29: getUTCDate()**

- [x] UTC day of month (1–31). Same idea as getDate() but UTC.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-date.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCDate();
```

![js-date-get example 29 source](../code_sandbox/snaps/js-date-get-29-code.png)

![js-date-get example 29 result](../code_sandbox/snaps/js-date-get-29-result.png)

- [x] **Outcome:** `getUTCDate()` is **25**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-30"></a>

### **Example 30: getUTCFullYear()**

- [x] UTC four-digit year.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-full-year.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCFullYear();
```

![js-date-get example 30 source](../code_sandbox/snaps/js-date-get-30-code.png)

![js-date-get example 30 result](../code_sandbox/snaps/js-date-get-30-result.png)

- [x] **Outcome:** `getUTCFullYear()` is **2021**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-31"></a>

### **Example 31: getUTCMonth()**

- [x] UTC month 0–11. March is 2.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-month.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCMonth();
```

![js-date-get example 31 source](../code_sandbox/snaps/js-date-get-31-code.png)

![js-date-get example 31 result](../code_sandbox/snaps/js-date-get-31-result.png)

- [x] **Outcome:** `getUTCMonth()` is **2**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-32"></a>

### **Example 32: getUTCDay()**

- [x] UTC weekday 0–6. March 25 2021 UTC was Thursday (4).
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-day.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCDay();
```

![js-date-get example 32 source](../code_sandbox/snaps/js-date-get-32-code.png)

![js-date-get example 32 result](../code_sandbox/snaps/js-date-get-32-result.png)

- [x] **Outcome:** `getUTCDay()` is **4**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-33"></a>

### **Example 33: getUTCHours()**

- [x] UTC hour 0–23. Date-only ISO is midnight UTC.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-hours.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCHours();
```

![js-date-get example 33 source](../code_sandbox/snaps/js-date-get-33-code.png)

![js-date-get example 33 result](../code_sandbox/snaps/js-date-get-33-result.png)

- [x] **Outcome:** `getUTCHours()` is **0**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-34"></a>

### **Example 34: getUTCMinutes()**

- [x] UTC minutes 0–59.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-minutes.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCMinutes();
```

![js-date-get example 34 source](../code_sandbox/snaps/js-date-get-34-code.png)

![js-date-get example 34 result](../code_sandbox/snaps/js-date-get-34-result.png)

- [x] **Outcome:** `getUTCMinutes()` is **0**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-35"></a>

### **Example 35: getUTCSeconds()**

- [x] UTC seconds 0–59.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-seconds.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCSeconds();
```

![js-date-get example 35 source](../code_sandbox/snaps/js-date-get-35-code.png)

![js-date-get example 35 result](../code_sandbox/snaps/js-date-get-35-result.png)

- [x] **Outcome:** `getUTCSeconds()` is **0**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<a id="js-date-get-example-36"></a>

### **Example 36: getUTCMilliseconds()**

- [x] UTC milliseconds 0–999.
- [x] No Tryit on the page — still run on `new Date("2021-03-25")` (UTC midnight).

Sandbox: `code_sandbox/js-date-get/get-utc-milliseconds.html`

```javascript
const d = new Date("2021-03-25");
d.getUTCMilliseconds();
```

![js-date-get example 36 source](../code_sandbox/snaps/js-date-get-36-code.png)

![js-date-get example 36 result](../code_sandbox/snaps/js-date-get-36-result.png)

- [x] **Outcome:** `getUTCMilliseconds()` is **0**. ISO is **2021-03-25T00:00:00.000Z**. Local getters on the same object can disagree (see getDate / getHours / getDay).

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-date-get/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Does a Date object keep ticking?

<details>
<summary>Answer</summary>

- [x] **No.** Get methods read a **static snapshot**.

</details>

### Question 2: What is `getMonth()` for March?

<details>
<summary>Answer</summary>

- [x] **2.** January is **0**, December is **11**.

</details>

### Question 3: What is `getDate()` on `new Date("2021-03-25")` here?

<details>
<summary>Answer</summary>

- [x] **24**, not 25.
- [x] Date-only ISO is **UTC midnight** = **March 24, 18:00** Mountain.

</details>

### Question 4: What is `getHours()` on that same Date?

<details>
<summary>Answer</summary>

- [x] **18** local. `getUTCHours()` is **0**.

</details>

### Question 5: What is `getDay()` on that Date locally vs UTC?

<details>
<summary>Answer</summary>

- [x] Local **3** (Wednesday, Mar 24).
- [x] UTC **4** (Thursday, Mar 25). **0 is Sunday**.

</details>

### Question 6: What is `months[d.getMonth()]` on that Date?

<details>
<summary>Answer</summary>

- [x] **"March"** — still March even though `getDate()` is 24.

</details>

### Question 7: What is `getTime()` of `new Date("1970-01-01")`?

<details>
<summary>Answer</summary>

- [x] **0.** ISO is **1970-01-01T00:00:00.000Z**.
- [x] Local print may be **31 Dec 1969**.

</details>

### Question 8: Can you call `d.now()`?

<details>
<summary>Answer</summary>

- [x] **No.** `Date.now()` is **static** on `Date`.

</details>

### Question 9: What does the years-since-1970 formula use?

<details>
<summary>Answer</summary>

- [x] **365-day** years (`day * 365`), then `Math.round(Date.now() / year)`.
- [x] It is **not** a calendar year and ignores leaps.

</details>

### Question 10: What unit is `getTimezoneOffset()`?

<details>
<summary>Answer</summary>

- [x] **Minutes.** Positive **west** of UTC. This daylight Mountain zone is **360**.

</details>

### Question 11: Why run `getYear()` if it is deprecated?

<details>
<summary>Answer</summary>

- [x] To see it **run**: **121** for 2021.
- [x] **Do not use it.** Use **`getFullYear()`** (**2021**).

</details>

### Question 12: What is `getUTCDate()` on `"2021-03-25"`?

<details>
<summary>Answer</summary>

- [x] **25** — the UTC calendar day, while local `getDate()` is **24**.

</details>

### Question 13: What do “now” snaps represent?

<details>
<summary>Answer</summary>

- [x] The **browser's current local** value at screenshot time — not a fake hardcoded clock.

</details>

</details>

## Summary

Read local fields with getFullYear, getMonth, getDate, getDay, and the time getters; read UTC with the getUTC\* twins. Date-only ISO is UTC midnight, so US local getters can show the previous evening. getTime and Date.now are epoch milliseconds. Skip getYear.

## References

- [JS Date Get (W3Schools)](https://www.w3schools.com/js/js_date_methods.asp)
- [MDN: Date.prototype.getDate](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate)
- [MDN: Date.now](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
- [MDN: Date.prototype.getTimezoneOffset](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)
