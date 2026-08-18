# JavaScript Tutorial — Build Plan (JS Home → JS JSONP)

Master plan and **resume tracker** for documenting the full W3Schools JavaScript course into
`Files/javascript/tutorial.md`, following the rule
`Files/javascript/.cursor/rules/javascript_tutorial.mdc`.

Scope: **every tutorial page from `JS Home` (top) down to `JS JSONP` (bottom)** in left-nav order.
The trailing meta items after JSONP (JS Examples, JS Browser, JS Editor, JS Exercises, JS Quiz,
JS Website, JS Syllabus, JS Study Plan, JS Interview Prep, JS Bootcamp, JS Certificate) are **out of scope**.

---

## How to use this plan (read on every resume)

1. Find the **first unchecked page** below (top to bottom). That is the next task.
2. Do the page end-to-end per the rule: **read → rebuild every example in the sandbox → run → snap code + result → append one accordion** to `tutorial.md`. The accordion **Introduction** must list **every** Example title (all N of them).
3. Tick the page here (`[ ]` → `[x]`) and update **Resume pointer** at the top of the tracker.
4. Make **one git commit per page** (workflow rule: one task = one unit of work), then the user can `git push`.
5. Move to the next unchecked page. Never batch multiple pages into one commit unless explicitly asked.

**Improvement pass:** pages tagged `(exists — improve)` already have an accordion in `tutorial.md` from an
earlier, thinner pass. Rewrite them to the current, more-detailed standard (every example rebuilt + run + snapped,
richer explanations, 8–15 Q&A). Replace the existing `<summary>` block in place (ask before replacing per the rule),
do **not** duplicate it.

### Status legend

- `[ ]` not started
- `[x]` done to current standard (examples rebuilt, run, snapped, accordion appended/updated, committed)
- Tag `(exists — improve)` = an older accordion exists and must be upgraded, not created fresh.
- Tag `(new)` = no accordion yet.

### Per-page checklist (the "definition of done")

- [ ] Section read fully in the browser (all headings, notes, tables, warnings, every Tryit example).
- [ ] Sandbox folder `code_sandbox/<slug>/` created with **one HTML file per Example** (plus `index.html` hub).
- [ ] Examples run over http (or `node` for console-only) and match the page.
- [ ] Per-example snaps saved to `code_sandbox/snaps/`: `<slug>-NN-code.png` + `<slug>-NN-result.png`
      (NN matches the Example heading order; never one shared pair for a whole method table).
- [ ] One accordion appended/updated in `tutorial.md` (Introduction, Detailed Explanation, Terminal Commands,
      Questions and Answers, Summary, References) with every example's written outcome.
- [ ] **Introduction lists every Example title** (Example 1 … Example N) matching the Detailed Explanation
      headings exactly — if there are 34 examples, list all 34; do not summarize or omit.
- [ ] Each Introduction example line ends with **`[View](#<slug>-example-NN)`**, and the matching
      `<a id="<slug>-example-NN"></a>` sits immediately before that `### **Example N:**` heading.
- [ ] **Coverage count:** number of `### **Example` headings ≥ number of Tryits + reference-table rows +
      named constructs on the page (HTML wrappers may be one grouped Example that still runs every wrapper).
      Introduction title-list count must equal that Example heading count.
- [ ] Single git commit made for this page.

#### Grain (do not collapse)

Model section: **JS Output** — one `### Example N` per named method (`innerHTML`, `innerText`, `document.write()`,
`alert()`, `console.log()`), each with its own sandbox file and snaps.

**Forbidden (real failure):** **JS String Reference** listed Access / Search / Transform methods in bullets and
only fenced `trim()`. A name list is not an Example. On a **reference table**, every row (`at()`, `charAt()`,
`slice()`, `replace()`, `split()`, … through `valueOf()`) needs its own Example heading, tested code, snaps,
and written outcome. Teaching pages with many Tryits of the same method (`slice(7,13)`, `slice(7)`, `slice(-12)`)
are also **one Example per Tryit**, not one combined dump.

This applies to every later catalog too: Number / Array / Math / Date / Map / Set / RegExp / Object / Function
Reference pages, operator lists, and overview pages that name `if` / `else` / `switch` / `for` / `while`.

### Conventions

- **Slug** = page title lowercased, spaces → hyphens, punctuation dropped
  (e.g. `JS Numbers` → `js-numbers`, `toString()` → `js-tostring`, `var/let/const` → `js-varletconst`).
- **Commit message** first line: `S.P: <Page Title> — document JS tutorial section`
  (e.g. `6.1: JS Numbers — document JS tutorial section`). Stage `tutorial.md`, the page sandbox, and its snaps.
- **Base URL** for each page: `https://www.w3schools.com/js/<file>.asp`.
- **Local server** from `Files/javascript/code_sandbox`, e.g. `py -3 -m http.server 8770 --bind 127.0.0.1`,
  then open `http://127.0.0.1:8770/<slug>/`.
- **Range names are parents.** The user names sidebar **groups**, not the child landing page that
  reuses the same label. `"apply to JS Objects to JS Dates"` includes every Object child **and**
  every Date child through **JS Date Methods**, not only `js_dates.asp`. See
  `Files/javascript/.cursor/rules/javascript_tutorial.mdc`.

---

## Resume pointer

- **Next task:** `17.12` JS Destructuring (new).
- **Last completed:** `17.11` JS Type Conversion.
- **Notes:** Rule + this plan now require **JS Output grain** (one `### Example` per Tryit / table row /
  named construct) and an **Introduction table of contents** that lists **every** Example title with a
  **`[View](#<slug>-example-NN)`** jump link (Example 1 … Example N; 39 titles on String Reference).
  `tutorial.md` already has both. Per-page git commits for `3.1`–`5.5` were not made in that correction
  pass (user asked for the rewrite, not commits).

---

## Section-level progress (high level)

- [ ] **S0** Getting Started (3 + Home)
- [ ] **S1** Syntax & Variables (7)
- [ ] **S2** Operators (4)
- [ ] **S3** Conditionals (7)
- [ ] **S4** Loops (6)
- [ ] **S5** Strings (5)
- [x] **S6** Numbers (6)
- [x] **S7** Functions (10)
- [x] **S8** Objects (7)
- [x] **S9** Scope (5)
- [x] **S10** Dates (5)
- [x] **S11** Arrays (8)
- [x] **S12** Sets (5)
- [x] **S13** Maps (4)
- [x] **S14** Iterations (4)
- [x] **S15** Math (3)
- [x] **S16** RegExp (10)
- [ ] **S17** Data Types (12)
- [ ] **S18** Errors (4)
- [ ] **S19** Debugging (6)
- [ ] **S20** Style Guide & Best Practices (4)
- [ ] **S21** Reference (5)
- [ ] **S22** Projects (5)
- [ ] **S23** Versions (17)
- [ ] **S24** JS HTML DOM (9)
- [ ] **S25** JS HTML Events (7)
- [ ] **S26** JS HTML First (4)
- [ ] **S27** JS Window API / BOM (8)
- [ ] **S28** JS JSON (8)
- [ ] **S29** JS Web API (6)
- [ ] **S30** JS Temporal (21)
- [ ] **S31** Functions Advanced (11)
- [ ] **S32** Objects Advanced (9)
- [ ] **S33** Classes (3)
- [ ] **S34** Asynchronous (13)
- [ ] **S35** Modules (5)
- [ ] **S36** Meta & Proxy (4)
- [ ] **S37** Typed Arrays & Atomics (6)
- [ ] **S38** DOM Navigation (4)
- [ ] **S39** Graphics (6)
- [ ] **S40** AJAX (10)
- [ ] **S41** jQuery (4)
- [ ] **S42** JSONP (1)

---

## Detailed page tracker

### S0 — Getting Started

- [ ] `0.1` JS Home — `default.asp` (new)
- [x] `0.2` JS Introduction — `js_intro.asp` (exists — improve)
- [x] `0.3` JS Where To — `js_whereto.asp` (exists — improve)
- [x] `0.4` JS Output — `js_output.asp` (exists — improve)

### S1 — Syntax & Variables

- [x] `1.1` JS Syntax — `js_syntax.asp` (exists — improve)
- [x] `1.2` JS Statements — `js_statements.asp` (exists — improve)
- [x] `1.3` JS Comments — `js_comments.asp` (exists — improve)
- [x] `1.4` JS Variables — `js_variables.asp` (exists — improve)
- [x] `1.5` JS Let — `js_let.asp` (exists — improve)
- [x] `1.6` JS Const — `js_const.asp` (exists — improve)
- [x] `1.7` JS Types — `js_types.asp` (exists — improve)

### S2 — Operators

- [x] `2.1` JS Operators — `js_operators.asp` (exists — improve)
- [x] `2.2` JS Arithmetic — `js_arithmetic.asp` (exists — improve)
- [x] `2.3` JS Assignment — `js_assignment.asp` (exists — improve)
- [x] `2.4` JS Comparisons — `js_comparisons.asp` (exists — improve)

### S3 — Conditionals

- [x] `3.1` JS Conditional — `js_conditionals.asp` (exists — improve)
- [x] `3.2` JS If Conditions — `js_if.asp` (exists — improve)
- [ ] `3.3` JS If Else — `js_if_else.asp` (new)
- [ ] `3.4` JS Ternary — `js_if_ternary.asp` (new)
- [ ] `3.5` JS Switch — `js_switch.asp` (new)
- [ ] `3.6` JS Booleans — `js_booleans.asp` (new)
- [ ] `3.7` JS Logical — `js_logical.asp` (new)

### S4 — Loops

- [x] `4.1` JS Loops — `js_loops.asp` (exists — improve)
- [x] `4.2` JS Loop for — `js_loop_for.asp` (exists — improve)
- [x] `4.3` JS Loop while — `js_loop_while.asp` (exists — improve)
- [x] `4.4` JS Break — `js_break.asp` (exists — improve)
- [x] `4.5` JS Continue — `js_continue.asp` (exists — improve)
- [x] `4.6` JS Control Flow — `js_control_flow.asp` (exists — improve)

### S5 — Strings

- [x] `5.1` JS Strings — `js_strings.asp` (exists — improve)
- [x] `5.2` JS String Templates — `js_string_templates.asp` (exists — improve)
- [x] `5.3` JS String Methods — `js_string_methods.asp` (exists — improve)
- [x] `5.4` JS String Search — `js_string_search.asp` (exists — improve)
- [x] `5.5` JS String Reference — `js_string_reference.asp` (exists — improve)

### S6 — Numbers

- [x] `6.1` JS Numbers — `js_numbers.asp` (new)
- [x] `6.2` JS Number Methods — `js_number_methods.asp` (new)
- [x] `6.3` JS Number Properties — `js_number_properties.asp` (new)
- [x] `6.4` JS Number Reference — `js_number_reference.asp` (new)
- [x] `6.5` JS Bitwise — `js_bitwise.asp` (new)
- [x] `6.6` JS BigInt — `js_bigint.asp` (new)

### S7 — Functions

- [x] `7.1` JS Functions — `js_functions.asp` (new)
- [x] `7.2` Function Intro — `js_function_intro.asp` (new)
- [x] `7.3` Function Invocation — `js_function_invocation.asp` (new)
- [x] `7.4` Function Parameters — `js_function_parameters.asp` (new)
- [x] `7.5` Function Returns — `js_function_return.asp` (new)
- [x] `7.6` Function Arguments — `js_function_arguments.asp` (new)
- [x] `7.7` Function Expressions — `js_function_expressions.asp` (new)
- [x] `7.8` Function Arrow — `js_arrow_function.asp` (new)
- [x] `7.9` Function Quiz — `js_function_quiz.asp` (new)
- [x] `7.10` JS Timers — `js_timers.asp` (new)

### S8 — Objects

- [x] `8.1` JS Objects — `js_objects.asp` (new)
- [x] `8.2` Object Intro — `js_object_intro.asp` (new)
- [x] `8.3` Object Properties — `js_object_properties.asp` (new)
- [x] `8.4` Object Methods — `js_object_methods.asp` (new)
- [x] `8.5` Object this — `js_object_this.asp` (new)
- [x] `8.6` Object Display — `js_object_display.asp` (new)
- [x] `8.7` Object Constructors — `js_object_constructors.asp` (new)

### S9 — Scope

- [x] `9.1` JS Scope — `js_scope.asp` (new)
- [x] `9.2` JS Code Blocks — `js_codeblocks.asp` (new)
- [x] `9.3` JS Hoisting — `js_hoisting.asp` (new)
- [x] `9.4` JS var/let/const — `js_varletconst.asp` (new)
- [x] `9.5` JS Strict Mode — `js_strict.asp` (new)

### S10 — Dates

- [x] `10.1` JS Dates — `js_dates.asp` (new)
- [x] `10.2` JS Date Formats — `js_date_formats.asp` (new)
- [x] `10.3` JS Date Get — `js_date_methods.asp` (new)
- [x] `10.4` JS Date Set — `js_date_methods_set.asp` (new)
- [x] `10.5` JS Date Methods — `js_date_reference.asp` (new)

### S11 — Arrays

- [x] `11.1` JS Arrays — `js_arrays.asp` (new)
- [x] `11.2` JS Array Constructor — `js_array_constructor.asp` (new)
- [x] `11.3` JS Array Methods — `js_array_methods.asp` (new)
- [x] `11.4` JS Array Search — `js_array_search.asp` (new)
- [x] `11.5` JS Array Sort — `js_array_sort.asp` (new)
- [x] `11.6` JS Array Iterations — `js_array_iteration.asp` (new)
- [x] `11.7` JS Array Reference — `js_array_reference.asp` (new)
- [x] `11.8` JS Array const — `js_array_const.asp` (new)

### S12 — Sets

- [x] `12.1` JS Sets — `js_sets.asp` (new)
- [x] `12.2` JS Set Methods — `js_set_methods.asp` (new)
- [x] `12.3` JS Set Logic — `js_set_logic.asp` (new)
- [x] `12.4` JS Set WeakSet — `js_sets_weak.asp` (new)
- [x] `12.5` JS Set Reference — `js_set_reference.asp` (new)

### S13 — Maps

- [x] `13.1` JS Maps — `js_maps.asp` (new)
- [x] `13.2` JS Map Methods — `js_map_methods.asp` (new)
- [x] `13.3` JS Map WeakMap — `js_maps_weak.asp` (new)
- [x] `13.4` JS Map Reference — `js_map_reference.asp` (new)

### S14 — Iterations

- [x] `14.1` JS Iterations — `js_looping.asp` (new)
- [x] `14.2` JS Iterables — `js_iterables.asp` (new)
- [x] `14.3` JS Iterators — `js_iterators.asp` (new)
- [x] `14.4` JS Generators — `js_generators.asp` (new)

### S15 — Math

- [x] `15.1` JS Math — `js_math.asp` (new)
- [x] `15.2` JS Math Reference — `js_math_reference.asp` (new)
- [x] `15.3` JS Math Random — `js_random.asp` (new)

### S16 — RegExp

- [x] `16.1` JS RegExp — `js_regexp.asp` (new)
- [x] `16.2` JS RegExp Flags — `js_regexp_flags.asp` (new)
- [x] `16.3` JS RegExp Classes — `js_regexp_characters.asp` (new)
- [x] `16.4` JS RegExp Metachars — `js_regexp_meta_characters.asp` (new)
- [x] `16.5` JS RegExp Assertions — `js_regexp_assertions.asp` (new)
- [x] `16.6` JS RegExp Groups — `js_regexp_groups.asp` (new)
- [x] `16.7` JS RegExp Quantifiers — `js_regexp_quantifiers.asp` (new)
- [x] `16.8` JS RegExp Patterns — `js_regexp_patterns.asp` (new)
- [x] `16.9` JS RegExp Objects — `js_regexp_objects.asp` (new)
- [x] `16.10` JS RegExp Methods — `js_regexp_methods.asp` (new)

### S17 — Data Types

- [x] `17.1` JS Data Types — `js_datatypes.asp` (new)
- [x] `17.2` JS Primitive Data — `js_datatypes_primitives.asp` (new)
- [x] `17.3` JS Object Types — `js_datatypes_objects.asp` (new)
- [x] `17.4` JS Symbols — `js_datatypes_symbol.asp` (new)
- [x] `17.5` JS typeof — `js_typeof.asp` (new)
- [x] `17.6` JS undefined — `js_undefined.asp` (new)
- [x] `17.7` JS NaN — `js_nan.asp` (new)
- [x] `17.8` JS toString() — `js_tostring.asp` (new)
- [x] `17.9` JS toLocaleString() — `js_tolocalestring.asp` (new)
- [x] `17.10` JS Type Coercion — `js_type_coercion.asp` (new)
- [x] `17.11` JS Type Conversion — `js_type_conversion.asp` (new)
- [ ] `17.12` JS Destructuring — `js_destructuring.asp` (new)

### S18 — Errors

- [ ] `18.1` JS Errors Intro — `js_errors_intro.asp` (new)
- [ ] `18.2` JS Errors Silent — `js_errors_silent.asp` (new)
- [ ] `18.3` JS Error Statements — `js_errors.asp` (new)
- [ ] `18.4` JS Error Object — `js_error_object.asp` (new)

### S19 — Debugging

- [ ] `19.1` Debug Intro — `js_debugging.asp` (new)
- [ ] `19.2` Debug Console — `js_debugging_console.asp` (new)
- [ ] `19.3` Debug Breakpoints — `js_debugging_breakpoints.asp` (new)
- [ ] `19.4` Debug Errors — `js_debugging_errors.asp` (new)
- [ ] `19.5` Debug Async — `js_debugging_async.asp` (new)
- [ ] `19.6` Debug Reference — `js_debugging_reference.asp` (new)

### S20 — Style Guide & Best Practices

- [ ] `20.1` JS Style Guide — `js_conventions.asp` (new)
- [ ] `20.2` JS Best Practices — `js_best_practices.asp` (new)
- [ ] `20.3` JS Mistakes — `js_mistakes.asp` (new)
- [ ] `20.4` JS Performance — `js_performance.asp` (new)

### S21 — Reference

- [ ] `21.1` JS Alphabetic — `js_alphabetic_reference.asp` (new)
- [ ] `21.2` JS Statements (Reference) — `js_statements_reference.asp` (new)
- [ ] `21.3` JS Keywords — `js_reserved.asp` (new)
- [ ] `21.4` JS Operators (Reference) — `js_operators_reference.asp` (new)
- [ ] `21.5` JS Precedence — `js_precedence.asp` (new)

### S22 — Projects

- [ ] `22.1` JS Counter — `js_project_counter.asp` (new)
- [ ] `22.2` JS Event Listener (Project) — `js_project_eventlistener.asp` (new)
- [ ] `22.3` JS To-Do List — `js_project_todo.asp` (new)
- [ ] `22.4` JS Modal Popup — `js_project_modal_popup.asp` (new)
- [ ] `22.5` JS Form Validation (Project) — `js_project_form_validation.asp` (new)

### S23 — Versions

- [ ] `23.1` JS 2027 — `js_2027.asp` (new)
- [ ] `23.2` JS 2026 — `js_2026.asp` (new)
- [ ] `23.3` JS 2025 — `js_2025.asp` (new)
- [ ] `23.4` JS 2024 — `js_2024.asp` (new)
- [ ] `23.5` JS 2023 — `js_2023.asp` (new)
- [ ] `23.6` JS 2022 — `js_2022.asp` (new)
- [ ] `23.7` JS 2021 — `js_2021.asp` (new)
- [ ] `23.8` JS 2020 — `js_2020.asp` (new)
- [ ] `23.9` JS 2019 — `js_2019.asp` (new)
- [ ] `23.10` JS 2018 — `js_2018.asp` (new)
- [ ] `23.11` JS 2017 — `js_2017.asp` (new)
- [ ] `23.12` JS 2016 — `js_2016.asp` (new)
- [ ] `23.13` JS 2015 (ES6) — `js_es6.asp` (new)
- [ ] `23.14` JS 2009 (ES5) — `js_es5.asp` (new)
- [ ] `23.15` JS 1999 (ES3) — `js_es3.asp` (new)
- [ ] `23.16` JS Versions — `js_versions.asp` (new)
- [ ] `23.17` JS History — `js_history.asp` (new)

### S24 — JS HTML DOM

- [ ] `24.1` HTML DOM — `js_htmldom.asp` (new)
- [ ] `24.2` HTML DOM API — `js_htmldom_methods.asp` (new)
- [ ] `24.3` Selecting Elements — `js_htmldom_elements.asp` (new)
- [ ] `24.4` Changing HTML — `js_htmldom_html.asp` (new)
- [ ] `24.5` Changing CSS — `js_htmldom_css.asp` (new)
- [ ] `24.6` Form Validation — `js_validation.asp` (new)
- [ ] `24.7` DOM Animations — `js_htmldom_animate.asp` (new)
- [ ] `24.8` Document Reference — `js_htmldom_document.asp` (new)
- [ ] `24.9` Element Reference — `js_htmldom_element_reference.asp` (new)

### S25 — JS HTML Events

- [ ] `25.1` Intro to Events — `js_events.asp` (new)
- [ ] `25.2` Mouse Events — `js_events_mouse.asp` (new)
- [ ] `25.3` Keyboard Events — `js_events_keyboard.asp` (new)
- [ ] `25.4` Load Events — `js_events_load.asp` (new)
- [ ] `25.5` Manage Events — `js_events_management.asp` (new)
- [ ] `25.6` Event Examples — `js_htmldom_events.asp` (new)
- [ ] `25.7` Event Listener — `js_htmldom_eventlistener.asp` (new)

### S26 — JS HTML First

- [ ] `26.1` HTML First — `js_htmlfirst.asp` (new)
- [ ] `26.2` HTML Progressive — `js_htmlfirst_progressive.asp` (new)
- [ ] `26.3` HTML First Features — `js_htmlfirst_features.asp` (new)
- [ ] `26.4` HTML First CSS — `js_htmlfirst_css.asp` (new)

### S27 — JS Window API (BOM)

- [ ] `27.1` JS Window — `js_window.asp` (new)
- [ ] `27.2` JS Screen — `js_window_screen.asp` (new)
- [ ] `27.3` JS Location — `js_window_location.asp` (new)
- [ ] `27.4` JS History — `js_window_history.asp` (new)
- [ ] `27.5` JS Navigator — `js_window_navigator.asp` (new)
- [ ] `27.6` JS Popup Alert — `js_popup.asp` (new)
- [ ] `27.7` JS Cookies — `js_cookies.asp` (new)
- [ ] `27.8` JS Fetch API — `js_api_fetch.asp` (new)

### S28 — JS JSON

- [ ] `28.1` JSON Intro — `js_json.asp` (new)
- [ ] `28.2` JSON Syntax — `js_json_syntax.asp` (new)
- [ ] `28.3` JSON Values — `js_json_datatypes.asp` (new)
- [ ] `28.4` JSON Parse — `js_json_parse.asp` (new)
- [ ] `28.5` JSON Stringify — `js_json_stringify.asp` (new)
- [ ] `28.6` JSON Fetch — `js_json_server.asp` (new)
- [ ] `28.7` JSON HTML — `js_json_html.asp` (new)
- [ ] `28.8` JSON vs XML — `js_json_xml.asp` (new)

### S29 — JS Web API

- [ ] `29.1` APIs Intro — `js_api_intro.asp` (new)
- [ ] `29.2` API Geolocation — `js_api_geolocation.asp` (new)
- [ ] `29.3` API Web Pointer — `js_api_pointer_events.asp` (new)
- [ ] `29.4` API Web Storage — `js_api_web_storage.asp` (new)
- [ ] `29.5` API Validation — `js_validation_api.asp` (new)
- [ ] `29.6` API Web Worker — `js_api_web_workers.asp` (new)

### S30 — JS Temporal

- [ ] `30.1` Temporal Intro — `js_temporal.asp` (new)
- [ ] `30.2` Temporal Why — `js_temporal_intro.asp` (new)
- [ ] `30.3` Temporal vs Date — `js_temporal_vs_date.asp` (new)
- [ ] `30.4` Temporal Duration — `js_temporal_duration.asp` (new)
- [ ] `30.5` Temporal Instant — `js_temporal_instant.asp` (new)
- [ ] `30.6` Temporal PlainDateTime — `js_temporal_plaindatetime.asp` (new)
- [ ] `30.7` Temporal PlainDate — `js_temporal_plain.asp` (new)
- [ ] `30.8` Temporal PlainYearM — `js_temporal_plainyearmonth.asp` (new)
- [ ] `30.9` Temporal PlainMonthD — `js_temporal_plainmonthday.asp` (new)
- [ ] `30.10` Temporal PlainTime — `js_temporal_plaintime.asp` (new)
- [ ] `30.11` Temporal ZonedDate — `js_temporal_zoneddatetime.asp` (new)
- [ ] `30.12` Temporal Now — `js_temporal_now.asp` (new)
- [ ] `30.13` Temporal Arithmetic — `js_temporal_arithmetic.asp` (new)
- [ ] `30.14` Temporal Since/Until — `js_temporal_differences.asp` (new)
- [ ] `30.15` Temporal Compare — `js_temporal_compare.asp` (new)
- [ ] `30.16` Temporal Conversion — `js_temporal_conversion.asp` (new)
- [ ] `30.17` Temporal Formats — `js_temporal_formats.asp` (new)
- [ ] `30.18` Temporal Mistakes — `js_temporal_mistakes.asp` (new)
- [ ] `30.19` Temporal Migrate — `js_temporal_migrate.asp` (new)
- [ ] `30.20` Temporal Standards — `js_temporal_standards.asp` (new)
- [ ] `30.21` Temporal Reference — `js_temporal_reference.asp` (new)

### S31 — Functions Advanced

- [ ] `31.1` Functions Advanced — `js_function_advanced.asp` (new)
- [ ] `31.2` Function Definitions — `js_function_definition.asp` (new)
- [ ] `31.3` Function Callbacks — `js_callback.asp` (new)
- [ ] `31.4` Function this — `js_function_this.asp` (new)
- [ ] `31.5` Function Call — `js_function_call.asp` (new)
- [ ] `31.6` Function Apply — `js_function_apply.asp` (new)
- [ ] `31.7` Function Bind — `js_function_bind.asp` (new)
- [ ] `31.8` Function IIFE — `js_function_iife.asp` (new)
- [ ] `31.9` Function Closures — `js_function_closures.asp` (new)
- [ ] `31.10` Function Reference — `js_function_reference.asp` (new)
- [ ] `31.11` Function Quiz (Advanced) — `js_function_advanced_quiz.asp` (new)

### S32 — Objects Advanced

- [ ] `32.1` Objects Advanced — `js_object_advanced.asp` (new)
- [ ] `32.2` Object Definitions — `js_object_definition.asp` (new)
- [ ] `32.3` Object this — `js_this.asp` (new)
- [ ] `32.4` Object Iterations — `js_object_iterations.asp` (new)
- [ ] `32.5` Object Get / Set — `js_object_accessors.asp` (new)
- [ ] `32.6` Object Management — `js_object_management.asp` (new)
- [ ] `32.7` Object Protection — `js_object_protection.asp` (new)
- [ ] `32.8` Object Prototypes — `js_object_prototypes.asp` (new)
- [ ] `32.9` Object Reference — `js_object_reference.asp` (new)

### S33 — Classes

- [ ] `33.1` JS Classes — `js_classes.asp` (new)
- [ ] `33.2` JS Class Inheritance — `js_class_inheritance.asp` (new)
- [ ] `33.3` JS Class Static — `js_class_static.asp` (new)

### S34 — Asynchronous

- [ ] `34.1` JS Asynchronous — `js_asynchronous.asp` (new)
- [ ] `34.2` Async Programming — `js_async.asp` (new)
- [ ] `34.3` Async Callbacks — `js_async_callbacks.asp` (new)
- [ ] `34.4` Async Promises — `js_async_promises.asp` (new)
- [ ] `34.5` Async Await — `js_async_await.asp` (new)
- [ ] `34.6` Async Parallel — `js_async_parallel.asp` (new)
- [ ] `34.7` Async Event Loop — `js_async_event_loop.asp` (new)
- [ ] `34.8` Async Fetch API — `js_async_fetch.asp` (new)
- [ ] `34.9` Async Mistakes — `js_async_mistakes.asp` (new)
- [ ] `34.10` Async Debugging — `js_async_debug.asp` (new)
- [ ] `34.11` Async AbortControl — `js_async_abortcontroller.asp` (new)
- [ ] `34.12` Async Web Workers — `js_async_webworkers.asp` (new)
- [ ] `34.13` Async Reference — `js_promise_reference.asp` (new)

### S35 — Modules

- [ ] `35.1` Modules Intro — `js_modules.asp` (new)
- [ ] `35.2` Modules Export — `js_modules_export.asp` (new)
- [ ] `35.3` Modules Import — `js_modules_import.asp` (new)
- [ ] `35.4` Modules Namespace — `js_modules_namespace.asp` (new)
- [ ] `35.5` Modules Dynamic — `js_modules_dynamic.asp` (new)

### S36 — Meta & Proxy

- [ ] `36.1` Meta Programming — `js_meta_programming.asp` (new)
- [ ] `36.2` Meta Reflect — `js_meta_reflect.asp` (new)
- [ ] `36.3` Meta Proxy — `js_meta_proxy.asp` (new)
- [ ] `36.4` Meta Reference — `js_meta_reference.asp` (new)

### S37 — Typed Arrays & Atomics

- [ ] `37.1` Typed Arrays — `js_typed_arrays.asp` (new)
- [ ] `37.2` Typed Methods — `js_typed_methods.asp` (new)
- [ ] `37.3` Typed Reference — `js_typed_reference.asp` (new)
- [ ] `37.4` Array Buffers — `js_arraybuffers.asp` (new)
- [ ] `37.5` DataViews — `js_dataview.asp` (new)
- [ ] `37.6` JS Atomics — `js_atomics.asp` (new)

### S38 — DOM Navigation

- [ ] `38.1` DOM Navigation — `js_htmldom_navigation.asp` (new)
- [ ] `38.2` DOM Nodes — `js_htmldom_nodes.asp` (new)
- [ ] `38.3` DOM Collections — `js_htmldom_collections.asp` (new)
- [ ] `38.4` DOM Node Lists — `js_htmldom_nodelist.asp` (new)

### S39 — Graphics

- [ ] `39.1` JS Graphics — `js_graphics.asp` (new)
- [ ] `39.2` JS Canvas — `js_graphics_canvas.asp` (new)
- [ ] `39.3` JS Plotly — `js_graphics_plotly.asp` (new)
- [ ] `39.4` JS Chart.js — `js_graphics_chartjs.asp` (new)
- [ ] `39.5` JS Google Chart — `js_graphics_google_chart.asp` (new)
- [ ] `39.6` JS D3.js — `js_graphics_d3js.asp` (new)

### S40 — AJAX

- [ ] `40.1` AJAX Intro — `js_ajax_intro.asp` (new)
- [ ] `40.2` AJAX XMLHttp — `js_ajax_http.asp` (new)
- [ ] `40.3` AJAX Request — `js_ajax_http_send.asp` (new)
- [ ] `40.4` AJAX Response — `js_ajax_http_response.asp` (new)
- [ ] `40.5` AJAX XML File — `js_ajax_xmlfile.asp` (new)
- [ ] `40.6` AJAX PHP — `js_ajax_php.asp` (new)
- [ ] `40.7` AJAX ASP — `js_ajax_asp.asp` (new)
- [ ] `40.8` AJAX Database — `js_ajax_database.asp` (new)
- [ ] `40.9` AJAX Applications — `js_ajax_applications.asp` (new)
- [ ] `40.10` AJAX Examples — `js_ajax_examples.asp` (new)

### S41 — jQuery

- [ ] `41.1` jQuery Selectors — `js_jquery_selectors.asp` (new)
- [ ] `41.2` jQuery HTML — `js_jquery_elements.asp` (new)
- [ ] `41.3` jQuery CSS — `js_jquery_css.asp` (new)
- [ ] `41.4` jQuery DOM — `js_jquery_dom.asp` (new)

### S42 — JSONP (endpoint)

- [ ] `42.1` JS JSONP — `js_json_jsonp.asp` (new)

---

## Out of scope (after JSONP)

`JS Examples`, `JS HTML DOM (examples)`, `JS HTML Input`, `JS HTML Objects`, `JS HTML Events (examples)`,
`JS Browser`, `JS Editor`, `JS Exercises`, `JS Quiz`, `JS Website`, `JS Syllabus`, `JS Study Plan`,
`JS Interview Prep`, `JS Bootcamp`, `JS Certificate`.
