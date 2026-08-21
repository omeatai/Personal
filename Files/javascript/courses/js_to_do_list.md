# JS To-Do List

[Back to JavaScript Tutorial](../tutorial_main.md)

## Introduction

A to-do list stored as an array in localStorage. displayTasks rebuilds the ul. addTask pushes non-empty text. removeTask uses splice(i, 1). clearAll assigns []. JSON.stringify / JSON.parse round-trip the array. The final file loads and displays on open. Exercises: alert on empty, Enter to add, Saved! after save.

This section has **11** examples:

- [x] **Example 1:** HTML: input #task, Add, ul #list, Clear All [View](#js-todo-list-example-01)
- [x] **Example 2:** displayTasks() — loop and innerHTML the <ul> [View](#js-todo-list-example-02)
- [x] **Example 3:** addTask() — push, clear input, save, display [View](#js-todo-list-example-03)
- [x] **Example 4:** removeTask(i) — splice(i, 1) [View](#js-todo-list-example-04)
- [x] **Example 5:** clearAll() — tasks = [] [View](#js-todo-list-example-05)
- [x] **Example 6:** saveTasks() — JSON.stringify into localStorage [View](#js-todo-list-example-06)
- [x] **Example 7:** loadTasks() — JSON.parse back into the array [View](#js-todo-list-example-07)
- [x] **Example 8:** Final project: load + display on page open [View](#js-todo-list-example-08)
- [x] **Example 9:** Exercise 1: alert if the task is empty [View](#js-todo-list-example-09)
- [x] **Example 10:** Exercise 2: press Enter to add a task [View](#js-todo-list-example-10)
- [x] **Example 11:** Exercise 3: show "Saved!" after saveTasks [View](#js-todo-list-example-11)

## Detailed Explanation

- [x] **`tasks` is an array.** Display with a **for** loop and **innerHTML**.
- [x] **`splice(i, 1)`** deletes one row. Re-display so **x** indexes stay correct.
- [x] Storage: **`JSON.stringify` / `JSON.parse`**. Skip parse when **getItem is null**.
- [x] Empty add **returns**. Exercise 1 **alerts** instead.

<a id="js-todo-list-example-01"></a>

### **Example 1: HTML: input #task, Add, ul #list, Clear All**

- [x] Need **`id="task"`**, **Add** → `addTask()`, **`<ul id="list">`**, **Clear All** → `clearAll()`.
- [x] Start with **`let tasks = []`**.

Sandbox: `code_sandbox/js-todo-list/html-skeleton.html`

```html
<h2>To-Do List</h2>
<input type="text" id="task" placeholder="New task">
<button type="button" onclick="addTask()">Add</button>
<ul id="list"></ul>
<button type="button" onclick="clearAll()">Clear All</button>
<script>
let tasks = [];
</script>
```

<img alt="js-todo-list example 1 source" src="../code_sandbox/snaps/js-todo-list-01-code.png" />

<img alt="js-todo-list example 1 result" src="../code_sandbox/snaps/js-todo-list-01-result.png" />

- [x] **Outcome:** Empty list, input, two buttons. **tasks** is **[]**.

<a id="js-todo-list-example-02"></a>

### **Example 2: displayTasks() — loop and innerHTML the <ul>**

- [x] Rebuild the list HTML whenever **tasks** changes.
- [x] Each row is the text plus an **x** that calls **`removeTask(i)`**.

Sandbox: `code_sandbox/js-todo-list/display-tasks.html`

```javascript
function displayTasks() {
  let html = "";
  for (let i = 0; i < tasks.length; i++) {
    html += "<li>" + tasks[i] + " x</li>";
  }
  document.getElementById("list").innerHTML = html;
}
```

<img alt="js-todo-list example 2 source" src="../code_sandbox/snaps/js-todo-list-02-code.png" />

<img alt="js-todo-list example 2 result" src="../code_sandbox/snaps/js-todo-list-02-result.png" />

- [x] **Outcome:** With tasks **Buy milk** and **Walk dog**, the ul shows **two** items.

<a id="js-todo-list-example-03"></a>

### **Example 3: addTask() — push, clear input, save, display**

- [x] Read **`#task`**. Empty string → **`return`** (no add).
- [x] `tasks.push(text)`, clear the input, **`saveTasks()`**, **`displayTasks()`**.

Sandbox: `code_sandbox/js-todo-list/add-task.html`

```javascript
function addTask() {
  let taskInput = document.getElementById("task");
  let text = taskInput.value;
  if (text === "") {
    return;
  }
  tasks.push(text);
  taskInput.value = "";
  saveTasks();
  displayTasks();
}
```

<img alt="js-todo-list example 3 source" src="../code_sandbox/snaps/js-todo-list-03-code.png" />

<img alt="js-todo-list example 3 result" src="../code_sandbox/snaps/js-todo-list-03-result.png" />

- [x] **Outcome:** Add **Read** then **Code**. List length **2**. Input cleared to **""**. Empty add leaves the list unchanged.

<a id="js-todo-list-example-04"></a>

### **Example 4: removeTask(i) — splice(i, 1)**

- [x] **`splice(i, 1)`** removes **1** item at index **i**.
- [x] Then save + display so the **x** buttons get **new indexes**.

Sandbox: `code_sandbox/js-todo-list/remove-task.html`

```javascript
function removeTask(i) {
  tasks.splice(i, 1);
  saveTasks();
  displayTasks();
}
```

<img alt="js-todo-list example 4 source" src="../code_sandbox/snaps/js-todo-list-04-code.png" />

<img alt="js-todo-list example 4 result" src="../code_sandbox/snaps/js-todo-list-04-result.png" />

- [x] **Outcome:** Start **[A, B, C]**. `removeTask(1)` → **[A, C]**.

<a id="js-todo-list-example-05"></a>

### **Example 5: clearAll() — tasks = []**

- [x] Replace the array with a **new empty** one, then save + display.

Sandbox: `code_sandbox/js-todo-list/clear-all.html`

```javascript
function clearAll() {
  tasks = [];
  saveTasks();
  displayTasks();
}
```

<img alt="js-todo-list example 5 source" src="../code_sandbox/snaps/js-todo-list-05-code.png" />

<img alt="js-todo-list example 5 result" src="../code_sandbox/snaps/js-todo-list-05-result.png" />

- [x] **Outcome:** After two tasks, Clear All → **[]** and **0** list items.

<a id="js-todo-list-example-06"></a>

### **Example 6: saveTasks() — JSON.stringify into localStorage**

- [x] localStorage stores **strings**. Arrays need **`JSON.stringify`**.

Sandbox: `code_sandbox/js-todo-list/save-tasks.html`

```javascript
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}
```

<img alt="js-todo-list example 6 source" src="../code_sandbox/snaps/js-todo-list-06-code.png" />

<img alt="js-todo-list example 6 result" src="../code_sandbox/snaps/js-todo-list-06-result.png" />

- [x] **Outcome:** `["Read","Code"]` is stored as the text **'["Read","Code"]'**.

<a id="js-todo-list-example-07"></a>

### **Example 7: loadTasks() — JSON.parse back into the array**

- [x] `JSON.parse` rebuilds the **array**. Skip if **`getItem` is null**.

Sandbox: `code_sandbox/js-todo-list/load-tasks.html`

```javascript
function loadTasks() {
  let saved = localStorage.getItem("tasks");
  if (saved !== null) {
    tasks = JSON.parse(saved);
  }
}
```

<img alt="js-todo-list example 7 source" src="../code_sandbox/snaps/js-todo-list-07-code.png" />

<img alt="js-todo-list example 7 result" src="../code_sandbox/snaps/js-todo-list-07-result.png" />

- [x] **Outcome:** Parse of **'["Read"]'** yields array **["Read"]**. Then **displayTasks()** (final project calls both on load).

<a id="js-todo-list-example-08"></a>

### **Example 8: Final project: load + display on page open**

- [x] End of the file: **`loadTasks(); displayTasks();`** (the page omits a semicolon after `displayTasks()` — ASI still runs it).
- [x] This snap seeds two tasks, reloads the list, then removes the first.

Sandbox: `code_sandbox/js-todo-list/final-project.html`

```html
let tasks = [];
function displayTasks() {
  let html = "";
  for (let i = 0; i < tasks.length; i++) {
    html += "<li>" + tasks[i] + " <button type=\"button\" onclick=\"removeTask(" + i + ")\">x</button></li>";
  }
  document.getElementById("list").innerHTML = html;
}
function addTask() {
  let taskInput = document.getElementById("task");
  let text = taskInput.value;
  if (text === "") {
    return;
  }
  tasks.push(text);
  taskInput.value = "";
  saveTasks();
  displayTasks();
}
function removeTask(i) {
  tasks.splice(i, 1);
  saveTasks();
  displayTasks();
}
function clearAll() {
  tasks = [];
  saveTasks();
  displayTasks();
}
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}
function loadTasks() {
  let saved = localStorage.getItem("tasks");
  if (saved !== null) {
    tasks = JSON.parse(saved);
  }
}
loadTasks();
displayTasks();
```

<img alt="js-todo-list example 8 source" src="../code_sandbox/snaps/js-todo-list-08-code.png" />

<img alt="js-todo-list example 8 result" src="../code_sandbox/snaps/js-todo-list-08-result.png" />

- [x] **Outcome:** List shows **Buy milk** and **Walk dog**. After `removeTask(0)` only **Walk dog** remains.

<a id="js-todo-list-example-09"></a>

### **Example 9: Exercise 1: alert if the task is empty**

- [x] Replace the silent `return` with **`alert(...)`** so empty add is visible.

Sandbox: `code_sandbox/js-todo-list/ex-alert-empty.html`

```javascript
if (text === "") {
  alert("Please enter a task");
  return;
}
```

<img alt="js-todo-list example 9 source" src="../code_sandbox/snaps/js-todo-list-09-code.png" />

<img alt="js-todo-list example 9 result" src="../code_sandbox/snaps/js-todo-list-09-result.png" />

- [x] **Outcome:** Empty add does **not** push. This sandbox records **Please enter a task** instead of a blocking `alert`.

<a id="js-todo-list-example-10"></a>

### **Example 10: Exercise 2: press Enter to add a task**

- [x] Listen for **`keydown`** / **`keyup`** on `#task`. If **`event.key === "Enter"`**, call **`addTask()`**.

Sandbox: `code_sandbox/js-todo-list/ex-enter-key.html`

```javascript
taskInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    addTask();
  }
});
```

<img alt="js-todo-list example 10 source" src="../code_sandbox/snaps/js-todo-list-10-code.png" />

<img alt="js-todo-list example 10 result" src="../code_sandbox/snaps/js-todo-list-10-result.png" />

- [x] **Outcome:** Dispatching **Enter** with value **Ship it** adds that task. Length **1**.

<a id="js-todo-list-example-11"></a>

### **Example 11: Exercise 3: show "Saved!" after saveTasks**

- [x] The project already saves on every change. Add a **Saved!** message in **`saveTasks`**.

Sandbox: `code_sandbox/js-todo-list/ex-saved-message.html`

```javascript
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
  document.getElementById("msg").innerHTML = "Saved!";
}
```

<img alt="js-todo-list example 11 source" src="../code_sandbox/snaps/js-todo-list-11-code.png" />

<img alt="js-todo-list example 11 result" src="../code_sandbox/snaps/js-todo-list-11-result.png" />

- [x] **Outcome:** After add, the message is **Saved!** and storage holds the new array.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/js-todo-list/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does addTask do with ""?

<details>
<summary>Answer</summary>

- [x] **return** — no push. Exercise 1 **alerts**.

</details>

### Question 2: `removeTask(1)` on [A,B,C]?

<details>
<summary>Answer</summary>

- [x] **[A, C]**. `splice(1, 1)`.

</details>

### Question 3: What does clearAll store?

<details>
<summary>Answer</summary>

- [x] **[]** (stringified).

</details>

### Question 4: Why JSON.stringify?

<details>
<summary>Answer</summary>

- [x] localStorage only holds **strings**, not arrays.

</details>

### Question 5: What runs on page load in the final file?

<details>
<summary>Answer</summary>

- [x] **`loadTasks()`** then **`displayTasks()`**.

</details>

### Question 6: Enter key exercise?

<details>
<summary>Answer</summary>

- [x] **keydown** on `#task`; if **Enter**, **addTask()**.

</details>

### Question 7: Saved! exercise?

<details>
<summary>Answer</summary>

- [x] Set a message inside **`saveTasks`** after setItem.

</details>

### Question 8: Why rebuild innerHTML after splice?

<details>
<summary>Answer</summary>

- [x] The **x** buttons encode **indexes**. Old indexes would be wrong.

</details>


</details>

## Summary

Keep tasks in an array, render the ul from scratch after each change, and persist with JSON in localStorage. Guard empty input; Enter and a Saved! note are small upgrades.

## References

- [JS To-Do List (W3Schools)](https://www.w3schools.com/js/js_project_todo.asp)
- [MDN: Array.prototype.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
- [MDN: JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
