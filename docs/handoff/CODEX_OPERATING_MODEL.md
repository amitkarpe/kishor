# Codex Operating Model

## What Codex is expected to do

Codex should help maintain and extend the Kishor presentation repo as a repeatable Markdown-first publishing system.

Codex should be able to:

- choose the correct framework for a new request
- create new presentation folders
- preserve framework/source intent
- maintain metadata and indexing
- avoid editing old decks unless asked
- normalize legacy content into the new structure

## How to interpret future user requests

### Quiz requests

Examples:

- `Create quiz on Indian scientists using framework`
- `Create quiz on AWS IAM basics using framework`
- `Prepare Kahoot-style quiz deck on world inventors`

Default behavior:

- use the quiz framework
- also use the Kishor style system when slides are being created
- follow the two-phase workflow from the quiz framework
- keep the deck quiz-first

### Discussion requests

Examples:

- `Create discussion on courage using framework`
- `Create discussion on incident review culture using framework`
- `Create discussion on Shri Ram using framework`

Default behavior:

- use the discussion framework
- also use the Kishor style system when slides are being created
- start with a draft outline only
- wait for approval before full deck generation

## Framework-selection rules

Use this priority:

1. if the request explicitly says quiz, use `sources/quiz/Quiz_Framework_for_Kishor_Workflow_UPDATED.md`
2. if the request explicitly says discussion, use `sources/discussion/Discussion_Framework_for_Kishor_Workflow.md`
3. if the request is only about visual design or reusable style, use the style system files
4. if a deck is not Kishor-specific, fall back to the generic presentation style system

## Clarification rules

Codex should ask clarifying questions only when truly necessary.

Ask only when a missing detail would materially change the output, such as:

- category is unclear
- topic scope is ambiguous
- quantity/difficulty is essential for quiz design
- output mode is unclear
- a requested edit would overwrite existing deck content

If the missing detail is not blocking, make a KISS default and document it in `notes.md` or the relevant manifest.

## Existing-deck editing rules

Do not edit old decks unless the user explicitly asks.

Safe defaults:

- create a new folder for new work
- preserve old deck folders
- use versioning or new slugs when the topic is similar but content changes meaningfully

## Request-to-output pattern

### For new deck requests

1. identify category
2. load relevant framework
3. load relevant style system
4. create draft outline if required
5. wait for approval when the framework requires it
6. create `slides.md`, `meta.yml`, and `notes.md`
7. update homepage/index data
8. do not rewrite unrelated decks

### For legacy import requests

1. identify legacy source bundle
2. preserve provenance
3. normalize into repo structure
4. add import notes
5. update manifests
6. do not pretend inferred content is authoritative unless marked as such
