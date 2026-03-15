# Repo Target Structure

## Goal

Convert the repo from a single-deck Marp demo into a multi-presentation static site that can scale cleanly across quiz and discussion sessions.

## Published content layout

```text
repo-root/
  quiz/
    <slug>/
      slides.md
      meta.yml
      notes.md
      assets/
  discussion/
    <slug>/
      slides.md
      meta.yml
      notes.md
      assets/
  docs/
    handoff/
    manifests/
    sources/
      quiz/
      discussion/
      style/
      shared/
  legacy-import/
    quiz/
    discussion/
  templates/
    quiz/
    discussion/
  scripts/
    build-site.sh
    build_site.py
  .github/workflows/static.yml
  README.md
  AGENTS.md
```

## Folder intent

- `quiz/<slug>/`: one published quiz deck per folder
- `discussion/<slug>/`: one published discussion deck per folder
- `docs/sources/`: source frameworks, style systems, and shared authoring references
- `docs/handoff/`: planning and operating context imported from the handoff package
- `docs/manifests/`: source and presentation inventory from the handoff package
- `legacy-import/`: staging area for older PPTX-derived or not-yet-normalized decks
- `templates/`: reusable starter files for future deck creation
- `scripts/`: build and index generation logic

## Presentation-folder contract

Each published deck should normally contain:

- `slides.md`
- `meta.yml`
- `notes.md`
- optional `assets/`

## Build model

- build all published decks from root-level `quiz/` and `discussion/`
- generate `dist/index.html` as the homepage
- generate each deck at `dist/<category>/<slug>/index.html`
- keep source docs in the repo but out of the published deck URL structure

## Metadata shape

Recommended baseline:

- title
- category
- topic
- slug
- date
- description
- tags
- status

Optional extras can be added later if they help import, search, or PPTX export.
