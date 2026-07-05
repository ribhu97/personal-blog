---
title: "Your Post Title"
date: 2026-07-05
description: "One sentence dek — this appears below the title in serif, and as the meta description."
categories: ["safety"]   # one of: safety | research | builds | sports | essays
tags: ["mech-interp", "probes"]
image: images/your-og-image.jpeg
substack: ""             # paste Substack URL here if cross-posting; shows "also on Substack ↗" link
draft: true
---

## Section heading

Body copy is written in plain markdown. Source Serif 4 on the site, renders fine as-is in Obsidian.

### Sub-heading

Paragraph text. Link like this: [anchor text](https://example.com).

**Bold text.** *Italic text.* `inline code`.

---

## Pull quote / blockquote

> Write a pull quote like this. It gets rendered as a styled red-bordered blockquote.
> Multi-line is fine.

---

## Figures with captions

Drop images into `exampleSite/static/images/` then reference with a root-relative path.
The alt text becomes the figure caption on the site.

![This text becomes the caption below the image](/images/your-image.jpeg)

Do NOT use Obsidian wikilinks (`![[image.jpeg]]`) — they won't resolve on the site.

---

## Code blocks

Use standard fenced code blocks. They render as dark-background mono blocks.

```python
def example():
    return "renders as dark code block"
```

---

## Footnotes

Use standard Goldmark / Pandoc footnote syntax — works verbatim in Obsidian.

Body reference[^1] and another one[^2].

[^1]: First footnote text. Can include [links](https://example.com).
[^2]: Second footnote text.

Footnotes render in a styled NOTES section at the bottom of the post.

---

## Ordered / unordered lists

- Item one
- Item two
  - Nested item

1. First
2. Second

---

## Publishing checklist

- [ ] Fill in `title`, `date`, `description`
- [ ] Set correct `categories` value (drives breadcrumb + chip)
- [ ] Add relevant `tags`
- [ ] Add `image` path (drop file in `exampleSite/static/images/`)
- [ ] Add `substack` URL if cross-posting
- [ ] Set `draft: false` when ready
- [ ] Drop file into `exampleSite/content/posts/your-slug.md`
- [ ] Images drop into `exampleSite/static/images/`
