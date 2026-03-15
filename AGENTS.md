# AGENTS.md

## Purpose

This repository is a Markdown-first, Marp-first presentation system for Kishor sessions.

The live site is published on GitHub Pages and should support many presentations over time, grouped into:
- `quiz`
- `discussion`

## Core repo rules

- Keep published decks at repo root:
  - `quiz/<slug>/`
  - `discussion/<slug>/`
- Keep one deck per folder.
- Each deck should normally contain:
  - `slides.md`
  - `meta.yml`
  - `notes.md`
- Optional deck assets belong in:
  - `assets/`

Do not create new published decks under `docs/`.

## Source and framework rules

Authoritative source/framework files live under:
- `docs/sources/quiz/`
- `docs/sources/discussion/`
- `docs/sources/style/`
- `docs/sources/shared/`

Use these files first when the user asks to create or revise a deck:
- `docs/sources/quiz/Quiz_Framework_for_Kishor_Workflow_UPDATED.md`
- `docs/sources/discussion/Discussion_Framework_for_Kishor_Workflow.md`
- `docs/sources/style/Kishor_Presentation_Style_System_Workflow.md`
- `docs/sources/style/Presentation_Style_System_Workflow.md`

Supporting references:
- `docs/sources/shared/authoring_principles.md`
- `docs/sources/shared/deck_shapes.md`
- `docs/sources/shared/metadata_schema.md`
- `docs/sources/shared/quality_checklist.md`

If a user asks for a:
- quiz deck: use quiz framework + Kishor style by default
- discussion deck: use discussion framework + Kishor style by default
- non-Kishor or generic design task: use the generic style system as needed

## Templates

Starter templates live in:
- `templates/quiz/`
- `templates/discussion/`

Prefer copying/adapting those templates when creating a new deck.

## Build and deployment policy

Keep one canonical Pages workflow:
- `.github/workflows/static.yml`

Workflow triggers must remain:
- `push` to `main`
- `workflow_dispatch`

The site build entrypoint is:
- `bash scripts/build-site.sh`

The Python builder:
- reads deck metadata from `quiz/*/meta.yml` and `discussion/*/meta.yml`
- renders each deck with Marp
- generates the homepage index
- copies local assets
- creates `dist/.nojekyll`

Prefer the smallest possible patch when updating the workflow or build logic.

## Homepage/index rules

The homepage must:
- group decks by category
- show title, category, date, and short description
- link to each deck folder

Each built deck should also keep a link back to the homepage.

## Legacy import rules

Use `legacy-import/` as staging only.

Current legacy materials are not canonical published content. Normalize them into fresh Marp deck folders before publishing.

Do not overwrite a published deck with raw imported PPTX-derived material unless explicitly requested.

## Execution behavior for Codex

- Always show a brief plan before making changes.
- Prefer the smallest repo-consistent patch.
- Follow KISS: keep it short and simple.
- Amit prefers 80-90% useful framework-fit over chasing the last 10-20% of polish.
- Do not spend excessive tokens trying to perfect visual details once the workflow/framework fit is good enough.
- When creating a new deck, create a new folder instead of editing an old one unless the user explicitly asks for edits.
- Preserve source provenance in `notes.md`.
- Run relevant checks after edits:
  - `python3 scripts/build_site.py`
  - optional spot checks in `dist/`
- For workflow issues, inspect the latest failed GitHub Actions run before changing Pages settings.

## Commit and handoff

- Use clear, task-focused commit messages.
- Keep docs aligned with behavior changes.
- Never leave unrelated generated files committed unless needed.
- In final summaries, include exact verification commands and a clear next action for the user.
- Keep work on `main` unless Amit explicitly asks for branch/PR flow.

## Current scope note

- Do not try to convert all legacy decks now.
- Current migration scope is only:
  - 2 quiz decks total
  - 2 discussion decks total
- `discussion/what-is-dharma-really/` counts as the first discussion migration.
