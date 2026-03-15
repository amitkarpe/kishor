# Import Notes

## Import philosophy

Legacy materials should be imported conservatively.

Preserve:

- original topic intent
- category
- provenance
- useful speaker notes or structural logic

Normalize when needed:

- folder naming
- metadata fields
- note structure
- asset placement
- Markdown formatting for Marp compatibility

## Current package scope

This handoff package includes:

- authoritative framework/source docs
- sample Marp decks
- metadata stubs and notes for legacy discussion decks
- external-reference notes for legacy bundles that are not embedded

This package does **not** include:

- PPTX binaries
- full extracted slide content from every prior PPTX deck
- assets copied out of old decks

## Recommended import workflow for Codex

1. identify the legacy source
2. record provenance in `notes.md`
3. create or confirm target slug
4. create `meta.yml`
5. convert or recreate `slides.md` if source content is available
6. normalize assets into local `assets/`
7. update manifests and index data

## Current known external legacy sources

- `Kishor_Discussion_Series_10_PPTX.zip` — downloaded separately by user
- `Kishor_Quiz_Decks_Bundle.zip` — downloaded separately by user

These should be treated as external import sources and not as files inside this package.

## Legacy normalization contract

Preferred normalized shape:

- `slides.md`
- `meta.yml`
- `notes.md`
- `assets/`

If content is not available yet, keep:

- `meta.yml`
- `notes.md`

and mark status clearly as `pending_import_from_external_bundle`.
