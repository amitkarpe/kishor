# Content Standards

## Shared standards

These apply to all decks unless a category-specific framework overrides them.

- Markdown-first
- Marp-aware
- one main purpose per deck
- easy-to-browse metadata
- preserve framework intent
- speaker notes should remain concise and useful
- do not mix quiz and discussion logic in one deck unless explicitly requested

## Marp conventions

Recommended front matter baseline:

```yaml
---
marp: true
theme: default
paginate: false
---
```

Adjust theme and pagination only when needed.

## Quiz deck standards

Quiz decks should:

- be quiz-first, not lecture-first
- move quickly
- use clear question wording
- avoid overexplaining on every slide
- work well in live group settings
- follow the quiz framework's phase-based approval model

Recommended deck shape:

- title
- short instructions or warm-up
- repeating question/answer rhythm
- optional short value or context wrap-up
- concise close

## Discussion deck standards

Discussion decks should:

- be question-led
- use hook -> prompt/hint -> discussion flow
- use question + 3 bullets on discussion slides
- support speaker facilitation rather than replace it
- end in reflection and/or challenge according to the framework

## Tone standards

### Kishor decks
Use the Kishor-specific framework and style files.

### Non-Kishor decks
Use the generic presentation style system unless a topic-specific source exists.

## Source referencing rules

When Codex uses source files, it should preserve provenance in `notes.md` or deck generation notes.

Recommended note style:

- framework used
- style system used
- assumptions made
- source files referenced
- imported/normalized from legacy material if applicable

## Quality standards before publishing

Check:

- category is correct
- slug is clean
- metadata is complete
- structure matches the relevant framework
- no unrelated deck was modified
- description is short and useful for the homepage
