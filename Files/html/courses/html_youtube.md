# HTML YouTube

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

The easiest way to play video in HTML is **YouTube**. Skip local format conversion: upload the clip, copy the **video id**, and embed an **`<iframe>`**. This chapter covers the embed URL, **autoplay+mute**, **loop**, and **controls=0**.

This section has **2** examples:

- [x] **Example 1:** Embed [View](#html-youtube-example-01)
- [x] **Example 2:** URL parameters [View](#html-youtube-example-02)

## Detailed Explanation

- [x] **Why YouTube?** Converting files is slow. Let YouTube play the video on your page.
- [x] **Video id** — YouTube shows an id such as **`tgbNymZ7vqY`** when you save or play a video. Use that id in HTML.
- [x] **Autoplay + mute**
  - `autoplay=1` starts on visit — **annoying** for visitors.
  - Chromium blocks most autoplay; **muted autoplay is allowed**: `autoplay=1&mute=1`.
- [x] **Playlist / loop**
  - Playlist: comma-separated extra ids.
  - Loop forever: `playlist=videoID` **and** `loop=1`. `loop=0` (default) plays once.

<a id="html-youtube-example-01"></a>

### **Example 1: Embed**

- [x] **Embed steps:** upload → note the id → `<iframe>` → `src` = video URL → `width` / `height` → extra query params.
  - `src="https://www.youtube.com/embed/tgbNymZ7vqY"`

Sandbox: `code_sandbox/html-youtube/index.html`

```html
<iframe
  width="420"
  height="315"
  src="https://www.youtube.com/embed/tgbNymZ7vqY"
>
</iframe>
```

<img alt="html-youtube source" src="../code_sandbox/snaps/html-youtube-code.png" />

<img alt="html-youtube iframe result" src="../code_sandbox/snaps/html-youtube-result.png" />

- [x] **Outcome:** the page demonstrates **Embed** as shown in the result snap.

<a id="html-youtube-example-02"></a>

### **Example 2: URL parameters**

- [x] **Controls**
  - `controls=0` hides the player controls. Default `controls=1` shows them.
  - Sandbox: `params.html`.

Sandbox: `code_sandbox/html-youtube/params.html`

```html
<iframe src="https://www.youtube.com/embed/tgbNymZ7vqY?autoplay=1&mute=1">
  <iframe
    src="https://www.youtube.com/embed/tgbNymZ7vqY?playlist=tgbNymZ7vqY&loop=1"
  >
    <iframe
      src="https://www.youtube.com/embed/tgbNymZ7vqY?controls=0"
    ></iframe></iframe
></iframe>
```

<img alt="html-youtube params source" src="../code_sandbox/snaps/html-youtube-01-code.png" />

- [x] **Outcome:** the page demonstrates **URL parameters** as shown in the result snap.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/html/code_sandbox
python -m http.server 8766 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8766/html-youtube/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: Why embed YouTube instead of hosting the file?

<details>
<summary>Answer</summary>

- [x] Converting formats is **difficult and time-consuming**.
- [x] YouTube plays the video for you.

</details>

### Question 2: What is a YouTube video id?

<details>
<summary>Answer</summary>

- [x] A string such as **`tgbNymZ7vqY`**.
- [x] You use it in the embed URL.

</details>

### Question 3: Which element embeds the player?

<details>
<summary>Answer</summary>

- [x] **`<iframe>`** with `src="https://www.youtube.com/embed/ID"`.

</details>

### Question 4: How do you muted-autoplay a YouTube embed?

<details>
<summary>Answer</summary>

- [x] Add **`autoplay=1&mute=1`**.
- [x] Autoplay with sound is often **blocked** and is annoying.

</details>

### Question 5: How do you loop a YouTube video?

<details>
<summary>Answer</summary>

- [x] `loop=1` **and** `playlist=` the same video id.

</details>

### Question 6: How do you hide player controls?

<details>
<summary>Answer</summary>

- [x] **`controls=0`**. Default is `controls=1`.

</details>

</details>

## Summary

Upload to YouTube, copy the id, embed `youtube.com/embed/ID` in an iframe. Optional query params: muted autoplay, playlist+loop, controls=0.

## References

- [HTML YouTube Videos (W3Schools)](https://www.w3schools.com/html/html_youtube.asp)
- [YouTube IFrame Player API](https://developers.google.com/youtube/iframe_api_reference)
- [MDN: `<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
