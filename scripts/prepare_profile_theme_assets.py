"""Separate the real Rust slice and build deterministic light/dark SVG assets."""
import copy
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / "assets/profile"
NS = "{http://www.w3.org/2000/svg}"
ET.register_namespace("", NS[1:-1])
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def number(value):
    return "0" if abs(value) < .0005 else f"{value:.3f}".rstrip("0").rstrip(".")


def arc(start, end):
    def point(radius, angle):
        return f"{number(radius * math.sin(angle))},{number(-radius * math.cos(angle))}"
    large = int(end - start > math.pi)
    return f"M{point(117,start)}A117,117,0,{large},1,{point(117,end)}L{point(65,end)}A65,65,0,{large},0,{point(65,start)}Z"


graphic = ET.parse(ASSETS / "statistics.svg").getroot()
pie = next(g for g in graphic.findall(NS + "g") if any(t.text == "Python" for t in g.iter(NS + "text")))
legend = next(g for g in pie.findall(NS + "g") if g.findall(NS + "text"))
slices = next(g for g in pie.findall(NS + "g") if g.findall(NS + "path"))
if not any(t.text == "Rust" for t in legend.findall(NS + "text")):
    old_paths = slices.findall(NS + "path")
    data = []
    for path in old_paths:
        name, count = path.find(NS + "title").text.rsplit(" ", 1)
        colour = re.search(r"fill:\s*([^;]+)", path.get("style")).group(1)
        data.append({"language": name, "contributions": int(count), "colour": colour})
    # Rust's two commits were included in 'other' in the original snapshot.
    assert data[-1]["language"] == "other" and data[-1]["contributions"] == 6
    data[-1]["contributions"] -= 2
    data.insert(-1, {"language": "Rust", "contributions": 2, "colour": "#dea584"})
    total = sum(d["contributions"] for d in data)
    assert total == 1060
    marker_template = legend.find(NS + "rect")
    text_template = legend.find(NS + "text")
    legend.clear()
    legend.set("transform", "translate(273, 0)")
    for i, d in enumerate(data):
        y = (i + 1) * 32.5
        marker = copy.deepcopy(marker_template)
        marker.set("y", number(y - 21.6666666667 / 2))
        marker.set("fill", d["colour"])
        legend.append(marker)
        label = copy.deepcopy(text_template)
        label.text = d["language"]
        label.set("y", number(y))
        legend.append(label)
    start = sum(d["contributions"] for d in data[:5]) / total * 2 * math.pi
    old_other = old_paths[-1]
    slices.remove(old_other)
    for d in data[-2:]:
        end = start + d["contributions"] / total * 2 * math.pi
        path = copy.deepcopy(old_other)
        path.set("d", arc(start, end))
        path.set("style", f"fill: {d['colour']};")
        path.find(NS + "title").text = f"{d['language']} {d['contributions']}"
        slices.append(path)
        start = end
    (ASSETS / "language-metadata.json").write_text(json.dumps({"metric": "Commit contributions by repository primary language", "snapshotDate": "2026-10-25", "total": total, "languages": data}, indent=2) + "\n")


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

print("Separated Rust's two commits from other; totals preserved. Built fixed light/dark greetings and charts.")
