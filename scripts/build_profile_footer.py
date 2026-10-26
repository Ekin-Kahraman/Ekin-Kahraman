"""Build the profile's contribution panel and project invitation as native SVGs."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/profile"
FONT = '-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif'

# Verified merged on 26 October 2026: Scanpy 4032, 4056, 4057, 4058, 4059;
# PyDESeq2 442 and 443. These are contributions, including documentation,
# rather than a claim to have authored or maintained either package.
PALETTES = {
    "dark": dict(bg="#171322", panel="#211a32", ink="#f0f3fa", muted="#b6adc9",
                 accent="#c4a3ff", border="#594272", green="#a6e3bd", work="#121f20"),
    "light": dict(bg="#f6f1ff", panel="#eee5fc", ink="#282033", muted="#645473",
                  accent="#7041ad", border="#cbb6e6", green="#226a45", work="#edf7f0"),
}


def text(x, y, value, size, colour, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-family=\'{FONT}\' font-size="{size}" '
            f'font-weight="{weight}" fill="{colour}" {extra}>{escape(value)}</text>')


def write(name, width, height, title, content, style=""):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">'
           f'<title id="title">{escape(title)}</title>'
           f'<style>{style}@media(prefers-reduced-motion:reduce)'
           '{.signal,.direction{animation:none}}</style>' + content + '</svg>\n')
    ET.fromstring(svg)
    (ASSETS / name).write_text(svg)


def merge_mark(x, y, colour, scale=1):
    return (f'<g transform="translate({x} {y}) scale({scale})" fill="none" '
            f'stroke="{colour}" stroke-width="2.5" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M10 9v32M38 9v6c0 15-28 10-28 21"/>'
            '<circle cx="10" cy="7" r="5"/><circle cx="10" cy="44" r="5"/>'
            '<circle cx="38" cy="7" r="5"/></g>')


for theme, p in PALETTES.items():
    for mobile in (False, True):
        suffix = f"{theme}{'-mobile' if mobile else ''}"
        w, h = (360, 280) if mobile else (700, 244)
        content = (f'<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1">'
                   f'<stop stop-color="{p["panel"]}"/><stop offset="1" stop-color="{p["bg"]}"/>'
                   '</linearGradient></defs>'
                   f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" '
                   f'fill="url(#wash)" stroke="{p["border"]}"/>')
        content += text(26 if mobile else 32, 34, "OPEN-SOURCE SOFTWARE CONTRIBUTIONS", 10.4 if mobile else 11.5,
                        p["accent"], 700, 'letter-spacing="1.3"')
        if mobile:
            content += text(25, 139, "7", 112, p["accent"], 750, 'letter-spacing="-6"')
            content += text(117, 91, "Merged pull", 27, p["ink"], 700, 'letter-spacing="-.7"')
            content += text(117, 125, "requests.", 27, p["ink"], 700, 'letter-spacing="-.7"')
            content += f'<path d="M26 166H334" stroke="{p["border"]}"/>'
            content += text(26, 202, "Scanpy + PyDESeq2", 24, p["ink"], 650, 'letter-spacing="-.6"')
            content += text(26, 233, "Accepted contributions to established", 14, p["muted"])
            content += text(26, 254, "scientific software.", 14, p["muted"])
        else:
            content += text(30, 165, "7", 134, p["accent"], 750, 'letter-spacing="-7"')
            content += text(150, 98, "Merged pull requests.", 34, p["ink"], 700, 'letter-spacing="-1.2"')
            content += text(152, 133, "Scanpy + PyDESeq2", 23, p["accent"], 550)
            content += text(152, 166, "Accepted contributions to established scientific software.", 14, p["muted"])
            content += merge_mark(600, 72, p["accent"], 1.25)
            content += f'<path d="M32 197H668" stroke="{p["border"]}"/>'
            content += text(32, 224, "Plot examples, clearer errors and documentation fixes.", 13.5, p["muted"])
            content += f'<circle class="signal" cx="656" cy="220" r="4" fill="{p["green"]}"/>'
        write(f"contributions-{suffix}.svg", w, h,
              "Open-source software contributions: 7 merged pull requests in Scanpy and PyDESeq2.", content,
              '.signal{animation:signal 3s ease-in-out infinite}@keyframes signal{50%{opacity:.35}}')

        # The invitation points directly into GitHub's native pinned repositories.
        w, h = (360, 228) if mobile else (700, 210)
        content = (f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" '
                   f'fill="{p["work"]}" stroke="{p["green"]}" stroke-opacity=".45"/>')
        content += text(w/2, 31, "SELECTED PROJECTS", 10.5, p["green"], 700,
                        'letter-spacing="2.3" text-anchor="middle"')
        content += text(w/2, 79 if mobile else 84, "See what I’ve built", 31 if mobile else 43,
                        p["ink"], 700, 'letter-spacing="-1.4" text-anchor="middle"')
        lines = ["Research software, ML", "and automated workflows."] if mobile else ["Research software, ML and automated workflows."]
        for i, line in enumerate(lines):
            content += text(w/2, (110 if mobile else 119) + i*21, line, 14 if mobile else 16,
                            p["muted"], extra='text-anchor="middle"')
        cy = 169 if mobile else 157
        centres = [w/2 + (i-2.5)*(43 if mobile else 64) for i in range(6)]
        content += (f'<path d="M{centres[0]} {cy}H{centres[-1]}" fill="none" '
                    f'stroke="{p["green"]}" stroke-opacity=".4" stroke-dasharray="3 5"/>')
        colours = ["#d8784d", "#b785d1", "#65a4d4", "#78ae96", "#c49a55", "#7f91d6"]
        glyphs = [
            '<path d="m-7-6 14 12M-7 6 7-6M0-8v16"/><circle cy="-8" r="2"/><circle cy="8" r="2"/>',
            '<path d="M0-7v14M-7 0H7"/>',
            '<circle cx="-4" cy="-3" r="4"/><circle cx="5" cy="4" r="4"/>',
            '<path d="M-7 7V0M0 7V-7M7 7V-3"/>',
            '<circle cx="-5" cy="-4" r="2"/><circle cx="5" cy="-4" r="2"/><circle cy="5" r="2"/>',
            '<path d="M-7-5H7M-7 5H7M-5-7v4M0-7v4M5 3v4"/>',
        ]
        for cx, colour, glyph in zip(centres, colours, glyphs):
            content += (f'<rect x="{cx-16}" y="{cy-16}" width="32" height="32" rx="7" '
                        f'fill="{p["work"]}" stroke="{colour}" stroke-opacity=".65"/>'
                        f'<g transform="translate({cx} {cy})" fill="none" stroke="{colour}" '
                        f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{glyph}</g>')
        ay = 208 if mobile else 194
        content += (f'<g class="direction" fill="none" stroke="{p["green"]}" stroke-width="2" '
                    f'stroke-linecap="round" stroke-linejoin="round">'
                    f'<path d="M{w/2} {ay-10}v13m-5-5 5 5 5-5"/></g>')
        write(f"projects-invitation-{suffix}.svg", w, h,
              "See what I’ve built: research software, ML and automated workflows. Explore the six pinned projects below.",
              content, '.direction{animation:direction 2.4s ease-in-out infinite}'
              '@keyframes direction{50%{transform:translateY(4px)}}')

    for name, count, label in (("scanpy", 5, "Scanpy"), ("pydeseq2", 2, "PyDESeq2")):
        content = (f'<rect x="1" y="1" width="338" height="77" rx="10" '
                   f'fill="{p["bg"]}" stroke="{p["border"]}"/>')
        content += merge_mark(17, 23, p["accent"], .6)
        content += text(61, 33, label, 23, p["ink"], 650, 'letter-spacing="-.5"')
        content += text(61, 57, f"{count} merged pull requests", 13.5, p["muted"])
        content += text(311, 46, "↗", 25, p["accent"], 500, 'text-anchor="middle"')
        write(f"contribution-link-{name}-{theme}.svg", 340, 79,
              f"{label}: view {count} merged pull requests", content)
        content = (f'<rect x="1" y="1" width="168" height="75" rx="10" '
                   f'fill="{p["bg"]}" stroke="{p["border"]}"/>')
        content += text(16, 30, label, 20.5, p["ink"], 650, 'letter-spacing="-.5"')
        content += text(16, 56, f"{count} merged PRs", 13.5, p["muted"])
        content += text(148, 56, "↗", 21, p["accent"], 500, 'text-anchor="middle"')
        write(f"contribution-link-{name}-{theme}-mobile.svg", 170, 77,
              f"{label}: view {count} merged pull requests", content)

print("Built contribution and project panels for both themes and screen sizes.")
