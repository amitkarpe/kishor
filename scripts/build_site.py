#!/usr/bin/env python3

from __future__ import annotations

import html
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
CATEGORIES = ("quiz", "discussion")
REQUIRED_KEYS = ("title", "category", "topic", "slug", "date", "description", "tags")


@dataclass
class Deck:
    title: str
    category: str
    topic: str
    slug: str
    date: str
    description: str
    tags: list[str]
    status: str
    path: Path

    @property
    def repo_path(self) -> str:
        return f"{self.category}/{self.slug}/"

    @property
    def output_path(self) -> Path:
        return DIST / self.category / self.slug / "index.html"


def parse_simple_yaml(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- "):
            if current_key is None:
                raise ValueError(f"List item without key in {path}")
            data.setdefault(current_key, [])
            assert isinstance(data[current_key], list)
            data[current_key].append(stripped[2:].strip())
            continue

        if ":" not in line:
            raise ValueError(f"Unsupported metadata line in {path}: {line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            data[key] = []
            current_key = key
            continue

        data[key] = value.strip("\"'")
        current_key = None

    return data


def load_decks() -> list[Deck]:
    decks: list[Deck] = []

    for category in CATEGORIES:
        for meta_path in sorted((ROOT / category).glob("*/meta.yml")):
            data = parse_simple_yaml(meta_path)
            missing = [key for key in REQUIRED_KEYS if key not in data]
            if missing:
                raise ValueError(f"Missing metadata keys in {meta_path}: {', '.join(missing)}")

            tags = data["tags"]
            if not isinstance(tags, list):
                raise ValueError(f"`tags` must be a list in {meta_path}")

            deck = Deck(
                title=str(data["title"]),
                category=str(data["category"]),
                topic=str(data["topic"]),
                slug=str(data["slug"]),
                date=str(data["date"]),
                description=str(data["description"]),
                tags=[str(tag) for tag in tags],
                status=str(data.get("status", "published")),
                path=meta_path.parent,
            )

            if deck.category != category:
                raise ValueError(f"Category mismatch in {meta_path}: expected {category}, got {deck.category}")

            decks.append(deck)

    return sorted(
        decks,
        key=lambda deck: (
            deck.category,
            datetime.strptime(deck.date, "%Y-%m-%d"),
            deck.title.lower(),
        ),
        reverse=True,
    )


def build_deck(deck: Deck) -> None:
    slides_path = deck.path / "slides.md"
    if not slides_path.exists():
        raise FileNotFoundError(f"Missing slides.md for {deck.repo_path}")

    deck.output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "npx",
            "--yes",
            "@marp-team/marp-cli",
            str(slides_path),
            "--html",
            "-o",
            str(deck.output_path),
        ],
        cwd=ROOT,
        check=True,
    )

    inject_home_link(deck.output_path)

    assets_dir = deck.path / "assets"
    if assets_dir.is_dir():
        shutil.copytree(assets_dir, deck.output_path.parent / "assets", dirs_exist_ok=True)


def inject_home_link(output_path: Path) -> None:
    html_text = output_path.read_text(encoding="utf-8")
    home_link = """
<style>
.kishor-home-link{
  position:fixed;
  top:16px;
  left:16px;
  z-index:9999;
  padding:10px 14px;
  border-radius:999px;
  background:rgba(24,22,20,.82);
  color:#fff;
  text-decoration:none;
  font:600 14px/1.2 Georgia, "Times New Roman", serif;
  box-shadow:0 10px 30px rgba(0,0,0,.18);
}
.kishor-home-link:hover{opacity:.92}
</style>
<a class="kishor-home-link" href="../../">Back to index</a>
</body>
""".strip()
    output_path.write_text(html_text.replace("</body>", home_link), encoding="utf-8")


def render_homepage(decks: list[Deck]) -> str:
    grouped = {category: [] for category in CATEGORIES}
    for deck in decks:
        grouped[deck.category].append(deck)

    sections: list[str] = []
    for category in CATEGORIES:
        items = []
        for deck in grouped[category]:
            tags = " ".join(
                f'<span class="tag">{html.escape(tag)}</span>' for tag in deck.tags
            )
            items.append(
                f"""
                <article class="card">
                  <div class="meta-row">
                    <span class="pill">{html.escape(deck.category.title())}</span>
                    <time datetime="{html.escape(deck.date)}">{html.escape(deck.date)}</time>
                  </div>
                  <h3><a href="{html.escape(deck.repo_path)}">{html.escape(deck.title)}</a></h3>
                  <p>{html.escape(deck.description)}</p>
                  <div class="tags">{tags}</div>
                </article>
                """.strip()
            )

        section_title = "Quiz Presentations" if category == "quiz" else "Discussion Presentations"
        sections.append(
            f"""
            <section>
              <div class="section-head">
                <h2>{html.escape(section_title)}</h2>
                <p>{len(grouped[category])} deck(s)</p>
              </div>
              <div class="card-grid">
                {''.join(items) if items else '<p class="empty">No decks published yet.</p>'}
              </div>
            </section>
            """.strip()
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kishor Presentations</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f5efe6;
      --paper: #fffaf2;
      --ink: #1f1a17;
      --muted: #6f6258;
      --line: #d9c8b8;
      --accent: #9d4f1f;
      --accent-soft: #f0d3bb;
      --quiz: #1f6f5b;
      --discussion: #7a2e59;
      --shadow: 0 20px 45px rgba(77, 48, 26, 0.12);
      font-family: Georgia, "Times New Roman", serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top right, rgba(157, 79, 31, 0.10), transparent 24rem),
        linear-gradient(180deg, #f7f1e8 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 3rem 1.25rem 4rem;
    }}
    header {{
      background: rgba(255, 250, 242, 0.88);
      border: 1px solid var(--line);
      border-radius: 24px;
      padding: 2rem;
      box-shadow: var(--shadow);
      backdrop-filter: blur(8px);
    }}
    h1, h2, h3 {{ margin: 0; }}
    h1 {{
      font-size: clamp(2.4rem, 5vw, 4rem);
      line-height: 0.95;
      letter-spacing: -0.04em;
    }}
    .lede {{
      max-width: 58rem;
      margin-top: 1rem;
      color: var(--muted);
      font-size: 1.05rem;
      line-height: 1.65;
    }}
    .summary {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}
    .summary-card {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 1rem 1.1rem;
    }}
    .summary-card strong {{
      display: block;
      font-size: 1.8rem;
      color: var(--accent);
    }}
    section {{
      margin-top: 2.5rem;
    }}
    .section-head {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .section-head p {{
      margin: 0;
      color: var(--muted);
    }}
    .card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
    }}
    .card {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 1.1rem;
      box-shadow: var(--shadow);
      min-height: 220px;
    }}
    .meta-row {{
      display: flex;
      justify-content: space-between;
      gap: 0.75rem;
      align-items: center;
      color: var(--muted);
      font-size: 0.92rem;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 0.2rem 0.6rem;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      color: white;
      background: var(--accent);
    }}
    section:nth-of-type(1) .pill {{ background: var(--quiz); }}
    section:nth-of-type(2) .pill {{ background: var(--discussion); }}
    .card h3 {{
      margin-top: 1rem;
      font-size: 1.35rem;
      line-height: 1.15;
    }}
    .card a {{
      color: inherit;
      text-decoration: none;
      border-bottom: 2px solid transparent;
    }}
    .card a:hover {{
      color: var(--accent);
      border-color: currentColor;
    }}
    .card p {{
      margin-top: 0.8rem;
      color: var(--muted);
      line-height: 1.55;
    }}
    .tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-top: 1rem;
    }}
    .tag {{
      padding: 0.2rem 0.55rem;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--ink);
      font-size: 0.82rem;
    }}
    .empty {{
      color: var(--muted);
      margin: 0;
    }}
    footer {{
      margin-top: 3rem;
      color: var(--muted);
      font-size: 0.95rem;
    }}
    code {{
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 0.92em;
    }}
    @media (max-width: 700px) {{
      main {{ padding: 1.25rem 0.9rem 3rem; }}
      header {{ padding: 1.3rem; border-radius: 18px; }}
      .section-head {{ flex-direction: column; align-items: flex-start; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Kishor Presentations</h1>
      <p class="lede">
        A Markdown-first Marp presentation library for recurring Kishor quiz and discussion sessions.
        Each deck lives in its own folder, is rendered through GitHub Pages, and links back here for browsing.
      </p>
      <div class="summary">
        <div class="summary-card">
          <strong>{len(decks)}</strong>
          Total published decks
        </div>
        <div class="summary-card">
          <strong>{len(grouped["quiz"])}</strong>
          Quiz decks
        </div>
        <div class="summary-card">
          <strong>{len(grouped["discussion"])}</strong>
          Discussion decks
        </div>
      </div>
    </header>
    {''.join(sections)}
    <footer>
      Built from repo metadata in <code>quiz/*/meta.yml</code> and <code>discussion/*/meta.yml</code>.
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    decks = load_decks()
    for deck in decks:
        build_deck(deck)

    (DIST / ".nojekyll").touch()
    (DIST / "index.html").write_text(render_homepage(decks), encoding="utf-8")


if __name__ == "__main__":
    main()
