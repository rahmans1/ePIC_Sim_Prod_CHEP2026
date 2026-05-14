#!/usr/bin/env python3
"""Embed local image assets in a Marp HTML export as data URLs."""

from __future__ import annotations

import argparse
import base64
import mimetypes
import re
from pathlib import Path


TWEMOJI_WARNING_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36">'
    '<path fill="#ffcc4d" d="M2.653 32.665 17.118 3.731c.489-.978 1.275-.978 1.764 0l14.465 28.934c.489.978-.006 1.778-1.1 1.778H3.753c-1.094 0-1.589-.8-1.1-1.778z"/>'
    '<path fill="#231f20" d="M15.583 12.102c0-1.333 1.085-2.417 2.417-2.417s2.417 1.084 2.417 2.417v9.666c0 1.333-1.085 2.417-2.417 2.417s-2.417-1.084-2.417-2.417v-9.666zM20.75 28.5c0 1.519-1.231 2.75-2.75 2.75s-2.75-1.231-2.75-2.75 1.231-2.75 2.75-2.75 2.75 1.231 2.75 2.75z"/>'
    "</svg>"
)


def data_url(path: Path) -> str:
    media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{media_type};base64,{encoded}"


def svg_data_url(svg: str) -> str:
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="HTML file to read")
    parser.add_argument("output", type=Path, help="HTML file to write")
    args = parser.parse_args()

    html_path = args.input.resolve()
    html_root = html_path.parent
    project_root = Path.cwd().resolve()
    html = html_path.read_text(encoding="utf-8")
    embedded: set[str] = set()

    def replace_src(match: re.Match[str]) -> str:
        prefix, url, suffix = match.groups()
        if url.startswith(("data:", "http://", "https://", "#")):
            return match.group(0)
        candidates = [(html_root / url).resolve(), (project_root / url).resolve()]
        asset_path = next((path for path in candidates if path.is_file()), None)
        if asset_path is None:
            return match.group(0)
        if not any(_is_relative_to(asset_path, root) for root in (html_root, project_root)):
            return match.group(0)
        if not asset_path.is_file():
            return match.group(0)
        embedded.add(url)
        return f"{prefix}{data_url(asset_path)}{suffix}"

    html = re.sub(r'((?:src|href)=["\'])([^"\']+)(["\'])', replace_src, html)
    html = html.replace(
        "https://cdn.jsdelivr.net/gh/jdecked/twemoji@17.0.2/assets/svg/26a0.svg",
        svg_data_url(TWEMOJI_WARNING_SVG),
    )

    args.output.write_text(html, encoding="utf-8")
    print(f"Embedded {len(embedded)} local asset reference(s) into {args.output}")


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
