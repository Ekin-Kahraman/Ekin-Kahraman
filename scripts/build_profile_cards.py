"""Build the GitHub-compatible SVG cards used by the profile README."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/profile"
FONT = '-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif'
ET.register_namespace("", "http://www.w3.org/2000/svg")
logo = ET.parse(ASSETS / "rustscenic-logo.svg").getroot()
logo_content = "".join(ET.tostring(c, encoding="unicode") for c in logo)


def write(name, width, height, title, content, style=""):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{title}</title><style>text{{font-family:{FONT}}}{style}</style>{content}</svg>'''
    ET.fromstring(svg)
    (ASSETS / name).write_text(svg + "\n")


def text(x, y, value, size, colour, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{colour}" {extra}>{value}</text>'


for theme in ("light", "dark"):
    dark = theme == "dark"
    bg, ink, muted, border = ("#24180f", "#f0ab89", "#9198a1", "#704025") if dark else ("#fff4ec", "#8b3d1c", "#59636e", "#e1b8a2")
    for mobile in (False, True):
        width, height = (360, 380) if mobile else (700, 324)
        x = width / 2
        title_size = 35 if mobile else 42
        logo_size = 52 if mobile else 64
        title_width = 169 if mobile else 203
        title_x = (width - title_width - 12 - logo_size) / 2 + 5
        logo_x, logo_y = title_x + title_width + 12, 13
        content = f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="5" fill="{bg}" stroke="{border}"/>'
        content += text(title_x, 61, "RustScenic", title_size, "#d46f40", 600, 'letter-spacing="-1.3"')
        content += f'<svg x="{logo_x}" y="{logo_y}" width="{logo_size}" height="{logo_size}" viewBox="0 0 1024 1024">{logo_content}</svg>'
        lines = (["The simplest, fastest software", "for studying gene regulation", "in single-cell data."] if mobile else ["The simplest, fastest software for studying gene regulation", "in single-cell data."])
        for i, line in enumerate(lines): content += text(x, 104 + i*25, line, 17 if mobile else 18, ink, 500, 'text-anchor="middle"')
        content += text(x, 183 if mobile else 165, "Published Python package, powered by Rust.", 11.5 if mobile else 12, muted, extra='text-anchor="middle"')
        if mobile:
            content += text(x, 229, "3.3× faster", 20, ink, 600, 'text-anchor="middle"')
            content += text(x, 259, "81% lower peak memory", 20, ink, 600, 'text-anchor="middle"')
        else:
            content += text(x, 211, '3.3× faster<tspan dx="24">81% lower peak memory</tspan>', 20, ink, 600, 'text-anchor="middle"')
        comparison = ["Benchmarked against widely used", "gene-regulation software."] if mobile else ["Benchmarked against widely used gene-regulation software."]
        for i, line in enumerate(comparison): content += text(x, (287 if mobile else 236) + i*16, line, 10.5 if mobile else 11, muted, extra='text-anchor="middle"')
        button_y = 325 if mobile else 260
        button_x = (width - 186) / 2
        content += f'<rect x="{button_x}" y="{button_y}" width="186" height="40" rx="4" fill="#d46f40"/>'
        content += text(button_x+15, button_y+25, "Explore RustScenic", 13, "#10131a", 600)
        content += text(button_x+163, button_y+26, "→", 20, "#10131a", 600, 'class="explore-arrow"')
        style = '.explore-arrow{animation:invite 1.8s ease-in-out infinite}@keyframes invite{50%{transform:translateX(5px)}}@media(prefers-reduced-motion:reduce){.explore-arrow,.floating-mark{animation:none}}'
        write(f"rustscenic-{theme}{'-mobile' if mobile else ''}.svg", width, height, "RustScenic: the simplest, fastest software for studying gene regulation in single-cell data. 3.3× faster, 81% lower peak memory. Explore RustScenic.", content, style)
        green_bg, green_text = ("#10211b", "#9be9a8") if dark else ("#e0eee3", "#1a6b2c")
        banner_width = 320 if mobile else 700
        content = f'<rect x=".5" y=".5" width="{banner_width-1}" height="63" rx="5" fill="{green_bg}" stroke="#3fb950" stroke-opacity=".4"/>'
        content += text(banner_width/2, 39, "See what I’ve built", 20, green_text, 600, 'letter-spacing="-.35" text-anchor="middle"')
        for arrow_x in (banner_width/2-112, banner_width/2+112):
            content += text(arrow_x, 41, "↓", 27, green_text, 400, 'class="project-arrow" text-anchor="middle"')
        style = '.project-arrow{animation:down 1.8s ease-in-out infinite}@keyframes down{50%{transform:translateY(4px)}}@media(prefers-reduced-motion:reduce){.project-arrow{animation:none}}'
        write(f"projects-{theme}{'-mobile' if mobile else ''}.svg", banner_width, 64, "See what I’ve built — explore pinned projects", content, style)

for name, colour, label, width in (("email", "#d14836", "EMAIL", 132), ("linkedin", "#0077b5", "LINKEDIN", 132)):
    content = f'<rect width="{width}" height="40" fill="{colour}"/>'
    if name == "email":
        content += '<g fill="none" stroke="white" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="27.5" y="13" width="19" height="14" rx="1.5"/><path d="M28.5 14.5 37 21 45.5 14.5"/></g>'
    label_x = 56.5 if name == "email" else width / 2
    label_anchor = "start" if name == "email" else "middle"
    label_length = ' textLength="48" lengthAdjust="spacing"' if name == "email" else ""
    content += text(label_x, 20, label, 13, "white", 800, f'letter-spacing="1.6" text-anchor="{label_anchor}" dominant-baseline="central"{label_length}')
    write(f"{name}.svg", width, 40, "Email Ekin Kahraman" if name == "email" else "Ekin Kahraman on LinkedIn", content)

arrow = '<g class="feature-direction"><path d="M20 18V74M7 61L20 74L33 61" fill="none" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></g>'
arrow_style = '.feature-direction{animation:feature-point 2.4s ease-in-out infinite}@keyframes feature-point{0%,100%{transform:translateY(0)}50%{transform:translateY(6px)}}@media(prefers-reduced-motion:reduce){.feature-direction{animation:none}}'
write("rustscenic-arrow.svg", 40, 110, "Explore RustScenic below", arrow, arrow_style)

print("Built themed, responsive profile cards.")
