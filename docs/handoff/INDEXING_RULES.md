# Indexing Rules

## Purpose

The homepage/index should make it easy to browse all presentations by category and recency.

## Minimum data per presentation

Each presentation entry should include:

- title
- category
- slug
- date
- short description
- tags
- path
- status

## Grouping

Group homepage entries by category:

1. quiz
2. discussion

## Sort order

Default sort order inside each category:

- newest first by date
- if dates match, sort alphabetically by title

## Description style

Descriptions should be:

- short
- plain
- one sentence
- useful to a browsing human

Good examples:

- `A discussion deck on dharma, duty, and right action for Kishor sessions.`
- `A fast quiz deck on Indian science legends for group play.`

Avoid:

- vague slogans
- long paragraphs
- hidden metadata inside descriptions

## Path rule

Store path as a repo-relative folder path, for example:

- `discussion/proud-hindu-today/`
- `quiz/indian-science-legends/`

## Suggested index data file

Use one simple shared data file such as:

- `docs/data/presentations.yml`

Each entry can be derived from each deck's `meta.yml` if automation is added later.
