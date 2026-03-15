# AGENTS.md

## Purpose
This repository prioritizes fast, low-friction iteration on `main`, reliable GitHub Pages deployment for Marp slides, and minimal branch confusion.

## Branching and PR policy
- `main` is the only long-lived branch.
- Every task must start from latest `main` and use a short-lived feature branch:
  - `feat/<topic>`
  - `fix/<topic>`
  - `chore/<topic>`
- All PRs must target `main` as base branch.
- Before opening a PR, rebase or merge latest `main` into your feature branch.
- Delete feature branch after merge.
- Do not use old demo branches (for example `marp-2-slides`) unless explicitly requested.

## Deployment workflow policy
- Keep one canonical Pages workflow: `.github/workflows/static.yml`.
- Workflow triggers must be:
  - `push` to `main`
  - `workflow_dispatch`
- Prefer first-party GitHub Actions where possible.
- Build Marp using:
  - `npx --yes @marp-team/marp-cli slides.md --html -o dist/index.html`
- Ensure `dist/.nojekyll` exists before upload.
- Deploy with `actions/deploy-pages`.

## Pages settings policy
- GitHub Pages Source must be **GitHub Actions**.
- If the site shows 404:
  1. Verify `slides.md` exists on `main`.
  2. Verify `.github/workflows/static.yml` exists on `main`.
  3. Rerun the workflow from the Actions tab.
  4. If failure happens at “Set up job”, check repository/organization Actions policy.

## Execution behavior for Codex
- Always show a brief plan before making changes.
- Prefer the smallest possible patch.
- Run checks after edits (lint/tests/build as applicable).
- For workflow edits, validate YAML syntax and relevant commands.
- If auth/push is unavailable, state it immediately and provide exact manual commands.

## Commit/PR behavior
- Use clear commit messages.
- Include what changed and why in PR body.
- Include exact verification commands in final summary.
- Never leave repository with uncommitted changes at handoff unless explicitly requested.

## Communication style
- Be concise and action-oriented.
- Always include a **What you should do now** section for manual follow-up.
- If multiple options exist, recommend one default path.

## Quick Start for Contributors
1. Update local `main`:
   - `git checkout main && git pull`
2. Create a feature branch:
   - `git checkout -b feat/<topic>`
3. Build slides locally:
   - `npx --yes @marp-team/marp-cli slides.md --html -o dist/index.html`
4. Open a PR with base branch set to `main`.
