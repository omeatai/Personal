# HTML Video

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The HTML **`<video>`** element shows a video on a page. This chapter covers **`controls`**, **`<source>`** fallbacks, **width/height**, **autoplay** (and **muted** autoplay in Chromium), formats (**MP4, WebM, Ogg**), and a small **JavaScript** play/pause/size demo. Sample clip: **Big Buck Bunny**.

This section has **3** examples:

- [x] **Example 1:** Controls [View](#html-video-example-01)
- [x] **Example 2:** Muted autoplay [View](#html-video-example-02)
- [x] **Example 3:** JavaScript [View](#html-video-example-03)

## Detailed Explanation

- [x] **Formats** — MP4 (`video/mp4`), WebM (`video/webm`), Ogg (`video/ogg`). Safari: MP4 and WebM yes, **Ogg no**. Other listed browsers: all three.
- [x] **Tags:** `<video>` video; `<source>` alternate files; `<track>` text tracks.

<a id="html-video-example-01"></a>

### **Example 1: Controls**

- [x] **Markup**
  - `controls` adds play, pause, and volume.
  - Always set **width and height** so the page does not flicker while the video loads.
  - `<source>` lists alternatives; the browser uses the **first recognized** format.
  - Text between the tags shows only if `<video>` is **unsupported**.

Sandbox: `code_sandbox/html-video/index.html`

```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.ogg" type="video/ogg" />
  Your browser does not support the video tag.
</video>
```

<img alt="html-video source" src="../code_sandbox/snaps/html-video-code.png" />

<img alt="html-video controls result" src="../code_sandbox/snaps/html-video-result.png" />

- [x] **Outcome:** a **320×240** video player with native **controls** (play, pause, volume).

<a id="html-video-example-02"></a>

### **Example 2: Muted autoplay**

- [x] **Autoplay**
  - `autoplay` starts the video automatically.
  - **Chromium** usually blocks autoplay **with sound**. **Muted autoplay is allowed**: `autoplay muted`.
  - Sandbox: `autoplay.html`.

Sandbox: `code_sandbox/html-video/autoplay.html`

```html
<video width="320" height="240" autoplay muted>
  <source src="movie.mp4" type="video/mp4" />
</video>
```

<img alt="html-video autoplay source" src="../code_sandbox/snaps/html-video-01-code.png" />

<img alt="html-video autoplay muted result" src="../code_sandbox/snaps/html-video-01-result.png" />

- [x] **Outcome:** the clip starts by itself because **`autoplay muted`** is set (Chromium blocks autoplay with sound).

<a id="html-video-example-03"></a>

### **Example 3: JavaScript**

- [x] **DOM** — methods/properties/events to load, play, pause, set duration and volume.
  - Buttons: **Play/Pause**, **Big**, **Small**, **Normal**.
  - Sandbox: `js.html`.

Sandbox: `code_sandbox/html-video/js.html`

```html
<button onclick="playPause()">Play/Pause</button>
<button onclick="makeBig()">Big</button>
<button onclick="makeSmall()">Small</button>
<button onclick="makeNormal()">Normal</button>
```

<img alt="html-video js source" src="../code_sandbox/snaps/html-video-02-code.png" />

<img alt="html-video javascript controls result" src="../code_sandbox/snaps/html-video-02-result.png" />

- [x] **Outcome:** the browser shows **Play/Pause**, **Big**, **Small**, **Normal**.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-video/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What does `controls` add?

<details>
<summary>Answer</summary>

- [x] Play, pause, and volume (and the rest of the native control bar).

</details>

### Question 2: Why set width and height on `<video>`?

<details>
<summary>Answer</summary>

- [x] So the page does not **flicker** while the video loads.

</details>

### Question 3: How do `<source>` elements work?

<details>
<summary>Answer</summary>

- [x] They list **alternative files**.
- [x] The browser uses the **first format it recognizes**.

</details>

### Question 4: How do you autoplay in Chrome?

<details>
<summary>Answer</summary>

- [x] Use **`autoplay muted`**.
- [x] Chromium often **blocks** autoplay with sound.

</details>

### Question 5: Which video formats does HTML support?

<details>
<summary>Answer</summary>

- [x] **MP4**, **WebM**, **Ogg**.
- [x] Safari does **not** support Ogg in this table.

</details>

### Question 6: Which tags go with video?

<details>
<summary>Answer</summary>

- [x] `<video>`, `<source>`, `<track>`.

</details>

</details>

## Summary

Use `<video>` with `controls`, width/height, and `<source>` fallbacks. Autoplay in Chromium needs `muted`. Formats: MP4, WebM, Ogg. The DOM can play, pause, and resize.

## References

- [HTML Video (W3Schools)](https://www.w3schools.com/html/html5_video.asp)
- [HTML Audio/Video DOM](https://www.w3schools.com/tags/ref_av_dom.asp)
- [MDN: `<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
- [MDN: Autoplay guide](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)
