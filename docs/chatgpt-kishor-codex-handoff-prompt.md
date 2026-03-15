# ChatGPT Handoff Prompt For Kishor Presentation Repo

Use the following prompt in ChatGPT. It is written so ChatGPT can prepare a clean handoff package for this repository and for future Codex Cloud work.

```text
You are ChatGPT helping prepare a durable handoff package for a GitHub repository that hosts Marp-based presentations on GitHub Pages.

Your job is to prepare a complete collaboration package for a separate coding agent, Codex Cloud, which will work inside the repository and turn the materials you provide into a long-term presentation system.

Important: do not give a short answer. Produce a complete, practical package specification and then provide the files in a ZIP if your environment supports it. If you cannot return a ZIP directly, provide:
- a full file tree
- the full contents of all text files
- a short note describing which files should be saved where

The repository context and expectations are below.

==================================================
PROJECT CONTEXT
==================================================

Repository:
- GitHub repo: `https://github.com/amitkarpe/kishor`
- GitHub Pages site: `https://amitkarpe.github.io/kishor/`

Current technical baseline:
- The repository currently uses Marp Markdown presentations.
- GitHub Pages deployment uses GitHub Actions.
- Current Pages workflow builds HTML using Marp CLI and deploys with Pages actions.
- The currently working build command is:
  `npx --yes @marp-team/marp-cli slides.md --html -o dist/index.html`
- The workflow also creates `dist/.nojekyll` and deploys with `actions/deploy-pages`.

Important operational facts:
- This repo is becoming a long-lived knowledge base and hosted site for many presentations.
- Future presentations will be created by Codex Cloud, not manually each time.
- Content creation will be driven by topic requests and a growing library of Markdown source/framework files.
- The future system should stay Markdown-first and Marp-first.
- PPTX is optional and secondary. Markdown/HTML is the primary format.

High-level future goal:
- The site should host many presentations over time.
- There are 2 presentation categories:
  - `quiz`
  - `discussion`
- Every presentation must live in its own new folder.
- Every presentation should be linked from a homepage/index page.
- Homepage entries should be grouped by category.
- Each homepage entry should show:
  - title
  - category
  - date
  - short description

Expected URL/folder style:
- `quiz/<slug>/`
- `discussion/<slug>/`

Source-input rules:
- Source inputs are Markdown files only.
- The user will upload or paste Markdown from ChatGPT Projects and other working notes.
- Example source/framework files that may exist now or later:
  - `Quiz_Framework_for_Kishor_Workflow_UPDATED.md`
  - `Discussion_Framework_for_Kishor_Workflow.md`
  - `Presentation_Style_System_Workflow.md`
  - `Kishor_Presentation_Style_System_Workflow.md`
- There may also be many additional source or context files you decide are useful.

Source-location expectation:
- Codex should be able to keep framework/source files in a clear folder structure inside the repo.
- Those source files should be easy to reference from repo instructions and future agent guidance.
- The repo should eventually have AGENTS instructions that point Codex to the important source/framework files.

Operating model for future Codex requests:
- The user will ask things like:
  - `Create quiz on <TOPIC> using Framework`
  - `Create discussion on <TOPIC> using Framework`
- Codex should choose the correct framework when possible.
- Codex should ask for clarification only when necessary.

Scale expectation:
- Around 20 to 100 presentations over time.

Assets:
- Markdown text
- Local images when needed

Metadata expectations for each presentation:
- `title`
- `category`
- `topic`
- `tags`

You may add a few more practical metadata fields if needed, but keep it simple.

PPTX expectation:
- Markdown and HTML are primary.
- Optional PPTX export scaffolding is good to have for future use.
- Do not optimize the whole system around PPTX.

Generation strictness:
- Each new presentation should always create a new folder.
- The site index should be updated automatically or at least predictably by Codex.
- Source references should be preserved.
- Old decks should not be edited unless explicitly requested.

Unknowns that you should solve pragmatically:
- Quiz format details
- Discussion format details
- Slide count defaults
- Naming standard
- Style/design system details
- Knowledge-base file list
- Operating model details
- Existing old deck import structure

Where details are missing, do not block on questions. Make reasonable, KISS-style defaults and document them clearly.

==================================================
WHAT YOU MUST PRODUCE
==================================================

Prepare a complete handoff package for Codex Cloud so that Codex can later:
- restructure the repo from a single-deck demo into a multi-presentation site
- maintain a knowledge base of source/framework files
- add future presentations in a repeatable way
- keep GitHub Pages and Marp compatibility

Your package must be suitable for import into this repo.

I want one deliverable ZIP with well-organized text files and content. The ZIP should include at least these groups:

1. Updated project information
- A strong repo-level explanation of what Kishor presentations are
- The mission of the repo
- The content categories
- The operating workflow between user, ChatGPT, and Codex
- The expected output conventions for future presentation creation

2. Project source/framework files
- A curated `sources/` structure
- Quiz framework documents
- Discussion framework documents
- Style system documents
- Naming/content conventions
- Any reusable authoring rubrics you think Codex should follow

3. Existing or legacy presentation materials
- All quiz-related presentations you can provide
- All discussion-related presentations you can provide
- Prefer normalized, Markdown-first forms
- Organize them so Codex can later import them into the repo structure

4. Collaboration/knowledge files
- Any additional documents that will help Codex work better in future
- Assumptions
- Decision notes
- Import notes
- Mapping of source files to likely future use

==================================================
REQUIRED OUTPUT STRUCTURE
==================================================

Create a package using a simple structure like this. You can improve names slightly if needed, but keep it close to this layout:

``
kishor-codex-handoff/
  README_HANDOFF.md
  PROJECT_INFORMATION_FOR_KISHOR_PRESENTATIONS.md
  CODEX_OPERATING_MODEL.md
  REPO_TARGET_STRUCTURE.md
  CONTENT_STANDARDS.md
  NAMING_CONVENTIONS.md
  PPTX_EXPORT_NOTES.md
  IMPORT_NOTES.md
  ASSUMPTIONS.md
  AGENTS_APPENDIX_FOR_CODEX.md
  INDEXING_RULES.md
  sources/
    quiz/
      Quiz_Framework_for_Kishor_Workflow_UPDATED.md
      ...
    discussion/
      Discussion_Framework_for_Kishor_Workflow.md
      ...
    style/
      Presentation_Style_System_Workflow.md
      Kishor_Presentation_Style_System_Workflow.md
      ...
    shared/
      glossary.md
      authoring-principles.md
      quality-checklist.md
      ...
  legacy-presentations/
    quiz/
      <presentation-slug>/
        slides.md
        meta.yml
        notes.md
        assets/
    discussion/
      <presentation-slug>/
        slides.md
        meta.yml
        notes.md
        assets/
  examples/
    quiz-sample/
      slides.md
      meta.yml
    discussion-sample/
      slides.md
      meta.yml
  manifests/
    source-manifest.md
    presentation-manifest.md
``

If you have a better structure, keep these principles:
- simple
- Markdown-first
- easy for Codex to import
- easy for humans to browse
- scalable to 20-100 presentations

==================================================
WHAT EACH FILE SHOULD CONTAIN
==================================================

Please include at least the following content.

1. `README_HANDOFF.md`
- Explain what is in the ZIP.
- Explain how Codex should use it.
- List the most important files first.

2. `PROJECT_INFORMATION_FOR_KISHOR_PRESENTATIONS.md`
- Explain the project mission.
- Explain the 2 categories: quiz and discussion.
- Explain intended audience if you can infer it.
- Explain the preferred Markdown-first workflow.
- Explain how GitHub Pages and Marp influence repo design.

3. `CODEX_OPERATING_MODEL.md`
- Describe how future Codex requests should be interpreted.
- Include example requests such as:
  - `Create quiz on AWS IAM basics using framework`
  - `Create discussion on incident review culture using framework`
- Define how Codex should choose frameworks.
- Define when Codex should ask clarifying questions.
- Define when Codex should refuse to edit old decks.

4. `REPO_TARGET_STRUCTURE.md`
- Propose a concrete repo layout that supports:
  - homepage/index
  - `quiz/<slug>/`
  - `discussion/<slug>/`
  - shared source/framework folders
  - local assets
  - metadata
- Keep this realistic for GitHub Pages.

5. `CONTENT_STANDARDS.md`
- Define quality rules for quiz decks.
- Define quality rules for discussion decks.
- Define tone and structure expectations.
- Define Markdown and Marp conventions.
- Define how to cite or reference source files.

6. `NAMING_CONVENTIONS.md`
- Recommend a folder naming scheme.
- Recommend a title style.
- Recommend how slugs should be formed.
- Recommend how dates should be recorded.
- Bias toward stable, simple names.

7. `PPTX_EXPORT_NOTES.md`
- Explain the optional future path to export PPTX from Marp or adjacent tooling.
- Keep it lightweight and secondary.
- Do not redesign the system around PPTX.

8. `IMPORT_NOTES.md`
- Explain how Codex should import legacy decks and source files into the repo.
- Explain what should be preserved and what can be normalized.

9. `ASSUMPTIONS.md`
- Explicitly list all assumptions you made.
- Keep them concise and reviewable.

10. `AGENTS_APPENDIX_FOR_CODEX.md`
- Provide content that Codex could later use to extend repo instructions.
- List important framework files and when to use them.
- Describe a minimal cross-reference map from category/topic to source documents.

11. `INDEXING_RULES.md`
- Explain what data the homepage should show for each presentation.
- Explain grouping by category.
- Explain sort order.
- Explain how descriptions should be written.

12. `sources/*`
- Provide all reusable source/framework docs in Markdown.
- Organize by category or purpose.
- Prefer practical authoring documents over vague guidance.

13. `legacy-presentations/*`
- Include as many old or prior quiz/discussion presentations as possible.
- Prefer one folder per presentation.
- Each presentation should ideally contain:
  - `slides.md`
  - `meta.yml`
  - `notes.md` if useful
  - `assets/` if needed

14. `examples/*`
- Provide one clean sample quiz deck and one clean sample discussion deck.
- Use Marp Markdown.
- Make them good enough that Codex could copy them as templates.

15. `manifests/*`
- Provide a concise manifest of source files and imported presentations.
- This should help Codex and the repo maintainer understand what came from where.

==================================================
TECHNICAL AND WRITING RULES
==================================================

Please follow these rules when preparing the package.

1. Markdown-first
- Prefer `.md` files for almost everything.
- Use YAML only where a small metadata file makes sense.

2. Marp-aware
- Any example decks or imported decks should be compatible with Marp.
- Use front matter where useful, for example:
  - `marp: true`
  - `theme`
  - `paginate`
- Keep examples realistic.

3. GitHub Pages aware
- Assume the repo will be hosted on GitHub Pages.
- Assume a homepage/index page must link to individual presentation folders.
- Assume local relative links matter.

4. KISS
- Keep naming simple.
- Keep file structures understandable.
- Avoid overengineering.

5. Preserve source intent
- If a source file contains methodology, structure, tone, or style rules, preserve that clearly.
- Do not dilute framework meaning into vague summaries.

6. Be explicit about provenance
- If you are converting or normalizing older materials, say so.
- If you infer something, label it as an assumption.

7. Minimize future token waste
- Organize files so Codex can find the right framework quickly.
- Reduce repetitive explanation.
- Favor concise but high-signal docs.

8. Keep future automation easy
- Make the structure predictable.
- Make it easy for a coding agent to add new folders and update an index.

==================================================
IMPORTANT DECISIONS YOU SHOULD MAKE IF MISSING
==================================================

If the user did not specify a detail, choose a sensible default and document it. In particular, choose:
- a good folder naming convention
- a reasonable metadata schema
- a default quiz deck shape
- a default discussion deck shape
- a practical slide-count guideline
- a sensible theme/style starting point
- a good way to organize reusable source files
- a good way to represent imported legacy decks

Bias toward:
- practical reuse
- low maintenance
- long-term clarity

==================================================
FORMAT OF YOUR RESPONSE
==================================================

Please respond in this order:

1. A short executive summary of what you are delivering
2. The proposed ZIP file name
3. The full file tree
4. The contents of each text file
5. Any notes about assumptions or limitations

If you can generate an actual ZIP/file bundle, do that.
If you cannot, provide all file contents inline in a way that can be saved directly.

==================================================
EXTRA CONTEXT FOR YOU
==================================================

This request is meant to help a future Codex Cloud agent work more effectively inside the repo. Your package should not be generic. It should be tailored to:
- GitHub Pages hosting
- Marp Markdown presentations
- quiz/discussion category split
- reusable framework/source files
- future import of many old decks
- Markdown-first publishing
- optional future PPTX export

You are not being asked to write application code right now. You are being asked to prepare the best possible structured knowledge and content package so a coding agent can build the repo correctly with less back-and-forth and fewer tokens.

Deliver a package that is operational, not theoretical.
```
