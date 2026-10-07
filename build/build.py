# -*- coding: utf-8 -*-
"""Assembles static pages from partials.py + content/*.html fragments.
Run from the project root: python3 build/build.py
Writes <slug>/index.html for each entry in pages.py (slug "" -> ./index.html).
Never hand-edit the generated index.html files directly - edit content/*.html
or partials.py and re-run this script instead."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from partials import HEAD, HEADER, FOOTER, SCHEMA_JSON, SITE_URL, NOINDEX  # noqa: E402
from pages import PAGES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT_DIR = os.path.join(ROOT, "content")


def build_page(page):
    slug = page["slug"].strip("/")
    canonical = f"{SITE_URL}/{slug}/" if slug else f"{SITE_URL}/"

    content_path = os.path.join(CONTENT_DIR, page["content"])
    with open(content_path, "r", encoding="utf-8") as f:
        body = f.read()

    head = (
        HEAD.replace("__TITLE__", page["title"])
        .replace("__DESCRIPTION__", page["description"])
        .replace("__CANONICAL__", canonical)
        .replace("__ROBOTS__", '<meta name="robots" content="noindex, nofollow">\n' if NOINDEX else "")
        .replace("__SCHEMA_JSON__", SCHEMA_JSON.replace("__SITE_URL__", SITE_URL))
    )

    html = head + HEADER + body + FOOTER

    out_dir = os.path.join(ROOT, slug) if slug else ROOT
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {os.path.relpath(out_path, ROOT)}")


def build_sitemap():
    urls = []
    for page in PAGES:
        if page.get("sitemap") is False:
            continue
        slug = page["slug"].strip("/")
        urls.append(f"{SITE_URL}/{slug}/" if slug else f"{SITE_URL}/")

    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n"
    )
    out_path = os.path.join(ROOT, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml")


def build_robots():
    content = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    out_path = os.path.join(ROOT, "robots.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote robots.txt")


def main():
    for page in PAGES:
        build_page(page)
    build_sitemap()
    build_robots()


if __name__ == "__main__":
    main()
