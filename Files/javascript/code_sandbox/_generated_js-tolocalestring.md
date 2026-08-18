<details>
  <summary>JS toLocaleString()</summary>

## Introduction

toLocaleString formats a value using locale rules. This Chrome is en-US: 1234567.89 prints 1,234,567.89 by default. de-DE uses 1.234.567,89. no-NO uses nbsp grouping: 1 234 567,89. Currency, percent, and fraction-digit options change the output. Date-only ISO strings are UTC midnight, so an array of 2026-01-01 and 2026-12-24 printed 12/31/2025, 5:00:00 PM and 12/23/2026, 5:00:00 PM in Mountain time — not the UTC calendar dates. BigInt also supports toLocaleString.

This section has **10** examples:

- [x] **Example 1:** Number toLocaleString() — default locale [View](#js-tolocalestring-example-01)
- [x] **Example 2:** Locales en-US, de-DE, no-NO [View](#js-tolocalestring-example-02)
- [x] **Example 3:** style currency — USD, EUR, NOK [View](#js-tolocalestring-example-03)
- [x] **Example 4:** style percent — 0.875 → 88% [View](#js-tolocalestring-example-04)
- [x] **Example 5:** minimumFractionDigits / maximumFractionDigits [View](#js-tolocalestring-example-05)
- [x] **Example 6:** Date toLocaleString("en-US") [View](#js-tolocalestring-example-06)
- [x] **Example 7:** Date options weekday/year/month/day [View](#js-tolocalestring-example-07)
- [x] **Example 8:** Readable file sizes [View](#js-tolocalestring-example-08)
- [x] **Example 9:** Array toLocaleString — each element [View](#js-tolocalestring-example-09)
- [x] **Example 10:** BigInt toLocaleString (named type on the page) [View](#js-tolocalestring-example-10)

## Detailed Explanation

- [x] This engine: **en-US**. Default number **1,234,567.89**.
- [x] de-DE **"1.234.567,89"**. no-NO **"1 234 567,89"** (nbsp).
- [x] USD **"$1,299.95"**. EUR **"1.299,95 €"**. NOK **"1 299,95 kr"**. percent **"88%"**. 3.14159 → **"3.14"**.
- [x] Date `en-US` on the fixed instant: **3/25/2021, 9:30:45 AM**. Long: **Thursday, March 25, 2021**.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**. In this Mountain zone, local `toString` / `toLocaleString` can fall on the **previous** calendar evening. Array demo printed **12/31/2025, 5:00:00 PM,12/23/2026, 5:00:00 PM**.
- [x] The method name is **toLocaleString** (locale, not local).

<a id="js-tolocalestring-example-01"></a>

### **Example 1: Number toLocaleString() — default locale**

- [x] `toLocaleString()` uses **this engine's** locale when you omit the locale argument.
- [x] This Chrome reports **en-US**. The grouping character is a comma.

Sandbox: `code_sandbox/js-tolocalestring/number-default.html`

```javascript
let num = 1234567.89;
let text = num.toLocaleString();
```

<img alt="js-tolocalestring example 1 source" src="./code_sandbox/snaps/js-tolocalestring-01-code.png" />

<img alt="js-tolocalestring example 1 result" src="./code_sandbox/snaps/js-tolocalestring-01-result.png" />

- [x] **Outcome:** This engine printed **"1,234,567.89"**. navigator.language is **"en-US"**.

<a id="js-tolocalestring-example-02"></a>

### **Example 2: Locales en-US, de-DE, no-NO**

- [x] Pass a **locale** (`language-COUNTRY`) to pick grouping and decimal marks.
- [x] `no-NO` uses a **nbsp** thousands separator in this engine.

Sandbox: `code_sandbox/js-tolocalestring/number-locales.html`

```javascript
let num = 1234567.89;
let us = num.toLocaleString("en-US");
let de = num.toLocaleString("de-DE");
let no = num.toLocaleString("no-NO");
```

<img alt="js-tolocalestring example 2 source" src="./code_sandbox/snaps/js-tolocalestring-02-code.png" />

<img alt="js-tolocalestring example 2 result" src="./code_sandbox/snaps/js-tolocalestring-02-result.png" />

- [x] **Outcome:** en-US **"1,234,567.89"**. de-DE **"1.234.567,89"**. no-NO **"1 234 567,89"** (nbsp spaces).

<a id="js-tolocalestring-example-03"></a>

### **Example 3: style currency — USD, EUR, NOK**

- [x] `style:"currency"` plus **`currency`** formats money for that locale.

Sandbox: `code_sandbox/js-tolocalestring/currency.html`

```javascript
let price = 1299.95;
let dollars = price.toLocaleString("en-US", {style:"currency", currency:"USD"});
let euros = price.toLocaleString("de-DE", {style:"currency", currency:"EUR"});
let kroner = price.toLocaleString("no-NO", {style:"currency", currency:"NOK"});
```

<img alt="js-tolocalestring example 3 source" src="./code_sandbox/snaps/js-tolocalestring-03-code.png" />

<img alt="js-tolocalestring example 3 result" src="./code_sandbox/snaps/js-tolocalestring-03-result.png" />

- [x] **Outcome:** USD **"$1,299.95"**. EUR **"1.299,95 €"** (nbsp before €). NOK **"1 299,95 kr"** (nbsp grouping).

<a id="js-tolocalestring-example-04"></a>

### **Example 4: style percent — 0.875 → 88%**

- [x] `style:"percent"` multiplies by 100 and adds a percent sign.

Sandbox: `code_sandbox/js-tolocalestring/percent.html`

```javascript
let score = 0.875;
let result = score.toLocaleString("en-US", {style:"percent"});
```

<img alt="js-tolocalestring example 4 source" src="./code_sandbox/snaps/js-tolocalestring-04-code.png" />

<img alt="js-tolocalestring example 4 result" src="./code_sandbox/snaps/js-tolocalestring-04-result.png" />

- [x] **Outcome:** result is **"88%"**.

<a id="js-tolocalestring-example-05"></a>

### **Example 5: minimumFractionDigits / maximumFractionDigits**

- [x] Pin the number of fraction digits with **minimumFractionDigits** and **maximumFractionDigits**.

Sandbox: `code_sandbox/js-tolocalestring/fraction-digits.html`

```javascript
let num = 3.14159;
let text = num.toLocaleString("en-US", {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2
});
```

<img alt="js-tolocalestring example 5 source" src="./code_sandbox/snaps/js-tolocalestring-05-code.png" />

<img alt="js-tolocalestring example 5 result" src="./code_sandbox/snaps/js-tolocalestring-05-result.png" />

- [x] **Outcome:** text is **"3.14"**.

<a id="js-tolocalestring-example-06"></a>

### **Example 6: Date toLocaleString("en-US")**

- [x] Dates format with the locale too. **`new Date()`** is **now** on the page Tryit.
- [x] This sandbox uses a **fixed** instant so the snap is stable: `2021-03-25T15:30:45.123Z`.

Sandbox: `code_sandbox/js-tolocalestring/date-en-us.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
let text = d.toLocaleString("en-US");
```

<img alt="js-tolocalestring example 6 source" src="./code_sandbox/snaps/js-tolocalestring-06-code.png" />

<img alt="js-tolocalestring example 6 result" src="./code_sandbox/snaps/js-tolocalestring-06-result.png" />

- [x] **Outcome:** This engine printed **"3/25/2021, 9:30:45 AM"** (Mountain, UTC−6).

<a id="js-tolocalestring-example-07"></a>

### **Example 7: Date options weekday/year/month/day**

- [x] Options control **weekday**, **year**, **month**, and **day** words vs numbers.

Sandbox: `code_sandbox/js-tolocalestring/date-options.html`

```javascript
const d = new Date("2021-03-25T15:30:45.123Z");
let text = d.toLocaleString("en-US", {
  weekday: "long",
  year: "numeric",
  month: "long",
  day: "numeric"
});
```

<img alt="js-tolocalestring example 7 source" src="./code_sandbox/snaps/js-tolocalestring-07-code.png" />

<img alt="js-tolocalestring example 7 result" src="./code_sandbox/snaps/js-tolocalestring-07-result.png" />

- [x] **Outcome:** This engine printed **"Thursday, March 25, 2021"** (local calendar day — still March 25).

<a id="js-tolocalestring-example-08"></a>

### **Example 8: Readable file sizes**

- [x] A common trick: divide bytes, then **`toLocaleString`** with **maximumFractionDigits: 1**.

Sandbox: `code_sandbox/js-tolocalestring/filesize.html`

```javascript
function fileSize(bytes) {
  if (bytes < 1024) return bytes + " bytes";
  if (bytes < 1024 * 1024) {
    return (bytes / 1024).toLocaleString("en-US", {maximumFractionDigits: 1}) + " KB";
  }
  return (bytes / 1024 / 1024).toLocaleString("en-US", {maximumFractionDigits: 1}) + " MB";
}
let size = 1536000;
let text = fileSize(size);
```

<img alt="js-tolocalestring example 8 source" src="./code_sandbox/snaps/js-tolocalestring-08-code.png" />

<img alt="js-tolocalestring example 8 result" src="./code_sandbox/snaps/js-tolocalestring-08-result.png" />

- [x] **Outcome:** 1536000 bytes → **"1.5 MB"** in this engine.

<a id="js-tolocalestring-example-09"></a>

### **Example 9: Array toLocaleString — each element**

- [x] Array **`toLocaleString`** converts **each** element, then joins with commas.
- [x] Date-only ISO (`YYYY-MM-DD`) is **UTC midnight**. In this Mountain zone, local `toString` / `toLocaleString` can fall on the **previous** calendar evening. These ISO dates are UTC midnight, so Mountain prints the **previous evening**.

Sandbox: `code_sandbox/js-tolocalestring/array-dates.html`

```javascript
const dates = [
  new Date("2026-01-01"),
  new Date("2026-12-24")
];
let text = dates.toLocaleString("en-US");
```

<img alt="js-tolocalestring example 9 source" src="./code_sandbox/snaps/js-tolocalestring-09-code.png" />

<img alt="js-tolocalestring example 9 result" src="./code_sandbox/snaps/js-tolocalestring-09-result.png" />

- [x] **Outcome:** This engine printed **"12/31/2025, 5:00:00 PM,12/23/2026, 5:00:00 PM"** — not Jan 1 / Dec 24 local. ISO stays **2026-01-01T00:00:00.000Z** and **2026-12-24T00:00:00.000Z**.

<a id="js-tolocalestring-example-10"></a>

### **Example 10: BigInt toLocaleString (named type on the page)**

- [x] The page lists **BigInt** as supporting `toLocaleString`. No Tryit — still run it.

Sandbox: `code_sandbox/js-tolocalestring/bigint-locale.html`

```javascript
let n = 1234567890123456789n;
let text = n.toLocaleString("en-US");
```

<img alt="js-tolocalestring example 10 source" src="./code_sandbox/snaps/js-tolocalestring-10-code.png" />

<img alt="js-tolocalestring example 10 result" src="./code_sandbox/snaps/js-tolocalestring-10-result.png" />

- [x] **Outcome:** This engine printed **"1,234,567,890,123,456,789"**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-tolocalestring/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What did `num.toLocaleString()` print here?

<details>
<summary>Answer</summary>

- [x] **"1,234,567.89"**. navigator.language **"en-US"**.

</details>

### Question 2: What is de-DE for that number?

<details>
<summary>Answer</summary>

- [x] **"1.234.567,89"** (dot thousands, comma decimal).

</details>

### Question 3: What is no-NO for that number?

<details>
<summary>Answer</summary>

- [x] **"1 234 567,89"** with nbsp grouping.

</details>

### Question 4: What is 1299.95 as USD / EUR / NOK here?

<details>
<summary>Answer</summary>

- [x] **"$1,299.95"**, **"1.299,95 €"**, **"1 299,95 kr"**.

</details>

### Question 5: What is `0.875` as percent en-US?

<details>
<summary>Answer</summary>

- [x] **"88%"**.

</details>

### Question 6: What is 3.14159 with min/max fraction digits 2?

<details>
<summary>Answer</summary>

- [x] **"3.14"**.

</details>

### Question 7: What is the fixed Date in en-US?

<details>
<summary>Answer</summary>

- [x] **"3/25/2021, 9:30:45 AM"** (Mountain).

</details>

### Question 8: What is the long weekday form?

<details>
<summary>Answer</summary>

- [x] **"Thursday, March 25, 2021"**.

</details>

### Question 9: What did `fileSize(1536000)` return?

<details>
<summary>Answer</summary>

- [x] **"1.5 MB"**.

</details>

### Question 10: Why did the date array show Dec 31 2025?

<details>
<summary>Answer</summary>

- [x] Date-only ISO is **UTC midnight**. Mountain is **17:00 the previous day** in winter.

</details>

### Question 11: Does BigInt support toLocaleString?

<details>
<summary>Answer</summary>

- [x] **Yes.** 1234567890123456789n → **"1,234,567,890,123,456,789"** here.

</details>

### Question 12: Is the method `toLocalString`?

<details>
<summary>Answer</summary>

- [x] **No.** It is **toLocaleString** (locale = language + country).

</details>


</details>

## Summary

Always report what this engine printed — locales differ. Pass an explicit locale for stable formatting. Treat date-only ISO as UTC when you locale-format Dates.

## References

- [JS toLocaleString() (W3Schools)](https://www.w3schools.com/js/js_tolocalestring.asp)
- [MDN: Number.prototype.toLocaleString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString)
- [MDN: Date.prototype.toLocaleString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)

</details>
