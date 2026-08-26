# -*- coding: utf-8 -*-
"""One-shot generator for ZUKU org-profile SVG chips. Not shipped as a product tool."""
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
    ("thread", "THREAD", "이야기", "SNS · 포럼 홈", "www.zuzunza.com", "#5CE1E6"),
    ("hype", "HYPE", "창작", "롱폼 · 사진 · 인터랙티브", "hype.zuzunza.com", "#00D4FF"),
    ("swipe", "SWIPE", "넘김", "세로 숏폼", "swipe.zuzunza.com", "#FF2D78"),
    ("jump", "JUMP", "플레이", "WASM · HTML5 게임", "jump.zuzunza.com", "#00FF88"),
    ("vive", "VIVE", "문학", "글 · 필문 · 연재", "vive.zuzunza.com", "#E8C547"),
    ("vine", "VINE", "사운드", "음악 · 보이스 · UTAU", "vine.zuzunza.com", "#A78BFA"),
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
    ("engine", "zuku-engine-next2d", "Jump 엔진 · 패키지 계약", "#00FF88"),
    ("cli", "zuku-cli", "검증 · 패키징 CLI", "#5CE1E6"),
    ("api", "zuku-api", "Jump API OpenAPI 3.1", "#00D4FF"),
    ("zukbox", "zukbox", "브라우저 저작 툴", "#A78BFA"),
    ("player", "zukbox-player", "WebGL / WebGPU 플레이어", "#FF2D78"),
    ("runtime", "zukbox-runtime", "ZWF WASM 런타임", "#4DB8B4"),
    ("home", "shizuku", "공개 홈 · 인덱스", "#E8C547"),
    ("site", "zukuapp.github.io", "Tresillo × ZUKU 사이트", "#5CE1E6"),
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
    ("cta-mail", "contact@zuzunza.com", "#12121A", "#5CE1E6", "#5CE1E6"),
]

CTA_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 40" width="220" height="40" role="img" aria-label="{label}">
  <rect width="220" height="40" rx="20" fill="{bg}" stroke="{stroke}"/>
  <text x="110" y="26" text-anchor="middle" fill="{fg}" font-size="13" font-weight="700" font-family="{font}">{label}</text>
</svg>
"""


HERO_DARK = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 280" width="960" height="280" role="img" aria-labelledby="title desc">
  <title id="title">ZUKU - Create what moves next.</title>
  <desc id="desc">Tresillo interactive UGC media platform. The Z mark starts a ripple.</desc>
  <defs>
    <linearGradient id="cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5CE1E6"/>
      <stop offset="100%" stop-color="#00D4FF"/>
    </linearGradient>
    <radialGradient id="glow" cx="81%" cy="36%" r="42%">
      <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.22"/>
      <stop offset="55%" stop-color="#0A0A0F" stop-opacity="0"/>
    </radialGradient>
    <style>
      .ring { transform-box: fill-box; transform-origin: center; animation: ripple 3.8s ease-out infinite; }
      .ring2 { animation-delay: 1.25s; }
      .ring3 { animation-delay: 2.5s; }
      @keyframes ripple {
        0% { transform: scale(0.28); opacity: 0.55; }
        70% { opacity: 0.12; }
        100% { transform: scale(2.05); opacity: 0; }
      }
      @media (prefers-reduced-motion: reduce) {
        .ring, .ring2, .ring3 { animation: none; opacity: 0.2; transform: scale(1); }
      }
    </style>
  </defs>
  <rect width="960" height="280" fill="#0A0A0F"/>
  <rect width="960" height="280" fill="url(#glow)"/>
  <line x1="0" y1="279.5" x2="960" y2="279.5" stroke="#5CE1E6" stroke-opacity="0.18"/>
  <g aria-hidden="true">
    <circle class="ring" cx="792" cy="96" r="52" fill="none" stroke="#5CE1E6" stroke-width="1.15"/>
    <circle class="ring ring2" cx="792" cy="96" r="52" fill="none" stroke="#00D4FF" stroke-width="1.15"/>
    <circle class="ring ring3" cx="792" cy="96" r="52" fill="none" stroke="#5CE1E6" stroke-width="1.15"/>
    <circle cx="792" cy="96" r="38" fill="none" stroke="#5CE1E6" stroke-opacity="0.22" stroke-width="1"/>
    <g transform="translate(768, 72) scale(1.5)">
      <rect x="1.75" y="1.75" width="28.5" height="28.5" rx="7.5" fill="none" stroke="url(#cyan)" stroke-width="2.5"/>
      <path fill="url(#cyan)" d="M8.25 8h15.5v3.15L13.05 20.85h10.7v3.15H8.25v-3.15L18.95 11.15H8.25V8z"/>
    </g>
  </g>
  <text x="56" y="64" fill="#5CE1E6" fill-opacity="0.9" font-family="ui-sans-serif, system-ui, Segoe UI, sans-serif" font-size="11" font-weight="600" letter-spacing="0.28em">TRESILLO PRESENTS</text>
  <g transform="translate(56, 86)" fill="url(#cyan)" aria-hidden="true">
    <path d="M0 0h20.5v4.6L7.55 25.1H20.5V29.7H0v-4.6L12.95 4.6H0V0z"/>
    <path d="M27.5 0h4.7v19.4c0 2.85 1.5 4.3 4.2 4.3s4.2-1.45 4.2-4.3V0h4.7v19.7c0 5.5-3.35 10-8.9 10s-8.9-4.5-8.9-10V0z"/>
    <path d="M52.9 0h4.7v11.9L67.6 0h5.8L63.2 13.2 74 29.7h-5.9L57.6 15.4v14.3h-4.7V0z"/>
    <path d="M77.7 0h4.7v19.4c0 2.85 1.5 4.3 4.2 4.3s4.2-1.45 4.2-4.3V0h4.7v19.7c0 5.5-3.35 10-8.9 10s-8.9-4.5-8.9-10V0z"/>
  </g>
  <text x="56" y="142" fill="#FFFFFF" font-family="ui-sans-serif, system-ui, Segoe UI, sans-serif" font-size="28" font-weight="700">Create what moves next.</text>
  <text x="56" y="176" fill="#A0A0B8" font-family="ui-sans-serif, system-ui, Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="15">보고, 넘기고, 직접 뛰어드세요. 창작과 플레이가 한 흐름입니다.</text>
  <g font-family="ui-sans-serif, system-ui, Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="12" font-weight="600">
    <rect x="56" y="204" width="72" height="28" rx="14" fill="none" stroke="#5CE1E6" stroke-opacity="0.45"/>
    <text x="92" y="222" text-anchor="middle" fill="#5CE1E6">플레이</text>
    <rect x="136" y="204" width="72" height="28" rx="14" fill="none" stroke="#5CE1E6" stroke-opacity="0.45"/>
    <text x="172" y="222" text-anchor="middle" fill="#5CE1E6">창작</text>
    <rect x="216" y="204" width="88" height="28" rx="14" fill="none" stroke="#5CE1E6" stroke-opacity="0.45"/>
    <text x="260" y="222" text-anchor="middle" fill="#5CE1E6">오픈소스</text>
  </g>
</svg>
'''

HERO_LIGHT = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 280" width="960" height="280" role="img" aria-labelledby="title desc">
  <title id="title">ZUKU - Create what moves next.</title>
  <desc id="desc">Tresillo interactive UGC media platform. The Z mark starts a ripple.</desc>
  <defs>
    <linearGradient id="cyanL" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0097A7"/>
      <stop offset="100%" stop-color="#006064"/>
    </linearGradient>
    <radialGradient id="glowL" cx="81%" cy="36%" r="42%">
      <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.16"/>
      <stop offset="55%" stop-color="#F4F6FA" stop-opacity="0"/>
    </radialGradient>
    <style>
      .ring { transform-box: fill-box; transform-origin: center; animation: ripple 3.8s ease-out infinite; }
      .ring2 { animation-delay: 1.25s; }
      .ring3 { animation-delay: 2.5s; }
      @keyframes ripple {
        0% { transform: scale(0.28); opacity: 0.5; }
        70% { opacity: 0.1; }
        100% { transform: scale(2.05); opacity: 0; }
      }
      @media (prefers-reduced-motion: reduce) {
        .ring, .ring2, .ring3 { animation: none; opacity: 0.18; transform: scale(1); }
      }
    </style>
  </defs>
  <rect width="960" height="280" fill="#F4F6FA"/>
  <rect width="960" height="280" fill="url(#glowL)"/>
  <line x1="0" y1="279.5" x2="960" y2="279.5" stroke="#006064" stroke-opacity="0.16"/>
  <g aria-hidden="true">
    <circle class="ring" cx="792" cy="96" r="52" fill="none" stroke="#0097A7" stroke-width="1.15"/>
    <circle class="ring ring2" cx="792" cy="96" r="52" fill="none" stroke="#006064" stroke-width="1.15"/>
    <circle class="ring ring3" cx="792" cy="96" r="52" fill="none" stroke="#0097A7" stroke-width="1.15"/>
    <circle cx="792" cy="96" r="38" fill="none" stroke="#0097A7" stroke-opacity="0.28" stroke-width="1"/>
    <g transform="translate(768, 72) scale(1.5)">
      <rect x="1.75" y="1.75" width="28.5" height="28.5" rx="7.5" fill="none" stroke="url(#cyanL)" stroke-width="2.5"/>
      <path fill="url(#cyanL)" d="M8.25 8h15.5v3.15L13.05 20.85h10.7v3.15H8.25v-3.15L18.95 11.15H8.25V8z"/>
    </g>
  </g>
  <text x="56" y="64" fill="#006064" font-family="ui-sans-serif, system-ui, Segoe UI, sans-serif" font-size="11" font-weight="600" letter-spacing="0.28em">TRESILLO PRESENTS</text>
  <g transform="translate(56, 86)" fill="url(#cyanL)" aria-hidden="true">
    <path d="M0 0h20.5v4.6L7.55 25.1H20.5V29.7H0v-4.6L12.95 4.6H0V0z"/>
    <path d="M27.5 0h4.7v19.4c0 2.85 1.5 4.3 4.2 4.3s4.2-1.45 4.2-4.3V0h4.7v19.7c0 5.5-3.35 10-8.9 10s-8.9-4.5-8.9-10V0z"/>
    <path d="M52.9 0h4.7v11.9L67.6 0h5.8L63.2 13.2 74 29.7h-5.9L57.6 15.4v14.3h-4.7V0z"/>
    <path d="M77.7 0h4.7v19.4c0 2.85 1.5 4.3 4.2 4.3s4.2-1.45 4.2-4.3V0h4.7v19.7c0 5.5-3.35 10-8.9 10s-8.9-4.5-8.9-10V0z"/>
  </g>
  <text x="56" y="142" fill="#0A0A0F" font-family="ui-sans-serif, system-ui, Segoe UI, sans-serif" font-size="28" font-weight="700">Create what moves next.</text>
  <text x="56" y="176" fill="#4A4A60" font-family="ui-sans-serif, system-ui, Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="15">보고, 넘기고, 직접 뛰어드세요. 창작과 플레이가 한 흐름입니다.</text>
  <g font-family="ui-sans-serif, system-ui, Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="12" font-weight="600">
    <rect x="56" y="204" width="72" height="28" rx="14" fill="none" stroke="#006064" stroke-opacity="0.4"/>
    <text x="92" y="222" text-anchor="middle" fill="#006064">플레이</text>
    <rect x="136" y="204" width="72" height="28" rx="14" fill="none" stroke="#006064" stroke-opacity="0.4"/>
    <text x="172" y="222" text-anchor="middle" fill="#006064">창작</text>
    <rect x="216" y="204" width="88" height="28" rx="14" fill="none" stroke="#006064" stroke-opacity="0.4"/>
    <text x="260" y="222" text-anchor="middle" fill="#006064">오픈소스</text>
  </g>
</svg>
'''


def main() -> None:
    (OUT / "hero-dark.svg").write_text(HERO_DARK.strip() + "\n", encoding="utf-8")
    (OUT / "hero-light.svg").write_text(HERO_LIGHT.strip() + "\n", encoding="utf-8")
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
        svg = CTA_TMPL.format(label=label, bg=bg, fg=fg, stroke=stroke, font=FONT)
        (OUT / f"{key}.svg").write_text(svg.strip() + "\n", encoding="utf-8")

    print("wrote heroes, cards, chips, ctas")


if __name__ == "__main__":
    main()
