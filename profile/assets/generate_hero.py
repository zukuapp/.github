"""Render the Trecillo developer banner from the pinned logo and Pretendard.

Requires fonttools and librsvg (rsvg-convert). Font outlines are written to
SVG so the banner does not depend on fonts installed on a visitor's device.
"""

from __future__ import annotations

import base64
import subprocess
import urllib.request
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


HERE = Path(__file__).resolve().parent
FONT_BASE = (
    "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/"
    "packages/pretendard/dist/web/static/woff2"
)
INTER_BOLD_URL = (
    "https://raw.githubusercontent.com/rsms/inter/v4.1/"
    "docs/font-files/Inter-Bold.woff2"
)


def load_font(weight: str) -> TTFont:
    path = Path("/tmp") / f"Pretendard-{weight}-1.3.9.woff2"
    if not path.exists():
        urllib.request.urlretrieve(
            f"{FONT_BASE}/Pretendard-{weight}.woff2", path
        )
    return TTFont(path)


def load_inter() -> TTFont:
    path = Path("/tmp/Inter-Bold-v4.1.woff2")
    if not path.exists():
        urllib.request.urlretrieve(INTER_BOLD_URL, path)
    return TTFont(path)


def outlined_text(
    font: TTFont,
    value: str,
    x: float,
    y: float,
    size: float,
    color: str,
    tracking: float = 0,
) -> str:
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    metrics = font["hmtx"].metrics
    scale = size / font["head"].unitsPerEm
    paths = []
    cursor = x
    for char in value:
        glyph_name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[glyph_name].draw(pen)
        if path := pen.getCommands():
            paths.append(
                f'<path d="{path}" '
                f'transform="translate({cursor:.2f} {y:.2f}) '
                f'scale({scale:.8f} {-scale:.8f})" fill="{color}"/>'
            )
        cursor += metrics[glyph_name][0] * scale + tracking
    return "\n".join(paths)


def main() -> None:
    bold, medium, inter = load_font("Bold"), load_font("Medium"), load_inter()
    logo = base64.b64encode(
        (HERE / "brand/trecillo-game-ci-20260919.png").read_bytes()
    ).decode("ascii")
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" width="1600" '
        'height="420" viewBox="0 0 1600 420" role="img" '
        'aria-labelledby="title desc">',
        '<title id="title">Trecillo · ZUKU 개발자 문서</title>',
        '<desc id="desc">현행 Trecillo 로고와 공개 개발 문서 안내</desc>',
        '<rect width="1600" height="420" fill="#0B0C10"/>',
        '<rect x="48" y="43" width="1504" height="334" rx="22" '
        'fill="none" stroke="#31333A" stroke-width="2"/>',
        f'<image x="72" y="81" width="338" height="233" '
        f'xlink:href="data:image/png;base64,{logo}"/>',
        '<rect x="474" y="80" width="4" height="260" rx="2" '
        'fill="#FF2D7A"/>',
        '<circle cx="526" cy="91" r="6" fill="#FF2D7A"/>',
        outlined_text(
            inter, "TRECILLO  /  DEVELOPERS", 550, 98, 25, "#FF4D8D", 1.8
        ),
        outlined_text(
            bold, "ZUKU 개발자 문서", 520, 209, 78, "#FFFFFF", -0.8
        ),
        outlined_text(
            medium, "공개 명세에서 첫 실행까지", 526, 278, 37, "#CFD1D8", -0.3
        ),
        '<line x1="526" y1="321" x2="1504" y2="321" '
        'stroke="#31333A" stroke-width="2"/>',
        outlined_text(inter, "ENGINE", 528, 358, 23, "#FF4D8D", 1.5),
        outlined_text(inter, "FORMAT", 760, 358, 23, "#FF4D8D", 1.5),
        outlined_text(inter, "API", 995, 358, 23, "#FF4D8D", 1.5),
        outlined_text(inter, "CONTRIBUTE", 1165, 358, 23, "#FF4D8D", 1.5),
        "</svg>",
    ]
    svg = HERE / "developer-hero.svg"
    svg.write_text("\n".join(parts) + "\n", encoding="utf-8")
    subprocess.run(
        [
            "rsvg-convert",
            "-w",
            "1600",
            "-h",
            "420",
            str(svg),
            "-o",
            str(HERE / "developer-hero.png"),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
