# JS RegExp Metachars

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

Metacharacters are tokens with special meaning. \d \D \w \W \s \S pair as a class and its complement. \xhh and \uhhhh pick characters by hex; \ddd is a legacy octal form (\127 is W). The Tryits cover \d \D \w \W \s, a hex replace, and \u0057. Table rows without a Tryit (\S, \ddd) still each get an Example.

This section has **9** examples:

- [x] **Example 1:** \d — digits [View](#js-regexp-metachars-example-01)
- [x] **Example 2:** \D — non-digits [View](#js-regexp-metachars-example-02)
- [x] **Example 3:** \w — word characters [View](#js-regexp-metachars-example-03)
- [x] **Example 4:** \W — non-word characters [View](#js-regexp-metachars-example-04)
- [x] **Example 5:** \s — whitespace [View](#js-regexp-metachars-example-05)
- [x] **Example 6:** \S — non-whitespace [View](#js-regexp-metachars-example-06)
- [x] **Example 7:** \ddd — octal character [View](#js-regexp-metachars-example-07)
- [x] **Example 8:** \xhh — hexadecimal replace [View](#js-regexp-metachars-example-08)
- [x] **Example 9:** \uhhhh — Unicode hex [View](#js-regexp-metachars-example-09)

## Detailed Explanation

- [x] **`\d`/`\D`** digits vs not. **`\w`/`\W`** word vs not (`[A-Za-z0-9_]`).
- [x] **`\s`/`\S`** whitespace vs not. JSON the `\s` array or you will see ` , , , `.
- [x] **`\x6F`** is **`o`**. **`\u0057`** is **W**. **`\127`** octal is also **W**.
- [x] Prefer hex/Unicode escapes over octal in new patterns.

<a id="js-regexp-metachars-example-01"></a>

### **Example 1: \d — digits**

- [x] **`\d`** matches digits. Global `match` returns each digit as its own hit.

Sandbox: `code_sandbox/js-regexp-metachars/meta-d.html`

```javascript
let text = "Give 100%!";
const pattern = /\d/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 1 source](../code_sandbox/snaps/js-regexp-metachars-01-code.png)

![js-regexp-metachars example 1 result](../code_sandbox/snaps/js-regexp-metachars-01-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["1","0","0"]**.

<a id="js-regexp-metachars-example-02"></a>

### **Example 2: \D — non-digits**

- [x] **`\D`** is the complement of **`\d`**.

Sandbox: `code_sandbox/js-regexp-metachars/meta-nondigit.html`

```javascript
let text = "Give 100%!";
const pattern = /\D/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 2 source](../code_sandbox/snaps/js-regexp-metachars-02-code.png)

![js-regexp-metachars example 2 result](../code_sandbox/snaps/js-regexp-metachars-02-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e"," ","%","!"]**.

<a id="js-regexp-metachars-example-03"></a>

### **Example 3: \w — word characters**

- [x] **`\w`** is **`[A-Za-z0-9_]`**.

Sandbox: `code_sandbox/js-regexp-metachars/meta-w.html`

```javascript
let text = "Give 100%!";
const pattern = /\w/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 3 source](../code_sandbox/snaps/js-regexp-metachars-03-code.png)

![js-regexp-metachars example 3 result](../code_sandbox/snaps/js-regexp-metachars-03-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e","1","0","0"]**.

<a id="js-regexp-metachars-example-04"></a>

### **Example 4: \W — non-word characters**

- [x] **`\W`** matches space, punctuation, `%`, `!`, etc.

Sandbox: `code_sandbox/js-regexp-metachars/meta-nonword.html`

```javascript
let text = "Give 100%!";
const pattern = /\W/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 4 source](../code_sandbox/snaps/js-regexp-metachars-04-code.png)

![js-regexp-metachars example 4 result](../code_sandbox/snaps/js-regexp-metachars-04-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **[" ","%","!"]**.

<a id="js-regexp-metachars-example-05"></a>

### **Example 5: \s — whitespace**

- [x] **`\s`** matches space, tab, newline, and other whitespace.

Sandbox: `code_sandbox/js-regexp-metachars/meta-s.html`

```javascript
let text = "Is this all there is?";
const pattern = /\s/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 5 source](../code_sandbox/snaps/js-regexp-metachars-05-code.png)

![js-regexp-metachars example 5 result](../code_sandbox/snaps/js-regexp-metachars-05-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **[" "," "," "," "]** (four spaces). `String(result)` would look like ` , , , `.

<a id="js-regexp-metachars-example-06"></a>

### **Example 6: \S — non-whitespace**

- [x] **`\S`** is the complement of **`\s`**. No Tryit on the page — still run it.

Sandbox: `code_sandbox/js-regexp-metachars/meta-nonspace.html`

```javascript
let text = "Give 100%!";
const pattern = /\S/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 6 source](../code_sandbox/snaps/js-regexp-metachars-06-code.png)

![js-regexp-metachars example 6 result](../code_sandbox/snaps/js-regexp-metachars-06-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["G","i","v","e","1","0","0","%","!"]**.

<a id="js-regexp-metachars-example-07"></a>

### **Example 7: \ddd — octal character**

- [x] **`\ddd`** is an octal code point. **`\127`** is **W** (octal 127 = 87).
- [x] Octal escapes are a legacy form. Prefer **`\xhh`** / **`\uhhhh`**. No Tryit on the page.

Sandbox: `code_sandbox/js-regexp-metachars/meta-octal.html`

```javascript
let text = "Visit W3Schools. Hello World!";
const pattern = /\127/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 7 source](../code_sandbox/snaps/js-regexp-metachars-07-code.png)

![js-regexp-metachars example 7 result](../code_sandbox/snaps/js-regexp-metachars-07-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["W","W"]**.

<a id="js-regexp-metachars-example-08"></a>

### **Example 8: \xhh — hexadecimal replace**

- [x] **`\x6F`** is **`o`** (hex 6F).
- [x] The Tryit **replaces** each `o` with `*`.

Sandbox: `code_sandbox/js-regexp-metachars/meta-hex.html`

```javascript
let text = "Visit W3Schools. Hello World!";
let pattern = /\x6F/g;
let result = text.replace(pattern, "*");
```

![js-regexp-metachars example 8 source](../code_sandbox/snaps/js-regexp-metachars-08-code.png)

![js-regexp-metachars example 8 result](../code_sandbox/snaps/js-regexp-metachars-08-result.png)

- [x] **Outcome:** result is **"Visit W3Sch**ls. Hell* W*rld!"**.

<a id="js-regexp-metachars-example-09"></a>

### **Example 9: \uhhhh — Unicode hex**

- [x] **`\u0057`** is **W** (U+0057).

Sandbox: `code_sandbox/js-regexp-metachars/meta-unicode.html`

```javascript
let text = "Visit W3Schools. Hello World!";
const pattern = /\u0057/g;
let result = text.match(pattern);
```

![js-regexp-metachars example 9 source](../code_sandbox/snaps/js-regexp-metachars-09-code.png)

![js-regexp-metachars example 9 result](../code_sandbox/snaps/js-regexp-metachars-09-result.png)

- [x] **Outcome:** `JSON.stringify(result)` is **["W","W"]**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-regexp-metachars/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `\d` match in `Give 100%!`?

<details>
<summary>Answer</summary>

- [x] **["1","0","0"]**.

</details>

### Question 2: What does `\D` match there?

<details>
<summary>Answer</summary>

- [x] **["G","i","v","e"," ","%","!"]**.

</details>

### Question 3: What does `\w` include?

<details>
<summary>Answer</summary>

- [x] Letters, digits, and **`_`**. Not space, `%`, `!`.

</details>

### Question 4: What does `\W` match in that string?

<details>
<summary>Answer</summary>

- [x] **[" ","%","!"]**.

</details>

### Question 5: How many `\s` hits in `Is this all there is?`?

<details>
<summary>Answer</summary>

- [x] **Four** spaces: **[" "," "," "," "]**.

</details>

### Question 6: What does `\S` match in `Give 100%!`?

<details>
<summary>Answer</summary>

- [x] Everything except the space: letters, digits, `%`, `!`.

</details>

### Question 7: What does `\x6F` replace in the Hello/World sentence?

<details>
<summary>Answer</summary>

- [x] Each **`o`** → `*`: **Visit W3Sch**ls. Hell* W*rld!**

</details>

### Question 8: What is `\u0057`?

<details>
<summary>Answer</summary>

- [x] **W**. Two hits in the Visit/World sentence.

</details>

### Question 9: What is `\127`?

<details>
<summary>Answer</summary>

- [x] Octal for **W**. Same two hits. Legacy — prefer `\u0057`.

</details>


</details>

## Summary

Use \d \w \s and their uppercase complements for common sets. Hex (\xhh) and Unicode (\uhhhh) name exact characters. Octal \ddd still works without the u flag but is a museum piece. JSON-stringify whitespace matches.

## References

- [JS RegExp Meta Characters (W3Schools)](https://www.w3schools.com/js/js_regexp_meta_characters.asp)
- [MDN: Character classes (including \d \w \s)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
