<details>
  <summary>JS Form Validation</summary>

## Introduction

A signup form that never reloads: submit is preventDefault’d, then four validators run. Name ≥ 2 after trim, email matches a simple regex, password ≥ 8, confirm non-empty and equal. Errors go in red <p>s under each field. Success sets Form is valid! in green. Exercise 1 requires a digit in the password. Do not skip preventDefault, and trim where the page trims.

This section has **12** examples:

- [x] **Example 1:** HTML form: Name, Email, Password, Confirm + error <p>s [View](#js-form-validation-example-01)
- [x] **Example 2:** CSS: .error red, .ok green, .field spacing [View](#js-form-validation-example-02)
- [x] **Example 3:** Cache form, inputs, error nodes, result [View](#js-form-validation-example-03)
- [x] **Example 4:** showError(el, message) and clearError(el) [View](#js-form-validation-example-04)
- [x] **Example 5:** submit + event.preventDefault() so the page does not reload [View](#js-form-validation-example-05)
- [x] **Example 6:** validateName() — trim, at least 2 characters [View](#js-form-validation-example-06)
- [x] **Example 7:** validateEmail() — simple regex [View](#js-form-validation-example-07)
- [x] **Example 8:** validatePassword() — at least 8 characters [View](#js-form-validation-example-08)
- [x] **Example 9:** validateConfirm() — required and must match [View](#js-form-validation-example-09)
- [x] **Example 10:** Finished project: empty submit shows all errors [View](#js-form-validation-example-10)
- [x] **Example 11:** Finished project: valid submit → Form is valid! [View](#js-form-validation-example-11)
- [x] **Example 12:** Exercise 1: password must contain a digit [View](#js-form-validation-example-12)

## Detailed Explanation

- [x] **`event.preventDefault()`** on submit or the page **reloads** and errors vanish.
- [x] **validateForm** runs **every** field (name && email && password && confirm).
- [x] Messages: **Name must be at least 2 characters.** / **Enter a valid email address.** / **Password must be at least 8 characters.** / **Please confirm your password.** / **Passwords do not match.**
- [x] Prefer **text** for messages (the page warns against innerHTML with user input).

<a id="js-form-validation-example-01"></a>

### **Example 1: HTML form: Name, Email, Password, Confirm + error <p>s**

- [x] Four fields, each with an **empty `<p class="error">`** underneath for messages.
- [x] **`id="signupForm"`**. Submit button **Create Account**.

Sandbox: `code_sandbox/js-form-validation/html-fields.html`

```html
<h2>Sign Up</h2>
<form id="signupForm">
  <div class="field">
    <label for="name">Name:</label><br>
    <input type="text" id="name">
    <p class="error" id="nameError"></p>
  </div>
  <div class="field">
    <label for="email">Email:</label><br>
    <input type="text" id="email">
    <p class="error" id="emailError"></p>
  </div>
  <div class="field">
    <label for="password">Password:</label><br>
    <input type="password" id="password">
    <p class="error" id="passwordError"></p>
  </div>
  <div class="field">
    <label for="confirm">Confirm Password:</label><br>
    <input type="password" id="confirm">
    <p class="error" id="confirmError"></p>
  </div>
  <button type="submit">Create Account</button>
  <p id="result"></p>
</form>
```

<img alt="js-form-validation example 1 source" src="./code_sandbox/snaps/js-form-validation-01-code.png" />

<img alt="js-form-validation example 1 result" src="./code_sandbox/snaps/js-form-validation-01-result.png" />

- [x] **Outcome:** Four inputs and a submit button. Error paragraphs are **blank** until JS writes them.

<a id="js-form-validation-example-02"></a>

### **Example 2: CSS: .error red, .ok green, .field spacing**

- [x] **.error** is **red** (invalid). **.ok** is **green** (`Form is valid!`).

Sandbox: `code_sandbox/js-form-validation/css-error-ok.html`

```css
input { padding: 8px; width: 260px; margin-bottom: 4px; }
.error { color: red; margin: 0; }
.ok { color: green; margin: 0; }
.field { margin-bottom: 12px; }
```

<img alt="js-form-validation example 2 source" src="./code_sandbox/snaps/js-form-validation-02-code.png" />

<img alt="js-form-validation example 2 result" src="./code_sandbox/snaps/js-form-validation-02-result.png" />

- [x] **Outcome:** An `.error` paragraph is **red**. An `.ok` paragraph is **green**.

<a id="js-form-validation-example-03"></a>

### **Example 3: Cache form, inputs, error nodes, result**

- [x] One **`const`** per field and per error `<p>`.

Sandbox: `code_sandbox/js-form-validation/field-objects.html`

```javascript
const form = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
```

<img alt="js-form-validation example 3 source" src="./code_sandbox/snaps/js-form-validation-03-code.png" />

<img alt="js-form-validation example 3 result" src="./code_sandbox/snaps/js-form-validation-03-result.png" />

- [x] **Outcome:** **form.tagName** is **FORM**. **nameInput.id** is **name**.

<a id="js-form-validation-example-04"></a>

### **Example 4: showError(el, message) and clearError(el)**

- [x] `showError` writes **innerHTML**. `clearError` sets **""**.
- [x] The page later warns: prefer **text** for messages (don’t dump raw user input into innerHTML).

Sandbox: `code_sandbox/js-form-validation/show-clear-error.html`

```javascript
function showError(el, message) {
  el.innerHTML = message;
}
function clearError(el) {
  el.innerHTML = "";
}
```

<img alt="js-form-validation example 4 source" src="./code_sandbox/snaps/js-form-validation-04-code.png" />

<img alt="js-form-validation example 4 result" src="./code_sandbox/snaps/js-form-validation-04-result.png" />

- [x] **Outcome:** showError writes **Name must be at least 2 characters.** clearError blanks it.

<a id="js-form-validation-example-05"></a>

### **Example 5: submit + event.preventDefault() so the page does not reload**

- [x] Without **`preventDefault`**, the browser **navigates** and you never see errors.
- [x] Then run **`validateForm()`**. Valid → **Form is valid!** (green). Else → **Please fix the errors.**

Sandbox: `code_sandbox/js-form-validation/prevent-default.html`

```javascript
form.addEventListener("submit", function (event) {
  event.preventDefault();
  result.innerHTML = "";
  if (validateForm()) {
    result.innerHTML = "Form is valid!";
    result.className = "ok";
  } else {
    result.innerHTML = "Please fix the errors.";
    result.className = "error";
  }
});
```

<img alt="js-form-validation example 5 source" src="./code_sandbox/snaps/js-form-validation-05-code.png" />

<img alt="js-form-validation example 5 result" src="./code_sandbox/snaps/js-form-validation-05-result.png" />

- [x] **Outcome:** Stub `validateForm()` that returns **false** → result **Please fix the errors.** and class **error**. Page did **not** reload.

<a id="js-form-validation-example-06"></a>

### **Example 6: validateName() — trim, at least 2 characters**

- [x] **`trim()`** so spaces don’t count as a name.
- [x] Length **< 2** → **Name must be at least 2 characters.**

Sandbox: `code_sandbox/js-form-validation/validate-name.html`

```javascript
function validateName() {
  let value = nameInput.value.trim();
  if (value.length < 2) {
    showError(nameError, "Name must be at least 2 characters.");
    return false;
  }
  clearError(nameError);
  return true;
}
```

<img alt="js-form-validation example 6 source" src="./code_sandbox/snaps/js-form-validation-06-code.png" />

<img alt="js-form-validation example 6 result" src="./code_sandbox/snaps/js-form-validation-06-result.png" />

- [x] **Outcome:** **"A"** fails. **"Ada"** passes.

<a id="js-form-validation-example-07"></a>

### **Example 7: validateEmail() — simple regex**

- [x] Pattern **`/^[^\s@]+@[^\s@]+\.[^\s@]+$/`** — not a full RFC parser, good enough here.
- [x] Fail message: **Enter a valid email address.**

Sandbox: `code_sandbox/js-form-validation/validate-email.html`

```javascript
function validateEmail() {
  let value = emailInput.value.trim();
  if (!(/[^\s@]+@[^\s@]+\.[^\s@]+/.test(value))) {
    showError(emailError, "Enter a valid email address.");
    return false;
  }
  clearError(emailError);
  return true;
}
```

<img alt="js-form-validation example 7 source" src="./code_sandbox/snaps/js-form-validation-07-code.png" />

<img alt="js-form-validation example 7 result" src="./code_sandbox/snaps/js-form-validation-07-result.png" />

- [x] **Outcome:** **ada@example.com** true. **ada@** false with the error text.

<a id="js-form-validation-example-08"></a>

### **Example 8: validatePassword() — at least 8 characters**

- [x] Does **not** trim (spaces count). Length **< 8** → **Password must be at least 8 characters.**

Sandbox: `code_sandbox/js-form-validation/validate-password.html`

```javascript
function validatePassword() {
  let value = passInput.value;
  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  clearError(passError);
  return true;
}
```

<img alt="js-form-validation example 8 source" src="./code_sandbox/snaps/js-form-validation-08-code.png" />

<img alt="js-form-validation example 8 result" src="./code_sandbox/snaps/js-form-validation-08-result.png" />

- [x] **Outcome:** **secret** (6) fails. **secret12** (8) passes.

<a id="js-form-validation-example-09"></a>

### **Example 9: validateConfirm() — required and must match**

- [x] Empty confirm → **Please confirm your password.**
- [x] Mismatch → **Passwords do not match.**

Sandbox: `code_sandbox/js-form-validation/validate-confirm.html`

```javascript
function validateConfirm() {
  let pass = passInput.value;
  let confirm = confirmInput.value;
  if (confirm === "") {
    showError(confirmError, "Please confirm your password.");
    return false;
  }
  if (confirm !== pass) {
    showError(confirmError, "Passwords do not match.");
    return false;
  }
  clearError(confirmError);
  return true;
}
```

<img alt="js-form-validation example 9 source" src="./code_sandbox/snaps/js-form-validation-09-code.png" />

<img alt="js-form-validation example 9 result" src="./code_sandbox/snaps/js-form-validation-09-result.png" />

- [x] **Outcome:** Empty → confirm error. **secret12** vs **secret99** → do not match. Matching pair → true.

<a id="js-form-validation-example-10"></a>

### **Example 10: Finished project: empty submit shows all errors**

- [x] `validateForm()` runs **all four** checks (does not stop at the first failure).
- [x] Result line: **Please fix the errors.**

Sandbox: `code_sandbox/js-form-validation/finished-invalid.html`

```html
const form = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passInput = document.getElementById("password");
const confirmInput = document.getElementById("confirm");
const nameError = document.getElementById("nameError");
const emailError = document.getElementById("emailError");
const passError = document.getElementById("passwordError");
const confirmError = document.getElementById("confirmError");
const result = document.getElementById("result");
function showError(el, message) {
  el.innerHTML = message;
}
function clearError(el) {
  el.innerHTML = "";
}
function validateName() {
  let value = nameInput.value.trim();
  if (value.length < 2) {
    showError(nameError, "Name must be at least 2 characters.");
    return false;
  }
  clearError(nameError);
  return true;
}
function validateEmail() {
  let value = emailInput.value.trim();
  if (!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value))) {
    showError(emailError, "Enter a valid email address.");
    return false;
  }
  clearError(emailError);
  return true;
}
function validatePassword() {
  let value = passInput.value;
  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  clearError(passError);
  return true;
}
function validateConfirm() {
  let pass = passInput.value;
  let confirm = confirmInput.value;
  if (confirm === "") {
    showError(confirmError, "Please confirm your password.");
    return false;
  }
  if (confirm !== pass) {
    showError(confirmError, "Passwords do not match.");
    return false;
  }
  clearError(confirmError);
  return true;
}
function validateForm() {
  let okName = validateName();
  let okEmail = validateEmail();
  let okPass = validatePassword();
  let okConfirm = validateConfirm();
  return okName && okEmail && okPass && okConfirm;
}
form.addEventListener("submit", function (event) {
  event.preventDefault();
  result.innerHTML = "";
  if (validateForm()) {
    result.innerHTML = "Form is valid!";
    result.className = "ok";
  } else {
    result.innerHTML = "Please fix the errors.";
    result.className = "error";
  }
});
```

<img alt="js-form-validation example 10 source" src="./code_sandbox/snaps/js-form-validation-10-code.png" />

<img alt="js-form-validation example 10 result" src="./code_sandbox/snaps/js-form-validation-10-result.png" />

- [x] **Outcome:** Empty submit: name/email/password/confirm errors all filled. Result **Please fix the errors.**

<a id="js-form-validation-example-11"></a>

### **Example 11: Finished project: valid submit → Form is valid!**

- [x] Name **Ada**, email **ada@example.com**, password **secret12** twice.

Sandbox: `code_sandbox/js-form-validation/finished-valid.html`

```javascript
const form = document.getElementById("signupForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passInput = document.getElementById("password");
const confirmInput = document.getElementById("confirm");
const nameError = document.getElementById("nameError");
const emailError = document.getElementById("emailError");
const passError = document.getElementById("passwordError");
const confirmError = document.getElementById("confirmError");
const result = document.getElementById("result");
function showError(el, message) {
  el.innerHTML = message;
}
function clearError(el) {
  el.innerHTML = "";
}
function validateName() {
  let value = nameInput.value.trim();
  if (value.length < 2) {
    showError(nameError, "Name must be at least 2 characters.");
    return false;
  }
  clearError(nameError);
  return true;
}
function validateEmail() {
  let value = emailInput.value.trim();
  if (!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value))) {
    showError(emailError, "Enter a valid email address.");
    return false;
  }
  clearError(emailError);
  return true;
}
function validatePassword() {
  let value = passInput.value;
  if (value.length < 8) {
    showError(passError, "Password must be at least 8 characters.");
    return false;
  }
  clearError(passError);
  return true;
}
function validateConfirm() {
  let pass = passInput.value;
  let confirm = confirmInput.value;
  if (confirm === "") {
    showError(confirmError, "Please confirm your password.");
    return false;
  }
  if (confirm !== pass) {
    showError(confirmError, "Passwords do not match.");
    return false;
  }
  clearError(confirmError);
  return true;
}
function validateForm() {
  let okName = validateName();
  let okEmail = validateEmail();
  let okPass = validatePassword();
  let okConfirm = validateConfirm();
  return okName && okEmail && okPass && okConfirm;
}
form.addEventListener("submit", function (event) {
  event.preventDefault();
  result.innerHTML = "";
  if (validateForm()) {
    result.innerHTML = "Form is valid!";
    result.className = "ok";
  } else {
    result.innerHTML = "Please fix the errors.";
    result.className = "error";
  }
});
```

<img alt="js-form-validation example 11 source" src="./code_sandbox/snaps/js-form-validation-11-code.png" />

<img alt="js-form-validation example 11 result" src="./code_sandbox/snaps/js-form-validation-11-result.png" />

- [x] **Outcome:** **Form is valid!** with class **ok**. Error paragraphs are empty.

<a id="js-form-validation-example-12"></a>

### **Example 12: Exercise 1: password must contain a digit**

- [x] Add **`/\d/`** (or `[0-9]`) to **validatePassword** after the length check.

Sandbox: `code_sandbox/js-form-validation/ex-password-number.html`

```javascript
if (!/\d/.test(value)) {
  showError(passError, "Password must contain at least one number.");
  return false;
}
```

<img alt="js-form-validation example 12 source" src="./code_sandbox/snaps/js-form-validation-12-code.png" />

<img alt="js-form-validation example 12 result" src="./code_sandbox/snaps/js-form-validation-12-result.png" />

- [x] **Outcome:** **password** (no digit) fails. **secret12** still passes.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-form-validation/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What happens on empty submit?

<details>
<summary>Answer</summary>

- [x] All four errors fill. Result **Please fix the errors.**

</details>

### Question 2: Valid Ada / ada@example.com / secret12 / secret12?

<details>
<summary>Answer</summary>

- [x] **Form is valid!** class **ok**.

</details>

### Question 3: Does `"  "` count as a name?

<details>
<summary>Answer</summary>

- [x] **No.** **trim** makes length **0**.

</details>

### Question 4: Email `ada@`?

<details>
<summary>Answer</summary>

- [x] **false** — **Enter a valid email address.**

</details>

### Question 5: Password `secret`?

<details>
<summary>Answer</summary>

- [x] **false** — need **8** characters.

</details>

### Question 6: Confirm empty vs mismatch?

<details>
<summary>Answer</summary>

- [x] **Please confirm your password.** vs **Passwords do not match.**

</details>

### Question 7: Without preventDefault?

<details>
<summary>Answer</summary>

- [x] The browser **submits/reloads**. You never see the JS result.

</details>

### Question 8: Exercise 1 extra rule?

<details>
<summary>Answer</summary>

- [x] Password must contain a **digit**. **password** fails; **secret12** passes.

</details>


</details>

## Summary

Stop the native submit, validate every field, write red errors under inputs, and only then show Form is valid!. Trim names/emails; require confirm to match. Add a digit rule if you want a slightly stronger password.

## References

- [JS Form Validation (W3Schools)](https://www.w3schools.com/js/js_project_form_validation.asp)
- [MDN: Event.preventDefault()](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
- [MDN: Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation)

</details>
