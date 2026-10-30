"""Check the published profile's links, assets and contribution geometry."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "README.md").read_text()
assert not re.search(r"<(?:script|style)\b|data:image/", text, re.I), "README must use GitHub-compatible markup"
for term in ("Creator of RustScenic.", "Leading RustScenic’s development", "Huang Lab", "Kuan-Lin Huang", "Connect With Me", "Statistics", "Open-source contributions", "Pinned projects below", "3× faster", "~80% lower peak memory"):
    assert term in text, f"Missing approved content: {term}"
assert "Open to" not in text and "Telegram" not in text
assert text.count("mailto:evk23umu@uea.ac.uk") == 1
assert "pinned-projects" not in text, "The projects cue must not leave a fragment that redirects on refresh"
assert "See what I’ve built" not in text, "Keep the old projects banner removed"
project_footer = text.rsplit("\n---\n", 1)[-1]
assert 'src="assets/profile/projects-arrow.svg" width="144" height="176"' in project_footer, "Keep the prominent arrow below the section divider"
assert not re.search(r"<(?:a|details|summary)\b", project_footer), "The arrow must stay a visual cue without links or an expanded list"
assert "Open-source contributions" not in project_footer, "Keep the arrow separate from Open-source contributions"
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
assert "Rust" in counts and "other" in counts
assert all(isinstance(count, int) and count >= 0 for count in counts.values())
assert sum(counts.values()) == language_data["total"]
statistics = json.loads((ROOT / "assets/profile/statistics-metadata.json").read_text())
assert language_data["total"] == statistics["contributionTypes"]["Commit"]
days = statistics["contributionDays"]
assert sum(d["contributionCount"] for d in days) == statistics["totalContributions"]
bars = {g.get("data-date"): g for g in graphic.find(ns + "g").findall(ns + "g")}
assert len(bars) == len(days)
for day in days:
    bar = bars[day["date"]]
    assert int(bar.get("data-count")) == day["contributionCount"]
    if day["contributionCount"] == 0:
        assert all(float(r.get("height")) == 2.6 for r in bar.findall(ns + "rect") if r.get("class").endswith(("-left", "-right")))
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
        parsed_chart = ET.fromstring(chart)
        assert parsed_chart.get("data-total-contributions") == str(statistics["totalContributions"])
        titles = {n.text for n in parsed_chart.iter(ns + "title")}
        assert all(f"{name} {count}" in titles for name, count in counts.items())
        assert not re.search(r"\d{4}-\d{2}-\d{2}\s*/\s*\d{4}-\d{2}-\d{2}", chart), "Keep the top-right date label removed"
        backgrounds = re.findall(r"\.fill-bg\s*\{\s*fill:\s*(#[0-9a-fA-F]{6})", chart)
        assert backgrounds and set(backgrounds) == {"#000000"}, "Statistics canvas must stay pure black"
        if static:
            assert not any(n.tag.rsplit("}", 1)[-1] in ("animate", "animateTransform", "animateMotion") for n in ET.fromstring(chart).iter())
print("Profile content, links, responsive assets, animations and zero-day geometry validated.")
