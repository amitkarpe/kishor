# Legacy Import Area

This folder stores staging inputs for older presentation material that has not yet been normalized into the published repo structure.

Use this area for:
- raw import notes
- metadata stubs
- references to external PPTX bundles

Do not treat files here as canonical published decks.

When promoting a legacy deck into the live site:
1. create a fresh folder under `quiz/<slug>/` or `discussion/<slug>/`
2. rewrite or normalize content into Marp Markdown
3. create `meta.yml`, `slides.md`, and `notes.md`
4. build the site and verify the new homepage entry
