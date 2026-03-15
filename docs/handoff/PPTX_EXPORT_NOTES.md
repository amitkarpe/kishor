# PPTX Export Notes

## Positioning

PPTX is optional and secondary.

The repo should remain:

- Markdown-first
- Marp-first
- GitHub Pages-first

## Practical future options

Possible export paths later:

1. Marp PDF/HTML export plus separate conversion workflow
2. Dedicated PPTX generator from normalized content
3. Adjacent export tooling that reads `slides.md` and `meta.yml`

## Recommended stance

Do not redesign the repo around PPTX export.

Instead:

- keep deck content clean in Markdown
- keep metadata predictable
- keep notes concise
- add export support later as an optional build path

## What to preserve now for future PPTX support

- stable per-deck folder structure
- slide source in Markdown
- metadata in YAML
- speaker/import notes in `notes.md`
- predictable slug and category structure

## Important note for this handoff

Current PPTX bundles are external to this ZIP and were intentionally excluded by user instruction.
