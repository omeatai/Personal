# JS Date Formats

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

JavaScript accepts three common date-string families: ISO 8601, short US MM/DD/YYYY, and long month-name forms. ISO is the only strictly specified family. Date-only ISO (YYYY-MM-DD, YYYY-MM, YYYY) is UTC midnight, so US time zones often print the previous local evening. Short and long strings are typically local midnight in this engine. Independent of input, the default print is a full local text string. Date.parse turns a valid string into milliseconds since 1 January 1970 UTC.

This section has **16** examples:

- [x] **Example 1:** new Date("2015-03-25") — ISO complete [View](#js-date-formats-example-01)
- [x] **Example 2:** new Date("2015-03") — year and month [View](#js-date-formats-example-02)
- [x] **Example 3:** new Date("2015") — year only [View](#js-date-formats-example-03)
- [x] **Example 4:** new Date("2015-03-25T12:00:00Z") [View](#js-date-formats-example-04)
- [x] **Example 5:** new Date("2015-03-25T12:00:00-06:30") [View](#js-date-formats-example-05)
- [x] **Example 6:** new Date("03/25/2015") — short MM/DD/YYYY [View](#js-date-formats-example-06)
- [x] **Example 7:** WARNING new Date("2015-3-25") — no leading zero [View](#js-date-formats-example-07)
- [x] **Example 8:** WARNING new Date("2015/03/25") — YYYY/MM/DD [View](#js-date-formats-example-08)
- [x] **Example 9:** WARNING new Date("25-03-2015") — DD-MM-YYYY [View](#js-date-formats-example-09)
- [x] **Example 10:** new Date("Mar 25 2015") [View](#js-date-formats-example-10)
- [x] **Example 11:** new Date("25 Mar 2015") [View](#js-date-formats-example-11)
- [x] **Example 12:** new Date("January 25 2015") [View](#js-date-formats-example-12)
- [x] **Example 13:** new Date("Jan 25 2015") [View](#js-date-formats-example-13)
- [x] **Example 14:** new Date("JANUARY, 25, 2015") [View](#js-date-formats-example-14)
- [x] **Example 15:** Date.parse("March 21, 2012") — milliseconds [View](#js-date-formats-example-15)
- [x] **Example 16:** Date.parse then new Date(msec) [View](#js-date-formats-example-16)

## Detailed Explanation

- [x] **Three input types:** ISO (`2015-03-25`), short (`03/25/2015`), long (`Mar 25 2015` / `25 Mar 2015`).
- [x] **ISO date-only is UTC midnight**, not local. This Mountain zone printed **Mar 24 18:00** for `2015-03-25`.
- [x] **`T`** separates date and time. **`Z`** is UTC. `+HH:MM` / `-HH:MM` is an offset from UTC.
- [x] **Warnings:** no leading zero, `YYYY/MM/DD`, and `DD-MM-YYYY` are unreliable. This engine parsed the first two and returned **Invalid Date** for `25-03-2015`.
- [x] Long names are **case insensitive**; **commas are ignored**.
- [x] `Date.parse` → milliseconds; `new Date(msec)` rebuilds the Date.

<a id="js-date-formats-example-01"></a>

### **Example 1: new Date("2015-03-25") — ISO complete**

- [x] ISO **YYYY-MM-DD** is the preferred JavaScript date string.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**, not local midnight. In US zones, local `getDate` / `getHours` / `getDay` can fall on the **previous** calendar day.
- [x] The page notes the printed day may be **March 24 or 25** depending on zone.

Sandbox: `code_sandbox/js-date-formats/iso-complete.html`

```javascript
const d = new Date("2015-03-25");
```

![js-date-formats example 1 source](../code_sandbox/snaps/js-date-formats-01-code.png)

![js-date-formats example 1 result](../code_sandbox/snaps/js-date-formats-01-result.png)

- [x] **Outcome:** UTC is **2015-03-25T00:00:00.000Z**. Local print is **Tue Mar 24 2015 18:00:00 GMT-0600** (Mountain). The engine did **not** use March 25 local midnight.

<a id="js-date-formats-example-02"></a>

### **Example 2: new Date("2015-03") — year and month**

- [x] ISO may omit the day: **YYYY-MM** is the first of that month **UTC**.
- [x] The page says the local day may be **February 28 or March 01**.

Sandbox: `code_sandbox/js-date-formats/iso-year-month.html`

```javascript
const d = new Date("2015-03");
```

![js-date-formats example 2 source](../code_sandbox/snaps/js-date-formats-02-code.png)

![js-date-formats example 2 result](../code_sandbox/snaps/js-date-formats-02-result.png)

- [x] **Outcome:** UTC is **2015-03-01T00:00:00.000Z**. Local print is **Sat Feb 28 2015 17:00:00 GMT-0700** (Mountain Standard — DST had not started yet).

<a id="js-date-formats-example-03"></a>

### **Example 3: new Date("2015") — year only**

- [x] ISO **YYYY** is January 1 **UTC** of that year.
- [x] The page says the local day may be **December 31 2014 or January 01 2015**.

Sandbox: `code_sandbox/js-date-formats/iso-year-only.html`

```javascript
const d = new Date("2015");
```

![js-date-formats example 3 source](../code_sandbox/snaps/js-date-formats-03-code.png)

![js-date-formats example 3 result](../code_sandbox/snaps/js-date-formats-03-result.png)

- [x] **Outcome:** UTC is **2015-01-01T00:00:00.000Z**. Local print is **Wed Dec 31 2014 17:00:00 GMT-0700**.

<a id="js-date-formats-example-04"></a>

### **Example 4: new Date("2015-03-25T12:00:00Z")**

- [x] Date and time are split by a capital **`T`**. **`Z`** means **UTC** (same idea as GMT).
- [x] `12:00:00Z` is noon UTC on March 25, 2015.

Sandbox: `code_sandbox/js-date-formats/iso-datetime-z.html`

```javascript
const d = new Date("2015-03-25T12:00:00Z");
```

![js-date-formats example 4 source](../code_sandbox/snaps/js-date-formats-04-code.png)

![js-date-formats example 4 result](../code_sandbox/snaps/js-date-formats-04-result.png)

- [x] **Outcome:** UTC stays **2015-03-25T12:00:00.000Z**. Local print is **Wed Mar 25 2015 06:00:00 GMT-0600**.

<a id="js-date-formats-example-05"></a>

### **Example 5: new Date("2015-03-25T12:00:00-06:30")**

- [x] Drop **`Z`** and add **`+HH:MM`** or **`-HH:MM`** to shift relative to UTC.
- [x] `12:00:00-06:30` is 12:00 in a zone six-and-a-half hours behind UTC (**18:30Z**).

Sandbox: `code_sandbox/js-date-formats/iso-datetime-offset.html`

```javascript
const d = new Date("2015-03-25T12:00:00-06:30");
```

![js-date-formats example 5 source](../code_sandbox/snaps/js-date-formats-05-code.png)

![js-date-formats example 5 result](../code_sandbox/snaps/js-date-formats-05-result.png)

- [x] **Outcome:** UTC is **2015-03-25T18:30:00.000Z**. Local print is **Wed Mar 25 2015 12:30:00 GMT-0600**.

<a id="js-date-formats-example-06"></a>

### **Example 6: new Date("03/25/2015") — short MM/DD/YYYY**

- [x] Short dates use **MM/DD/YYYY** (US order).
- [x] Unlike date-only ISO, this form is treated as **local** midnight in this engine.

Sandbox: `code_sandbox/js-date-formats/short-mm-dd-yyyy.html`

```javascript
const d = new Date("03/25/2015");
```

![js-date-formats example 6 source](../code_sandbox/snaps/js-date-formats-06-code.png)

![js-date-formats example 6 result](../code_sandbox/snaps/js-date-formats-06-result.png)

- [x] **Outcome:** Local print is **Wed Mar 25 2015 00:00:00 GMT-0600**. ISO is **2015-03-25T06:00:00.000Z**.

<a id="js-date-formats-example-07"></a>

### **Example 7: WARNING new Date("2015-3-25") — no leading zero**

- [x] **Warning:** months or days **without leading zeros** may fail in some browsers.
- [x] Run it and report what **this** engine did — do not assume Invalid Date.

Sandbox: `code_sandbox/js-date-formats/warn-no-leading-zero.html`

```javascript
const d = new Date("2015-3-25");
```

![js-date-formats example 7 source](../code_sandbox/snaps/js-date-formats-07-code.png)

![js-date-formats example 7 result](../code_sandbox/snaps/js-date-formats-07-result.png)

- [x] **Outcome:** This V8 engine **parsed** it as **Wed Mar 25 2015 00:00:00** local — **not** Invalid Date. The format is still unsafe. Prefer **`2015-03-25`** (ISO, UTC) or a tested long/short form.

<a id="js-date-formats-example-08"></a>

### **Example 8: WARNING new Date("2015/03/25") — YYYY/MM/DD**

- [x] **Warning:** **YYYY/MM/DD** is **undefined**. Some browsers guess; some return NaN.

Sandbox: `code_sandbox/js-date-formats/warn-yyyy-slash.html`

```javascript
const d = new Date("2015/03/25");
```

![js-date-formats example 8 source](../code_sandbox/snaps/js-date-formats-08-code.png)

![js-date-formats example 8 result](../code_sandbox/snaps/js-date-formats-08-result.png)

- [x] **Outcome:** This engine parsed it as **Wed Mar 25 2015 00:00:00** local. Still **do not rely** on slashes-in-ISO-order.

<a id="js-date-formats-example-09"></a>

### **Example 9: WARNING new Date("25-03-2015") — DD-MM-YYYY**

- [x] **Warning:** **DD-MM-YYYY** is also **undefined**.
- [x] `toISOString()` throws on an invalid Date, so this demo prints `String(d)` and `getTime()`.

Sandbox: `code_sandbox/js-date-formats/warn-dd-mm-yyyy.html`

```javascript
const d = new Date("25-03-2015");
```

![js-date-formats example 9 source](../code_sandbox/snaps/js-date-formats-09-code.png)

![js-date-formats example 9 result](../code_sandbox/snaps/js-date-formats-09-result.png)

- [x] **Outcome:** This engine returns **Invalid Date** (`getTime()` is **NaN**). Do not use day-first hyphen dates.

<a id="js-date-formats-example-10"></a>

### **Example 10: new Date("Mar 25 2015")**

- [x] Long dates are often **MMM DD YYYY**.
- [x] This form is **local** midnight here (not UTC).

Sandbox: `code_sandbox/js-date-formats/long-mar-25.html`

```javascript
const d = new Date("Mar 25 2015");
```

![js-date-formats example 10 source](../code_sandbox/snaps/js-date-formats-10-code.png)

![js-date-formats example 10 result](../code_sandbox/snaps/js-date-formats-10-result.png)

- [x] **Outcome:** **Wed Mar 25 2015 00:00:00 GMT-0600**. ISO **2015-03-25T06:00:00.000Z**.

<a id="js-date-formats-example-11"></a>

### **Example 11: new Date("25 Mar 2015")**

- [x] Month and day may appear in **either order**.

Sandbox: `code_sandbox/js-date-formats/long-25-mar.html`

```javascript
const d = new Date("25 Mar 2015");
```

![js-date-formats example 11 source](../code_sandbox/snaps/js-date-formats-11-code.png)

![js-date-formats example 11 result](../code_sandbox/snaps/js-date-formats-11-result.png)

- [x] **Outcome:** Same instant as `Mar 25 2015`: **Wed Mar 25 2015 00:00:00** local.

<a id="js-date-formats-example-12"></a>

### **Example 12: new Date("January 25 2015")**

- [x] The month may be written in **full** (`January`).

Sandbox: `code_sandbox/js-date-formats/long-january.html`

```javascript
const d = new Date("January 25 2015");
```

![js-date-formats example 12 source](../code_sandbox/snaps/js-date-formats-12-code.png)

![js-date-formats example 12 result](../code_sandbox/snaps/js-date-formats-12-result.png)

- [x] **Outcome:** **Sun Jan 25 2015 00:00:00 GMT-0700** (Mountain Standard in January).

<a id="js-date-formats-example-13"></a>

### **Example 13: new Date("Jan 25 2015")**

- [x] The month may be **abbreviated** (`Jan`).

Sandbox: `code_sandbox/js-date-formats/long-jan.html`

```javascript
const d = new Date("Jan 25 2015");
```

![js-date-formats example 13 source](../code_sandbox/snaps/js-date-formats-13-code.png)

![js-date-formats example 13 result](../code_sandbox/snaps/js-date-formats-13-result.png)

- [x] **Outcome:** Same as the full-month form: **Sun Jan 25 2015 00:00:00 GMT-0700**.

<a id="js-date-formats-example-14"></a>

### **Example 14: new Date("JANUARY, 25, 2015")**

- [x] **Commas are ignored.** Month names are **case insensitive**.

Sandbox: `code_sandbox/js-date-formats/long-january-commas.html`

```javascript
const d = new Date("JANUARY, 25, 2015");
```

![js-date-formats example 14 source](../code_sandbox/snaps/js-date-formats-14-code.png)

![js-date-formats example 14 result](../code_sandbox/snaps/js-date-formats-14-result.png)

- [x] **Outcome:** Still **Sun Jan 25 2015 00:00:00 GMT-0700**.

<a id="js-date-formats-example-15"></a>

### **Example 15: Date.parse("March 21, 2012") — milliseconds**

- [x] `Date.parse(string)` returns **milliseconds** since 1 January 1970 UTC.
- [x] A long date string is typically parsed as **local** time.

Sandbox: `code_sandbox/js-date-formats/date-parse-msec.html`

```javascript
let msec = Date.parse("March 21, 2012");
```

![js-date-formats example 15 source](../code_sandbox/snaps/js-date-formats-15-code.png)

![js-date-formats example 15 result](../code_sandbox/snaps/js-date-formats-15-result.png)

- [x] **Outcome:** This engine returned **1332309600000** (local midnight March 21, 2012 in Mountain time). The number is timezone-dependent.

<a id="js-date-formats-example-16"></a>

### **Example 16: Date.parse then new Date(msec)**

- [x] Pass the millisecond count to **`new Date(msec)`** to get a Date object.

Sandbox: `code_sandbox/js-date-formats/date-parse-then-date.html`

```javascript
let msec = Date.parse("March 21, 2012");
const d = new Date(msec);
```

![js-date-formats example 16 source](../code_sandbox/snaps/js-date-formats-16-code.png)

![js-date-formats example 16 result](../code_sandbox/snaps/js-date-formats-16-result.png)

- [x] **Outcome:** msec is **1332309600000**. d prints **Wed Mar 21 2012 00:00:00 GMT-0600**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-date-formats/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the three date input types on the page?

<details>
<summary>Answer</summary>

- [x] **ISO**, **short** (MM/DD/YYYY), and **long** (month name).

</details>

### Question 2: Is `new Date("2015-03-25")` local midnight?

<details>
<summary>Answer</summary>

- [x] **No.** Date-only ISO is **UTC midnight**.
- [x] This Mountain zone printed **Tue Mar 24 2015 18:00:00 GMT-0600**.
- [x] `toISOString()` is **2015-03-25T00:00:00.000Z**.

</details>

### Question 3: What did `new Date("2015-03")` print locally?

<details>
<summary>Answer</summary>

- [x] **Sat Feb 28 2015 17:00:00 GMT-0700** (UTC March 1).

</details>

### Question 4: What did `new Date("2015")` print locally?

<details>
<summary>Answer</summary>

- [x] **Wed Dec 31 2014 17:00:00 GMT-0700** (UTC January 1 2015).

</details>

### Question 5: What do `T` and `Z` mean in ISO date-time?

<details>
<summary>Answer</summary>

- [x] **`T`** separates date from time.
- [x] **`Z`** means **UTC** (GMT).

</details>

### Question 6: What is `new Date("2015-03-25T12:00:00-06:30")` in UTC?

<details>
<summary>Answer</summary>

- [x] **2015-03-25T18:30:00.000Z**.
- [x] Local print here is **Wed Mar 25 2015 12:30:00 GMT-0600**.

</details>

### Question 7: Is short `03/25/2015` UTC or local here?

<details>
<summary>Answer</summary>

- [x] **Local midnight** — **Wed Mar 25 2015 00:00:00 GMT-0600**.

</details>

### Question 8: Did `new Date("2015-3-25")` fail?

<details>
<summary>Answer</summary>

- [x] **No** in this V8 engine — it parsed as **local March 25**.
- [x] The page is still right: **other browsers may error**. Prefer leading zeros.

</details>

### Question 9: Did `new Date("2015/03/25")` fail?

<details>
<summary>Answer</summary>

- [x] **No** here — local March 25. The format is still **undefined**.

</details>

### Question 10: Did `new Date("25-03-2015")` fail?

<details>
<summary>Answer</summary>

- [x] **Yes.** **Invalid Date**, `getTime()` is **NaN**.

</details>

### Question 11: Are long month names case sensitive?

<details>
<summary>Answer</summary>

- [x] **No.** Commas are **ignored**. `JANUARY, 25, 2015` works.

</details>

### Question 12: What does `Date.parse("March 21, 2012")` return here?

<details>
<summary>Answer</summary>

- [x] **1332309600000** milliseconds (local midnight that day).
- [x] `new Date(msec)` prints **Wed Mar 21 2012 00:00:00 GMT-0600**.

</details>

</details>

## Summary

Prefer ISO with a time zone (`Z` or an offset). Treat date-only ISO as UTC midnight — US zones often show the previous local evening. Short and long strings are convenient but implementation-defined; the three warning formats must be tested, not trusted. Date.parse gives milliseconds you can feed back into new Date.

## References

- [JS Date Formats (W3Schools)](https://www.w3schools.com/js/js_date_formats.asp)
- [MDN: Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
- [MDN: Date.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
- [MDN: ISO 8601 date-time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
