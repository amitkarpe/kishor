# Presentation Style System - Workflow

**Status:** Draft v0.2  
**Owner:** Amit  
**Use case:** Reusable visual style system for presentation decks across multiple purposes  
**Scope:** Presentation style only. This file defines visual language, layout, slide behavior, and speaker-note style for general-purpose PPTX decks. It does **not** define topic workflow, discussion workflow, research workflow, or approval flow.

---

## 1) Purpose

Use this file whenever Amit wants a consistent visual style for a presentation.

This file should control:

- visual identity
- typography
- color usage
- layout behavior
- slide-type behavior
- speaker-note style
- closing-slide behavior

This file should **not** control:

- research workflow
- outline approval workflow
- topic-specific teaching logic
- discussion sequencing logic
- quiz rules

---

## 2) Design Intent

This visual system should feel:

- premium minimal
- dark and high contrast
- serious but modern
- bold without clutter
- suitable for teaching, strategy, internal decks, personal planning, reflection decks, and structured presentations
- readable on Zoom, projector, laptop, and screenshots

This is a clean, modern, reusable presentation style.

---

## 3) Fixed Visual Defaults

### Color palette

Use only these core colors unless Amit explicitly changes them:

- **Background black:** `#0B0B0B`
- **Text white:** `#FFFFFF`
- **Royal blue primary accent:** `#4169E1`
- **Orange pill-box highlight:** `#F59E0B`

### Color usage rules

- Use **black** for the main background on most slides.
- Use **white** for the main text.
- Use **royal blue** only for:
  - slide titles
  - section labels
- Use **orange** only as a **pill-box highlight** for selected keywords.
- Do not use orange for long text blocks.
- Do not introduce extra colors unless Amit explicitly asks.
- Avoid gradients, rainbow visuals, and random color variation.

### Background rule

- Default to **mostly black slides**.
- Dark background plus white text is the standard.
- Use white or light slides only if Amit explicitly asks.

---

## 4) Typography System

### Font feel

Use a **mix** of fonts with a clean modern look.

Default direction:

- primary display/title font: modern, strong, clean
- supporting/body font: simple, readable, sans-serif

Preferred fallback order:

1. Aptos
2. Arial
3. Calibri

### Typography rules

- Use **Title Case**
- Use **big left-aligned slide titles**
- Keep title text short and punchy
- Use **large, sparse body text**
- Prefer **2 to 4 ideas per slide**
- Keep line length short
- Use strong spacing between bullets
- Avoid dense paragraphs on slides
- Put the extra detail in speaker notes

### Body text rules

- Use short bullets or short punch lines
- Avoid paragraph-style slides
- Keep most bullet lines short
- Use orange pill-box only for one or two keywords when emphasis is truly needed

---

## 5) Layout Rules

### General layout

- Mostly left aligned
- Large margins
- Plenty of empty space
- Minimal shapes
- No visual crowding
- No header
- No footer
- No page numbers
- No logo or organization mark by default

### Spacing principles

- One clear visual hierarchy per slide
- Strong spacing between title and content
- Strong spacing between bullets
- Avoid placing content too close to slide edges
- Avoid bottom clutter

### Content density

Default density:

- **2 to 4 ideas per slide**
- one main message per slide
- if a slide feels crowded, split it

---

## 6) Generic Slide System Rules

Use these slide types as reusable building blocks.

### A. Title slide

Purpose:
- establish topic
- set tone
- create clarity

Rules:
- black background
- big left-aligned title
- optional one-line subtitle
- title may use royal blue
- no footer
- no extra clutter
- image only if essential and high quality

### B. Divider slide

Purpose:
- create a strong transition

Rules:
- **only title**
- no subtitle
- no quote
- no extra bullets
- black background
- title may use royal blue
- keep it visually sharp and minimal

### C. Hook slide

Purpose:
- open a section with one clear framing question

Rules:
- show **one big question only**
- do not show the prompt list on this slide
- place **2 to 5 prompts or hints in speaker notes**
- keep the slide visually open and sparse

### D. Prompt / hint slide

Purpose:
- keep the audience thinking after the hook

Rules:
- this slide may follow the hook slide when needed
- show the **2 to 5 prompts or hints**
- keep them short
- do not overload the slide

### E. Discussion / content slide

Purpose:
- explain a point clearly

Rules:
- structure = **question + 3 bullets**
- bullets should support the speaker, not replace the speaker
- keep the layout sparse
- use orange pill-box only for select emphasis
- image only if essential

### F. Comparison slide

Purpose:
- compare two ideas, options, states, or periods

Rules:
- use a clean two-column layout
- keep both sides balanced
- keep text short
- use the same color discipline as the rest of the deck

### G. Process slide

Purpose:
- show steps, flow, or sequence

Rules:
- show 3 to 5 steps maximum on one slide
- keep step labels short
- split into multiple slides if needed

### H. Reflection slide

Purpose:
- make the topic practical, personal, or memorable

Rules:
- ask one reflection question or one reflection statement
- keep it calm and uncluttered

### I. Closing challenge slide

Purpose:
- end with action

Rules:
- **one challenge only**
- if the previous slide is already a reflection slide, closing slide should stay as **one challenge only**
- if there is no reflection slide before closing, the closing slide may contain **reflection + challenge**, but the **challenge must be the last point**

---

## 7) Speaker Notes Rules

Speaker notes should be:

- bullet talking points
- concise
- easy to speak from
- structured for flow

Do not write essays in speaker notes.

Use notes for:

- hook prompts
- examples
- transitions
- questions to ask
- what to stress verbally
- likely audience reactions
- one key takeaway

Default speaker-note structure:

- main point
- why it matters
- one example
- one question or prompt
- intended takeaway

---

## 8) Image, Icon, and Shape Rules

### Images

- use images **only when essential**
- image must improve clarity, emotion, or engagement
- avoid generic stock overload
- prefer one strong image instead of many small ones

### Icons / emoji

- moderate use only
- use as visual anchors, not decoration overload
- keep icon style consistent

### Shapes

- minimal shapes only
- keep shapes simple
- avoid decorative frames and busy design blocks

---

## 9) Strict Do Not Use List

Do not use the following unless Amit explicitly asks:

- multicolor themes
- decorative header
- decorative footer
- page numbers
- logo placement
- dense paragraphs
- tiny text
- busy collages
- too many shapes
- too many icons
- orange text paragraphs
- low-contrast gray text on dark background

---

## 10) Quality Checklist Before Final PPTX

Before finalizing, check:

1. Is the palette limited to black, white, royal blue, and orange?
2. Is orange used only as a pill-box highlight?
3. Is blue used only in titles or section labels?
4. Are titles big and left aligned?
5. Are slides sparse and readable?
6. Is there no header, footer, page number, or logo?
7. Is the hook slide one big question only?
8. Does the prompt / hint slide follow the hook when needed?
9. Does the discussion slide use question + 3 bullets?
10. Does the closing follow the reflection/challenge rule?

If any answer is "no", fix the deck before delivering.

---

## 11) Current Defaults

These should now be treated as the presentation-style defaults unless Amit changes them later:

- font feel: mix
- title case: Title Case
- keyword style: orange pill-box
- blue usage: titles or section labels
- page numbers: no
- logo: no
- divider slide: title only
- hook slide: one big question only, prompts in notes
- prompt slide: 2 to 5 prompts or hints
- discussion slide: question + 3 bullets
- closing slide: one challenge only, with conditional reflection logic as defined above
