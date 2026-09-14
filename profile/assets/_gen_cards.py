# -*- coding: utf-8 -*-
"""One-shot generator for ZUKU org-profile SVG chips. Not shipped as a product tool.

Hero artwork lives in hero-dark.svg / hero-light.svg and must keep official
Trecillo vectors + ZUKU lockups + the 2026 teapot. Do not restore a geometric Z.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent
FONT = "ui-sans-serif, system-ui, Apple SD Gothic Neo, Malgun Gothic, sans-serif"

ICONS = {
    "thread": """
      <line x1="24" y1="30" x2="24" y2="52" stroke="{c}" stroke-width="2" stroke-linecap="round"/>
      <circle cx="24" cy="24" r="3.6" fill="{c}"/>
      <circle cx="24" cy="38" r="2.4" fill="{c}" opacity="0.7"/>
      <circle cx="24" cy="50" r="1.8" fill="{c}" opacity="0.4"/>
    """,
    "hype": """
      <rect x="14" y="28" width="28" height="18" rx="3.5" fill="none" stroke="{c}" stroke-width="2"/>
      <circle cx="20" cy="34" r="1.8" fill="{c}"/>
      <path d="M14 42.5 L22 36 L30 41 L42 32" fill="none" stroke="{c}" stroke-width="1.6" stroke-linejoin="round"/>
    """,
    "swipe": """
      <rect x="20" y="22" width="16" height="28" rx="3.5" fill="none" stroke="{c}" stroke-width="2"/>
      <line x1="24" y1="46" x2="32" y2="46" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>
    """,
    "jump": """
      <path d="M18 44 L28 28 L38 44" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M18 52 L28 36 L38 52" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.4"/>
    """,
    "vive": """
      <line x1="16" y1="28" x2="40" y2="28" stroke="{c}" stroke-width="2" stroke-linecap="round"/>
      <line x1="16" y1="36" x2="36" y2="36" stroke="{c}" stroke-width="2" stroke-linecap="round"/>
      <line x1="16" y1="44" x2="30" y2="44" stroke="{c}" stroke-width="2" stroke-linecap="round"/>
    """,
    "vine": """
      <rect x="15" y="36" width="3.2" height="10" rx="1.2" fill="{c}" opacity="0.45"/>
      <rect x="21" y="28" width="3.2" height="18" rx="1.2" fill="{c}"/>
      <rect x="27" y="24" width="3.2" height="22" rx="1.2" fill="{c}" opacity="0.8"/>
      <rect x="33" y="30" width="3.2" height="16" rx="1.2" fill="{c}"/>
      <rect x="39" y="34" width="3.2" height="12" rx="1.2" fill="{c}" opacity="0.55"/>
    """,
    "aist": """
      <circle cx="20" cy="30" r="3.2" fill="{c}"/>
      <circle cx="38" cy="28" r="3.2" fill="{c}" opacity="0.85"/>
      <circle cx="30" cy="46" r="3.2" fill="{c}" opacity="0.7"/>
      <line x1="22.8" y1="32" x2="35.2" y2="29.4" stroke="{c}" stroke-width="1.4"/>
      <line x1="21.6" y1="33.2" x2="28.2" y2="43.4" stroke="{c}" stroke-width="1.4"/>
      <line x1="37" y1="31" x2="32.2" y2="43.2" stroke="{c}" stroke-width="1.4"/>
    """,
}

CARDS = [
    ("thread", "THREAD", "이야기", "홈 · 커뮤니티", "www.zuzunza.com", "#5CE1E6"),
    ("hype", "HYPE", "창작", "영상 · 사진 · 인터랙티브", "hype.zuzunza.com", "#00D4FF"),
    ("swipe", "SWIPE", "넘김", "세로 숏폼", "swipe.zuzunza.com", "#FF2D78"),
    ("jump", "JUMP", "플레이", "브라우저 게임", "jump.zuzunza.com", "#00FF88"),
    ("vive", "VIVE", "문학", "글 · 연재", "vive.zuzunza.com", "#E8C547"),
    ("vine", "VINE", "사운드", "음악 · 보이스", "vine.zuzunza.com", "#A78BFA"),
    ("aist", "AIST", "생성", "AI 게임 스튜디오", "aist.zuzunza.com", "#4DB8B4"),
]

CARD_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 188 168" width="188" height="168" role="img" aria-label="{label}">
  <defs>
    <clipPath id="card">
      <rect width="188" height="168" rx="16"/>
    </clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="188" height="168" rx="16" fill="#12121A"/>
    <rect width="188" height="3" fill="{c}"/>
  </g>
  <rect width="188" height="168" rx="16" fill="none" stroke="#2A2A4A"/>
  <g transform="translate(8, 8)">{icon}</g>
  <text x="20" y="78" fill="{c}" font-size="10" font-weight="700" letter-spacing="0.18em" font-family="{font}">{name}</text>
  <text x="20" y="108" fill="#FFFFFF" font-size="22" font-weight="700" font-family="{font}">{verb}</text>
  <text x="20" y="130" fill="#A0A0B8" font-size="12" font-family="{font}">{blurb}</text>
  <text x="20" y="152" fill="#6A6A80" font-size="11" font-family="{font}">{host}  →</text>
</svg>
"""

CHIPS = [
    ("engine", "zuku-engine-next2d", "Jump 엔진", "#00FF88"),
    ("cli", "zuku-cli", "게임 패키지 도구", "#5CE1E6"),
    ("api", "zuku-api", "Jump 공개 API", "#00D4FF"),
    ("zukbox", "zukbox", "브라우저 저작 도구", "#A78BFA"),
    ("player", "zukbox-player", "게임 플레이어", "#FF2D78"),
    ("runtime", "zukbox-runtime", "Jump 실행 코어", "#4DB8B4"),
    ("home", "shizuku", "공개 홈", "#E8C547"),
    ("site", "zukuapp.github.io", "Trecillo × ZUKU", "#5CE1E6"),
]

CHIP_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 56" width="280" height="56" role="img" aria-label="{name}">
  <rect width="280" height="56" rx="12" fill="#12121A" stroke="#2A2A4A"/>
  <rect x="0" y="12" width="3" height="32" rx="1.5" fill="{c}"/>
  <text x="18" y="24" fill="#FFFFFF" font-size="13" font-weight="700" font-family="{font}">{name}</text>
  <text x="18" y="42" fill="#A0A0B8" font-size="11" font-family="{font}">{blurb}</text>
</svg>
"""

CTAS = [
    ("cta-play", "Play on zuzunza.com", "#5CE1E6", "#0A0A0F", "#5CE1E6"),
    ("cta-org", "github.com/zukuapp", "#12121A", "#5CE1E6", "#5CE1E6"),
    ("cta-site", "Company site", "#12121A", "#5CE1E6", "#5CE1E6"),
    ("cta-mail", "contact@crevision.kr", "#12121A", "#5CE1E6", "#5CE1E6"),
]

CTA_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 40" width="{w}" height="40" role="img" aria-label="{label}">
  <rect width="{w}" height="40" rx="20" fill="{bg}" stroke="{stroke}"/>
  <text x="{cx}" y="26" text-anchor="middle" fill="{fg}" font-size="13" font-weight="700" font-family="{font}">{label}</text>
</svg>
"""


def main() -> None:
    for key, name, verb, blurb, host, color in CARDS:
        svg = CARD_TMPL.format(
            label=f"{name} — {verb}",
            c=color,
            icon=ICONS[key].format(c=color),
            name=name,
            verb=verb,
            blurb=blurb,
            host=host,
            font=FONT,
        )
        (OUT / f"card-{key}.svg").write_text(svg.strip() + "\n", encoding="utf-8")

    for key, name, blurb, color in CHIPS:
        svg = CHIP_TMPL.format(name=name, blurb=blurb, c=color, font=FONT)
        (OUT / f"chip-{key}.svg").write_text(svg.strip() + "\n", encoding="utf-8")

    for key, label, bg, fg, stroke in CTAS:
        w = 240 if key == "cta-mail" else 220
        svg = CTA_TMPL.format(label=label, bg=bg, fg=fg, stroke=stroke, font=FONT, w=w, cx=w // 2)
        (OUT / f"{key}.svg").write_text(svg.strip() + "\n", encoding="utf-8")

    print("wrote cards, chips, ctas (heroes are hand-authored)")


if __name__ == "__main__":
    main()
