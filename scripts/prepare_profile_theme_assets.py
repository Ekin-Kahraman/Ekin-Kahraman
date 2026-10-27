"""Build deterministic light/dark assets from the current statistics master."""
import copy
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / "assets/profile"
NS = "{http://www.w3.org/2000/svg}"
ET.register_namespace("", NS[1:-1])
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


graphic = ET.parse(ASSETS / "statistics.svg").getroot()


def remove_motion(root):
    for parent in root.iter():
        for child in list(parent):
            if child.tag.rsplit("}", 1)[-1] in ("animate", "animateTransform", "animateMotion"):
                parent.remove(child)


def fixed_theme(css, theme):
    match = re.search(r"@media\s*\(prefers-color-scheme:\s*dark\)\s*\{", css)
    if not match:
        return css
    start, level, end = match.end(), 1, match.end()
    while level:
        level += (css[end] == "{") - (css[end] == "}")
        end += 1
    light = css[:match.start()] + css[end:]
    return light if theme == "light" else light + "\n" + css[start:end-1]


# Keep the redundant date range out of every rendered statistics variant.
for parent in graphic.iter():
    for child in list(parent):
        if child.tag == NS + "text" and re.fullmatch(r"\d{4}-\d{2}-\d{2}\s*/\s*\d{4}-\d{2}-\d{2}", "".join(child.itertext()).strip()):
            parent.remove(child)

# The statistics card intentionally keeps its own black canvas in both GitHub themes.
for style in graphic.findall(NS + "style"):
    css = fixed_theme(style.text or "", "dark")
    css = re.sub(r"(\.(?:fill|stroke)-bg\s*\{\s*(?:fill|stroke):\s*)#[0-9a-fA-F]{6}", r"\g<1>#000000", css)
    style.text = css

(ASSETS / "statistics.svg").write_text(ET.tostring(graphic, encoding="unicode") + "\n")
still = copy.deepcopy(graphic)
remove_motion(still)
(ASSETS / "statistics-still.svg").write_text(ET.tostring(still, encoding="unicode") + "\n")
for theme in ("light", "dark"):
    for static in (False, True):
        themed = copy.deepcopy(still if static else graphic)
        for style in themed.findall(NS + "style"):
            style.text = fixed_theme(style.text or "", theme)
        name = f"statistics-{'still-' if static else ''}{theme}.svg"
        (ASSETS / name).write_text(ET.tostring(themed, encoding="unicode") + "\n")

for theme in ("light", "dark"):
    for static in (False, True):
        path = ASSETS / f"hello-{'still-' if static else ''}{theme}.svg"
        hello = ET.fromstring(path.read_text().replace("Hi, I’m Ekin.", "Hi, I’m Ekin!"))
        for style in hello.findall(NS + "style"):
            # Theme selection belongs to GitHub's picture element, not the SVG's OS media query.
            font = re.search(r"@font-face\s*\{.*?\}", style.text or "", re.S)
            style.text = font.group(0) if font else ""
        for label in hello.iter(NS + "text"):
            label.set("fill", "#f0f6fc" if theme == "dark" else "#1f2328")
        serialized = ET.tostring(hello, encoding="unicode")
        path.write_text("\n".join(line.rstrip() for line in serialized.splitlines()) + "\n")

print("Built fixed light/dark greetings and current statistics variants.")
