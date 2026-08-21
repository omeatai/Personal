# HTML Media

[Back to HTML Tutorial](../tutorial_main.md)

## Introduction

**Multimedia** on the web is sound, music, videos, movies, and animations. This chapter lists common **file extensions**, which **video and audio formats HTML supports**, and which older formats do **not** play in browsers. There is **no Try it Yourself** example on this page.

This section has **1** example:

- [x] **Example 1:** Format tables (no Tryit) [View](#html-media-example-01)

## Detailed Explanation

- [x] **What is multimedia?**
  - Almost anything you can **hear or see**: images, music, sound, videos, films, animations.
  - Pages mix **different types and formats**.
- [x] **Browser support**
  - Early browsers: **text only**, one font, one color.
  - Later: colors, fonts, images, and multimedia.
- [x] **Formats**
  - Media lives in **files**. The usual hint is the **extension**: `.wav` `.mp3` `.mp4` `.mpg` `.wmv` `.avi`.
- [x] **Video formats** (page table)

| Format       | File         | Notes                                                       |
| ------------ | ------------ | ----------------------------------------------------------- |
| MPEG         | `.mpg/.mpeg` | First popular web video. **Not supported in HTML** anymore. |
| AVI          | `.avi`       | Microsoft. Cameras/TV. Windows, **not browsers**.           |
| WMV          | `.wmv`       | Microsoft. **Not browsers**.                                |
| QuickTime    | `.mov`       | Apple. **Not browsers**.                                    |
| RealVideo    | `.rm/.ram`   | Streaming. **Does not play in browsers**.                   |
| Flash        | `.swf/.flv`  | Often needs a **plug-in**.                                  |
| Ogg          | `.ogg`       | Theora Ogg. **Supported by HTML**.                          |
| WebM         | `.webm`      | Mozilla, Opera, Adobe, Google. **Supported by HTML**.       |
| MPEG-4 / MP4 | `.mp4`       | **All browsers**. **Recommended by YouTube**.               |

- **Note:** Only **MP4, WebM, and Ogg** video are supported by the HTML standard.

- [x] **Audio formats**

| Format    | File         | Notes                                                                 |
| --------- | ------------ | --------------------------------------------------------------------- |
| MIDI      | `.mid/.midi` | Notes, not recorded sound. **Not browsers**.                          |
| RealAudio | `.rm/.ram`   | **Does not play in browsers**.                                        |
| WMA       | `.wma`       | Microsoft. **Not browsers**.                                          |
| AAC       | `.aac`       | Apple / iTunes. **Not browsers** (as a raw `.aac` type on this page). |
| WAV       | `.wav`       | IBM/Microsoft. **Supported by HTML**.                                 |
| Ogg       | `.ogg`       | **Supported by HTML**.                                                |
| MP3       | `.mp3`       | Best compressed recorded music. **All browsers**.                     |
| MP4       | `.mp4`       | Video container that can hold audio. **All browsers**.                |

- **Note:** Only **MP3, WAV, and Ogg** audio are supported by the HTML standard.
- If the site is **recorded music**, choose **MP3**.

<a id="html-media-example-01"></a>

### **Example 1: Format tables (no Tryit)**

- [x] This chapter has **no Tryit page**. It is a format catalog; `<video>` and `<audio>` markup are in the next chapters.
- [x] HTML video: **MP4, WebM, Ogg**. HTML audio: **MP3, WAV, Ogg**.

```text
# No code snippets in this topic.
```

- [x] **Outcome:** there is nothing to render here — only the format tables above.

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

No server was started for this section (no sandbox page to open).

```bash
# none
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What counts as multimedia here?

<details>
<summary>Answer</summary>

- [x] Sound, music, videos, movies, animations — anything you can **hear or see**.

</details>

### Question 2: How do you usually tell a media file’s type?

<details>
<summary>Answer</summary>

- [x] By the **file extension** (`.mp3`, `.mp4`, `.wav`, …).

</details>

### Question 3: Which video formats does HTML support?

<details>
<summary>Answer</summary>

- [x] **MP4**, **WebM**, and **Ogg**.

</details>

### Question 4: Which video format does YouTube recommend?

<details>
<summary>Answer</summary>

- [x] **MP4**.

</details>

### Question 5: Which audio formats does HTML support?

<details>
<summary>Answer</summary>

- [x] **MP3**, **WAV**, and **Ogg**.

</details>

### Question 6: What should a recorded-music site use?

<details>
<summary>Answer</summary>

- [x] **MP3** — compressed, high quality, all browsers.

</details>

### Question 7: Do AVI, WMV, and MOV play in the HTML video element?

<details>
<summary>Answer</summary>

- [x] **No** (per this chapter). They play on desktop hardware/OS players, not as HTML-standard video types.

</details>

</details>

## Summary

HTML video is **MP4, WebM, Ogg** (YouTube: MP4). HTML audio is **MP3, WAV, Ogg** (music: MP3). Older types (MPEG, AVI, WMV, MOV, Flash, MIDI, WMA) are not the HTML media standard.

## References

- [HTML Multimedia (W3Schools)](https://www.w3schools.com/html/html_media.asp)
- [HTML Video](https://www.w3schools.com/html/html5_video.asp)
- [HTML Audio](https://www.w3schools.com/html/html5_audio.asp)
- [MDN: Media type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Formats)
