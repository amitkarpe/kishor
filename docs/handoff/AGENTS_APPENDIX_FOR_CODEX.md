# AGENTS Appendix For Codex

## Purpose

This document is designed so its content can be copied or adapted into future `AGENTS.md` repo instructions.

## Core rule

Treat this repo as a Markdown-first, Marp-first, GitHub Pages presentation system with two primary content categories:

- quiz
- discussion

## Primary source files

### Quiz workflow
Use:
- `docs/sources/quiz/Quiz_Framework_for_Kishor_Workflow_UPDATED.md`

When to use:
- quiz requests
- quiz deck creation
- Kahoot-style or quiz-first content
- quiz-first PPTX/slide requests

### Discussion workflow
Use:
- `docs/sources/discussion/Discussion_Framework_for_Kishor_Workflow.md`

When to use:
- discussion requests
- question-led value/history/culture talks
- discussion-first slide creation

### Kishor-specific visual style
Use:
- `docs/sources/style/Kishor_Presentation_Style_System_Workflow.md`

When to use:
- Kishor decks
- youth-facing decks
- slide styling for quiz/discussion content

### Generic visual style
Use:
- `docs/sources/style/Presentation_Style_System_Workflow.md`

When to use:
- non-Kishor decks
- topic-neutral decks
- reusable presentation style outside the Kishor context

## Minimal selection map

- request contains "quiz" -> quiz workflow + Kishor style
- request contains "discussion" -> discussion workflow + Kishor style
- request is only about visual design -> style system
- request is not Kishor-specific -> generic style system

## Safe defaults

- create new deck folder instead of editing old ones
- use lowercase hyphenated slugs
- keep metadata simple
- preserve source provenance in `notes.md`
- ask clarifying questions only when necessary

## Minimum per-deck file set

- `slides.md`
- `meta.yml`
- `notes.md`

Optional:

- `assets/`

## Index maintenance rule

Whenever a new deck is added, update the shared presentation index or equivalent homepage data source.
