# kishor

Minimal Marp demo presentation with exactly 2 slides.

## Files
- `slides.md`: Marp source deck.
- `.github/workflows/static.yml`: Builds slides and deploys to GitHub Pages.

## Run locally
Option A (no install, with Docker):
```bash
docker run --rm -v "$PWD":/work -w /work marpteam/marp-cli slides.md --html -o dist/index.html
```

Option B (Node installed):
```bash
npx @marp-team/marp-cli slides.md --html -o dist/index.html
```

Then open `dist/index.html` in your browser.

## GitHub Pages (important)
To use this workflow deployment, set:
- **Settings → Pages → Build and deployment → Source: GitHub Actions**

The workflow deploys on push (any branch) and manual dispatch, so you can publish ASAP from your current branch without merging.
