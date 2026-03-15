# Project Information For Kishor Presentations

## Mission

This repository should become a long-lived presentation knowledge base for Kishor sessions and adjacent youth-learning use cases.

The system should support:

- repeatable presentation creation
- Markdown-first authoring
- Marp-based publishing
- GitHub Pages hosting
- easy addition of future decks by Codex Cloud
- preservation of reusable frameworks and style systems

## Primary content categories

### 1. Quiz

Quiz decks are quiz-first sessions.

Typical characteristics:

- fast pacing
- lighter content density
- live use in Zoom or group settings
- quiz mechanics first, values or explanations second
- compatible with the quiz framework source

### 2. Discussion

Discussion decks are discussion-first sessions.

Typical characteristics:

- question-led structure
- prompt/hint flow
- reflection and challenge ending
- speaker-led facilitation
- compatible with the discussion framework source

## Intended audience

Inferred default audience:

- Hindu kids / teens
- roughly ages 12 to 17
- live group sessions
- need for readable, high-contrast slides
- content should be engaging, structured, and discussion-friendly

## Markdown-first publishing model

The repo should treat Markdown as the primary source of truth.

Preferred content layers:

1. `slides.md` as the presentation source
2. `meta.yml` as compact metadata
3. `notes.md` for speaker notes, import notes, or generation notes
4. optional `assets/` for local images

PPTX export may exist later, but Markdown/HTML is the primary system.

## Why GitHub Pages and Marp matter

This repo is hosted on GitHub Pages and already uses Marp CLI.

This means the structure should favor:

- local relative links
- deterministic folder layout
- one folder per presentation
- easy static build rules
- simple homepage/index generation
- lightweight authoring with minimal extra tooling

## Working principle

Codex should maintain a stable system where:

- every new presentation gets a new folder
- existing decks are not overwritten unless explicitly requested
- frameworks remain easy to find
- homepage updates are predictable
- metadata is simple and consistent
