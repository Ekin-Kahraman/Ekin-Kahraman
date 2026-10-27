"""Check the published profile's links, assets and contribution geometry."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "README.md").read_text()
assert not re.search(r"<(?:script|style)\b|data:image/", text, re.I), "README must use GitHub-compatible markup"
for term in ("Creator of RustScenic.", "Leading RustScenic’s development", "Huang Lab", "Kuan-Lin Huang", "Connect With Me", "Statistics", "Open-source software contributions", "See what I’ve built", "3× faster", "~80% lower peak memory"):
    assert term in text, f"Missing approved content: {term}"
assert "Open to" not in text and "Telegram" not in text
assert text.count("mailto:evk23umu@uea.ac.uk") == 1
assert "pinned-projects" not in text, "The project invitation must not change the URL to a pinned anchor"
for path in re.findall(r'(?:src|srcset)="(assets/[^\"]+)"', text):
    assert (ROOT / path).is_file(), f"Missing image: {path}"
for path in (ROOT / "assets/profile").glob("*.svg"):
    graphic = ET.parse(path).getroot()
    assert not any(n.tag.rsplit("}", 1)[-1] == "script" for n in graphic.iter()), path
projects = json.loads((ROOT / "scripts/pinned-projects.json").read_text())
assert len(projects) == 6 and projects[0]["name"] == "rustscenic" and projects[1]["name"] == "safetynett"
assert all(len(p["description"]) <= 350 for p in projects)
ns = "{http://www.w3.org/2000/svg}"
graphic = ET.parse(ROOT / "assets/profile/statistics.svg").getroot()
assert graphic.get("data-weak-day-scale") == "10"
assert graphic.get("data-remaining-day-scale") == "2"
zeros = [r for r in graphic.iter(ns + "rect") if r.get("class") in ("rb-l0-left", "rb-l0-right")]
assert zeros and all(float(r.get("height")) == 2.6 for r in zeros), "Empty days must stay flat"
assert all(n.get("repeatCount") == "indefinite" for n in graphic.iter() if n.tag.rsplit("}", 1)[-1] in ("animate", "animateTransform") and n.get("attributeName") in ("height", "transform"))
still = ET.parse(ROOT / "assets/profile/statistics-still.svg").getroot()
assert not any(n.tag.rsplit("}", 1)[-1] in ("animate", "animateTransform", "animateMotion") for n in still.iter())
workstation = (ROOT / "assets/profile/workstation.svg").read_text()
assert "plant-wind-filter" in workstation and "hardware-slate" in workstation
assert "Hi, I’m Ekin!" not in workstation and "mouse-use" in workstation
language_data = json.loads((ROOT / "assets/profile/language-metadata.json").read_text())
counts = {entry["language"]: entry["contributions"] for entry in language_data["languages"]}
assert counts["Rust"] == 2 and counts["other"] == 4
assert sum(counts.values()) == language_data["total"] == 1060
for theme in ("light", "dark"):
    for static in (False, True):
        suffix = f"{'still-' if static else ''}{theme}.svg"
        greeting = (ROOT / "assets/profile" / f"hello-{suffix}").read_text()
        chart = (ROOT / "assets/profile" / f"statistics-{suffix}").read_text()
        assert "prefers-color-scheme" not in greeting + chart, "Theme must be selected by GitHub's picture element"
        assert "Hi, I’m Ekin!" in greeting
        expected_ink = "#f0f6fc" if theme == "dark" else "#1f2328"
        labels = ET.fromstring(greeting).iter(ns + "text")
        assert all(label.get("fill") == expected_ink for label in labels)
        assert "Rust 2" in chart and "other 4" in chart
        backgrounds = re.findall(r"\.fill-bg\s*\{\s*fill:\s*(#[0-9a-fA-F]{6})", chart)
        assert backgrounds and set(backgrounds) == {"#000000"}, "Statistics canvas must stay pure black"
        if static:
            assert not any(n.tag.rsplit("}", 1)[-1] in ("animate", "animateTransform", "animateMotion") for n in ET.fromstring(chart).iter())
print("Profile content, links, responsive assets, animations and zero-day geometry validated.")
