<details>
  <summary>JS Cookies</summary>

## Introduction

Cookies are `document.cookie` name=value pairs. You create/change them by assignment, delete them with a past `expires`, and parse the read-back string with helpers (`setCookie`, `getCookie`, `checkCookie`).

This section has **11** examples:

- [x] **Example 1:** Create a cookie — document.cookie = name=value [View](#js-cookies-example-01)
- [x] **Example 2:** Cookie with expires date [View](#js-cookies-example-02)
- [x] **Example 3:** Cookie with path=/ [View](#js-cookies-example-03)
- [x] **Example 4:** Read cookies — let x = document.cookie [View](#js-cookies-example-04)
- [x] **Example 5:** Change a cookie by setting the same name [View](#js-cookies-example-05)
- [x] **Example 6:** Delete a cookie with an expired date [View](#js-cookies-example-06)
- [x] **Example 7:** Reading cookie returns only name=value pairs [View](#js-cookies-example-07)
- [x] **Example 8:** setCookie(cname, cvalue, exdays) [View](#js-cookies-example-08)
- [x] **Example 9:** getCookie(cname) — parse the cookie string [View](#js-cookies-example-09)
- [x] **Example 10:** checkCookie() — welcome or prompt [View](#js-cookies-example-10)
- [x] **Example 11:** All together — setCookie + getCookie + checkCookie on load [View](#js-cookies-example-11)

## Detailed Explanation

- [x] Write `name=value; expires=…; path=/`.
- [x] Read-back is only name=value pairs.
- [x] Match path when deleting.
- [x] The page’s 2013 sample expiry would delete a cookie today.

<a id="js-cookies-example-01"></a>

### **Example 1: Create a cookie — document.cookie = name=value**

- [x] A cookie is a small **name=value** string the browser stores for a site.
- [x] `document.cookie = "username=John Doe"` **adds** (or updates) that cookie.
- [x] Reading `document.cookie` later returns the name/value pairs, not the expires/path you wrote.
- [x] Must be served over **http(s)** — `file://` often will not store cookies.

Sandbox: `code_sandbox/js-cookies/create.html`

```html
document.cookie = "username=John Doe";
```

<img alt="js-cookies example 1 source" src="./code_sandbox/snaps/js-cookies-01-code.png" />

<img alt="js-cookies example 1 result" src="./code_sandbox/snaps/js-cookies-01-result.png" />

- [x] **Outcome:** After setting, `document.cookie` contains **username=John Doe** (among any others).

<a id="js-cookies-example-02"></a>

### **Example 2: Cookie with expires date**

- [x] Add **`expires=UTC-date`** so the cookie survives the session.
- [x] Without expires, it is often a **session** cookie (cleared when the browser closes).
- [x] The W3Schools sample date is in the **past** (`18 Dec 2013`) — that would **delete** the cookie today. The sandbox uses a **future** date so the create-with-expires idea actually sticks.

Sandbox: `code_sandbox/js-cookies/expires.html`

```html
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC";
```

<img alt="js-cookies example 2 source" src="./code_sandbox/snaps/js-cookies-02-code.png" />

<img alt="js-cookies example 2 result" src="./code_sandbox/snaps/js-cookies-02-result.png" />

- [x] **Outcome:** With a future `expires`, the cookie is stored and `username=John Doe` is readable. A 2013 expiry (as on the page) would expire immediately.

<a id="js-cookies-example-03"></a>

### **Example 3: Cookie with path=/**

- [x] **`path=/`** makes the cookie available on the whole site, not only the current folder.
- [x] If you omit path, it defaults to the **current path**, which surprises people later.
- [x] Always set `path=/` unless you have a reason not to.

Sandbox: `code_sandbox/js-cookies/path.html`

```html
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
```

<img alt="js-cookies example 3 source" src="./code_sandbox/snaps/js-cookies-03-code.png" />

<img alt="js-cookies example 3 result" src="./code_sandbox/snaps/js-cookies-03-result.png" />

- [x] **Outcome:** The cookie is set with **path=/** and the name/value is visible on this path.

<a id="js-cookies-example-04"></a>

### **Example 4: Read cookies — let x = document.cookie**

- [x] Reading `document.cookie` returns **all** cookies as one string: `n=v; n2=v2`.
- [x] You do **not** get expires, path, or httpOnly flags.
- [x] `HttpOnly` cookies are invisible to JavaScript by design.

Sandbox: `code_sandbox/js-cookies/read.html`

```html
let x = document.cookie;
```

<img alt="js-cookies example 4 source" src="./code_sandbox/snaps/js-cookies-04-code.png" />

<img alt="js-cookies example 4 result" src="./code_sandbox/snaps/js-cookies-04-result.png" />

- [x] **Outcome:** `x` is the cookie string, including **username=…** after we set it.

<a id="js-cookies-example-05"></a>

### **Example 5: Change a cookie by setting the same name**

- [x] To change a cookie, **set it again** with the same name (and the same path).
- [x] `username=John Smith` replaces `username=John Doe`.
- [x] A different `path` looks like a different cookie.

Sandbox: `code_sandbox/js-cookies/change.html`

```html
document.cookie = "username=John Smith; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
```

<img alt="js-cookies example 5 source" src="./code_sandbox/snaps/js-cookies-05-code.png" />

<img alt="js-cookies example 5 result" src="./code_sandbox/snaps/js-cookies-05-result.png" />

- [x] **Outcome:** After the change, the stored username is **John Smith**.

<a id="js-cookies-example-06"></a>

### **Example 6: Delete a cookie with an expired date**

- [x] There is no `deleteCookie`. Set **`expires` in the past** (Unix epoch is conventional).
- [x] You must match **name + path** (and domain if you set one).
- [x] `username=; expires=Thu, 01 Jan 1970 …; path=/;`

Sandbox: `code_sandbox/js-cookies/delete.html`

```html
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
```

<img alt="js-cookies example 6 source" src="./code_sandbox/snaps/js-cookies-06-code.png" />

<img alt="js-cookies example 6 result" src="./code_sandbox/snaps/js-cookies-06-result.png" />

- [x] **Outcome:** After the epoch expiry, `getCookie("username")` is empty.

<a id="js-cookies-example-07"></a>

### **Example 7: Reading cookie returns only name=value pairs**

- [x] Even if you write `expires` and `path`, **read-back is only** `name=value` pairs.
- [x] Setting a **new** name **adds**; it does not wipe other cookies.
- [x] The page’s buttons (display / create 1 / create 2 / delete) are this idea.

Sandbox: `code_sandbox/js-cookies/cookie-string.html`

```html
document.cookie will return all cookies in one string much like:
cookie1=value; cookie2=value; cookie3=value;
```

<img alt="js-cookies example 7 source" src="./code_sandbox/snaps/js-cookies-07-code.png" />

<img alt="js-cookies example 7 result" src="./code_sandbox/snaps/js-cookies-07-result.png" />

- [x] **Outcome:** After creating **c1=one** and **c2=two**, the read-back string contains both names and **no** expires text.

<a id="js-cookies-example-08"></a>

### **Example 8: setCookie(cname, cvalue, exdays)**

- [x] W3Schools helper: compute `expires` from **days**, then write `name=value;expires;path=/`.
- [x] `exdays * 24 * 60 * 60 * 1000` is milliseconds.
- [x] Always include **path=/** in the helper so later `getCookie` works site-wide.

Sandbox: `code_sandbox/js-cookies/set-cookie-fn.html`

```html
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
```

<img alt="js-cookies example 8 source" src="./code_sandbox/snaps/js-cookies-08-code.png" />

<img alt="js-cookies example 8 result" src="./code_sandbox/snaps/js-cookies-08-result.png" />

- [x] **Outcome:** `setCookie("username", "Ada", 1)` stores **Ada** for one day.

<a id="js-cookies-example-09"></a>

### **Example 9: getCookie(cname) — parse the cookie string**

- [x] Split `document.cookie` on **`;`**, trim spaces, find `name=`.
- [x] `decodeURIComponent` undoes encoding in values.
- [x] Return `""` if the name is missing — that is what `checkCookie` tests.

Sandbox: `code_sandbox/js-cookies/get-cookie-fn.html`

```html
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') { c = c.substring(1); }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
```

<img alt="js-cookies example 9 source" src="./code_sandbox/snaps/js-cookies-09-code.png" />

<img alt="js-cookies example 9 result" src="./code_sandbox/snaps/js-cookies-09-result.png" />

- [x] **Outcome:** `getCookie("username")` returns **Ada** after `setCookie`.

<a id="js-cookies-example-10"></a>

### **Example 10: checkCookie() — welcome or prompt**

- [x] If `getCookie("username")` is non-empty, **`alert("Welcome again " + username)`**.
- [x] Otherwise **`prompt`** for a name and `setCookie(..., 365)` if they typed one.
- [x] Native dialogs are stubbed in the snapshot: prompt returns **Sam**, then welcome can be shown on a second check.

Sandbox: `code_sandbox/js-cookies/check-cookie-fn.html`

```html
function checkCookie() {
  let username = getCookie("username");
  if (username != "") {
    alert("Welcome again " + username);
  } else {
    username = prompt("Please enter your name:", "");
    if (username != "" && username != null) {
      setCookie("username", username, 365);
    }
  }
}
```

<img alt="js-cookies example 10 source" src="./code_sandbox/snaps/js-cookies-10-code.png" />

<img alt="js-cookies example 10 result" src="./code_sandbox/snaps/js-cookies-10-result.png" />

- [x] **Outcome:** With no cookie, the stub prompt returns **Sam**, `setCookie` runs, and a second `checkCookie` would welcome Sam. The snapshot prints the stored name.

<a id="js-cookies-example-11"></a>

### **Example 11: All together — setCookie + getCookie + checkCookie on load**

- [x] The full page example defines all three functions and runs **`checkCookie()`** when the page loads.
- [x] First visit: prompt. Later visits: welcome alert.
- [x] The snapshot pre-sets **username=Taylor** so load looks like a returning visitor.

Sandbox: `code_sandbox/js-cookies/all-together.html`

```html
function setCookie(cname, cvalue, exdays) { /* ... */ }
function getCookie(cname) { /* ... */ }
function checkCookie() {
  let user = getCookie("username");
  if (user != "") { alert("Welcome again " + user); }
  else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) { setCookie("username", user, 365); }
  }
}
checkCookie();
```

<img alt="js-cookies example 11 source" src="./code_sandbox/snaps/js-cookies-11-code.png" />

<img alt="js-cookies example 11 result" src="./code_sandbox/snaps/js-cookies-11-result.png" />

- [x] **Outcome:** On load with an existing cookie, the mirrored alert is **Welcome again Taylor**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-cookies/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: How do you create a cookie?

<details>
<summary>Answer</summary>

- [x] Assign **`document.cookie = "name=value"`**.

</details>

### Question 2: Does a new assignment erase other cookies?

<details>
<summary>Answer</summary>

- [x] **No** — it **adds** or updates that **name** (same path).

</details>

### Question 3: How do you delete a cookie?

<details>
<summary>Answer</summary>

- [x] Set it again with **`expires` in the past** (1970) and the **same path**.

</details>

### Question 4: What do you see when you read `document.cookie`?

<details>
<summary>Answer</summary>

- [x] Only **name=value** pairs, not expires/path.

</details>

### Question 5: Why set `path=/`?

<details>
<summary>Answer</summary>

- [x] So the cookie is visible on **the whole site**, not just this folder.

</details>

### Question 6: What does `getCookie` return if the name is missing?

<details>
<summary>Answer</summary>

- [x] An **empty string**.

</details>

### Question 7: What does `checkCookie` do on a returning visitor?

<details>
<summary>Answer</summary>

- [x] **`alert("Welcome again " + username)`**.

</details>

### Question 8: What if `prompt` is cancelled?

<details>
<summary>Answer</summary>

- [x] It returns **`null`** — do not call `setCookie`.

</details>

### Question 9: Why did the page’s 2013 `expires` need a note?

<details>
<summary>Answer</summary>

- [x] That date is **in the past**, so it would **delete** the cookie today.

</details>

### Question 10: Can JS read `HttpOnly` cookies?

<details>
<summary>Answer</summary>

- [x] **No**.

</details>

### Question 11: Must examples run on http(s)?

<details>
<summary>Answer</summary>

- [x] **Yes** — `file://` often cannot store cookies.

</details>


</details>

## Summary

Set cookies with document.cookie and path=/. Parse with getCookie. Delete with a 1970 expires. Prefer Web Storage for non-secret client data; never store secrets in JS-visible cookies.

## References

- [JS Cookies](https://www.w3schools.com/js/js_cookies.asp)
- [MDN Document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)

</details>
