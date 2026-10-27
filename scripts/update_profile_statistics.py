"""Refresh the existing statistics artwork from GitHub's contribution API."""
import argparse
import copy
from datetime import date, datetime, timezone
import json
import math
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/profile"
NS = "{http://www.w3.org/2000/svg}"
ET.register_namespace("", NS[1:-1])
QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday contributionLevel } }
      }
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      totalRepositoryContributions
      commitContributionsByRepository(maxRepositories: 100) {
        repository { primaryLanguage { name color } }
        contributions { totalCount }
      }
    }
  }
}
"""
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2,
          "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
TYPE_FIELDS = {"Commit": "totalCommitContributions", "Issue": "totalIssueContributions",
               "PullReq": "totalPullRequestContributions", "Review": "totalPullRequestReviewContributions",
               "Repo": "totalRepositoryContributions"}


def number(value):
    return "0" if abs(value) < .0005 else f"{value:.3f}".rstrip("0").rstrip(".")


def read_live_data(year):
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", "query=" + QUERY, "-f", "login=Ekin-Kahraman",
         "-f", f"from={year}-01-01T00:00:00Z", "-f", f"to={year}-12-31T23:59:59Z"],
        capture_output=True, text=True, check=True, timeout=90,
    )
    response = json.loads(result.stdout)
    if response.get("errors"):
        raise ValueError(f"GitHub returned errors: {response['errors']}")
    return response["data"]["user"]["contributionsCollection"]


def normalize(collection, year):
    calendar = collection["contributionCalendar"]
    days = [day for week in calendar["weeks"] for day in week["contributionDays"]]
    days = sorted((d for d in days if date.fromisoformat(d["date"]).year == year), key=lambda d: d["date"])
    expected_days = (date(year + 1, 1, 1) - date(year, 1, 1)).days
    if len({d["date"] for d in days}) != expected_days or len(days) != expected_days:
        raise ValueError("GitHub did not return a complete calendar; leaving the published graphic intact")
    for day in days:
        if (not isinstance(day["contributionCount"], int) or day["contributionCount"] < 0
                or day["contributionLevel"] not in LEVELS
                or day["weekday"] != (date.fromisoformat(day["date"]).weekday() + 1) % 7):
            raise ValueError("Invalid contribution day")
    if sum(d["contributionCount"] for d in days) != calendar["totalContributions"]:
        raise ValueError("Daily contributions do not match GitHub's total")
    types = {label: collection[field] for label, field in TYPE_FIELDS.items()}
    if any(not isinstance(count, int) or count < 0 for count in types.values()):
        raise ValueError("Invalid contribution type totals")
    languages = {}
    for repo in collection["commitContributionsByRepository"]:
        lang = repo["repository"]["primaryLanguage"]
        name = lang["name"] if lang else "other"
        entry = languages.setdefault(name, {"language": name, "contributions": 0,
                                             "colour": (lang["color"] if lang else None) or "#444444"})
        count = repo["contributions"]["totalCount"]
        if not isinstance(count, int) or count < 0:
            raise ValueError("Invalid repository contribution count")
        entry["contributions"] += count
    # Keep the established five leading languages plus Rust and a truthful remainder.
    ranked = sorted((v for k, v in languages.items() if k not in ("Rust", "other")),
                    key=lambda v: (-v["contributions"], v["language"]))
    visible = ranked[:5]
    visible.append(languages.get("Rust", {"language": "Rust", "contributions": 0, "colour": "#dea584"}))
    other = types["Commit"] - sum(v["contributions"] for v in visible)
    if other < 0 or sum(v["contributions"] for v in languages.values()) > types["Commit"]:
        raise ValueError("Language counts exceed commit contributions")
    visible.append({"language": "other", "contributions": other, "colour": "#444444"})
    snapshot = {"totalContributions": calendar["totalContributions"], "year": year,
                "contributionTypes": types, "contributionDays": days}
    language_data = {"metric": "Commit contributions by repository primary language",
                     "total": types["Commit"], "languages": visible}
    return snapshot, language_data


def loop(parent, tag, attribute, start, end, **extra):
    return ET.SubElement(parent, NS + tag, {
        "attributeName": attribute, "values": f"{start};{end};{end};{start}",
        "dur": "14s", "repeatCount": "indefinite", "keyTimes": "0;.22;.94;1", **extra,
    })


def update_skyline(graphic, days):
    skyline = graphic.find(NS + "g")
    prototype = copy.deepcopy(skyline.find(NS + "g"))
    skyline.clear()
    first = date.fromisoformat(days[0]["date"])
    first_sunday = first.toordinal() - days[0]["weekday"]
    weeks = math.ceil((len(days) + days[0]["weekday"]) / 7)
    dy = 20 / math.sqrt(3)
    for day in days:
        week = (date.fromisoformat(day["date"]).toordinal() - first_sunday) // 7
        count = day["contributionCount"]
        x = 140 + (week - day["weekday"]) * 20
        base_y = 850 - (weeks + 7) * dy + (week + day["weekday"]) * dy
        raw_height = math.log10(count / 20 + 1) * 144 + 3
        flat_y = round(base_y - 3, 2)
        scale = 1.2 * (10 if 0 < count <= 3 else 2)
        y = flat_y + (round(base_y - raw_height, 2) - flat_y) * scale
        height = 2.6 + (round(raw_height * math.sqrt(3) / 2, 2) - 2.6) * scale
        if count == 0:
            y, height = flat_y, 2.6
        bar = ET.SubElement(skyline, NS + "g", {"transform": f"translate({number(x)} {number(y)})",
                            "data-date": day["date"], "data-count": str(count)})
        if 0 < count <= 3:
            bar.set("class", "weak-day")
        ET.SubElement(bar, NS + "title").text = f"{day['date']}: {count} contributions"
        if count:
            loop(bar, "animateTransform", "transform", f"{number(x)} {number(flat_y)}",
                 f"{number(x)} {number(y)}", type="translate")
        for original in prototype.findall(NS + "rect"):
            face = copy.deepcopy(original)
            for child in list(face):
                face.remove(child)
            side = face.get("class").rsplit("-", 1)[-1]
            face.set("class", f"rb-l{LEVELS[day['contributionLevel']]}-{side}")
            face.set("style", f"animation-delay:{-((-week * 7) % 360) / 36:.3f}s")
            if side != "top":
                face.set("height", number(height))
                if count:
                    loop(face, "animate", "height", "2.6", number(height))
            bar.append(face)


def update_radar(graphic, types):
    radar = next(g for g in graphic.findall(NS + "g") if g.find(NS + "polygon") is not None)
    for label in radar.iter(NS + "text"):
        if label.text in types:
            label.find(NS + "title").text = str(types[label.text])
    def points(values):
        coords = []
        for i, value in enumerate(values):
            level = min(math.log10(value), 5) + 1 if value else .8
            radius = 156 * level / 5
            angle = i / 5 * 2 * math.pi
            coords.append(f"{number(radius * math.sin(angle))},{number(-radius * math.cos(angle))}")
        return " ".join(coords)
    polygon = radar.find(NS + "polygon")
    polygon.clear()
    polygon.set("class", "radar")
    end = points(list(types.values()))
    polygon.set("points", end)
    loop(polygon, "animate", "points", points([0] * 5), end)


def update_languages(graphic, data):
    pie = next(g for g in graphic.findall(NS + "g") if any(c.findall(NS + "path") for c in g.findall(NS + "g")))
    legend, slices = pie.findall(NS + "g")
    marker_template = copy.deepcopy(legend.find(NS + "rect"))
    label_template = copy.deepcopy(legend.find(NS + "text"))
    slice_templates = [copy.deepcopy(p) for p in slices.findall(NS + "path")]
    legend[:] = []
    slices[:] = []
    angle = 0
    def point(radius, a):
        return f"{number(radius * math.sin(a))},{number(-radius * math.cos(a))}"
    for i, entry in enumerate(data["languages"]):
        y = (i + 1) * 32.5
        marker, label = copy.deepcopy(marker_template), copy.deepcopy(label_template)
        marker.set("y", number(y - 21.6666666667 / 2))
        marker.set("fill", entry["colour"])
        label.set("y", number(y))
        label.text = entry["language"]
        legend.extend([marker, label])
        end = angle + (entry["contributions"] / data["total"] * 2 * math.pi if data["total"] else 0)
        path = copy.deepcopy(slice_templates[min(i, len(slice_templates) - 1)])
        large = int(end - angle > math.pi)
        if end - angle >= 2 * math.pi - 1e-8:
            path.set("d", "M0,-117A117,117,0,1,1,0,117A117,117,0,1,1,0,-117M0,-65A65,65,0,1,0,0,65A65,65,0,1,0,0,-65Z")
        elif entry["contributions"]:
            path.set("d", f"M{point(117,angle)}A117,117,0,{large},1,{point(117,end)}L{point(65,end)}A65,65,0,{large},0,{point(65,angle)}Z")
        else:
            path.set("d", "M0,0Z")
        path.set("style", f"fill: {entry['colour']};")
        path.find(NS + "title").text = f"{entry['language']} {entry['contributions']}"
        slices.append(path)
        angle = end


def pin_readme(revision):
    if not re.fullmatch(r"[a-f0-9]{40}", revision):
        raise ValueError("Expected a full asset commit SHA")
    path = ROOT / "README.md"
    text = path.read_text()
    text, count = re.subn(
        r"https://raw\.githubusercontent\.com/Ekin-Kahraman/Ekin-Kahraman/[a-f0-9]{40}/assets/profile/(statistics-(?:still-)?(?:dark|light)\.svg)",
        lambda m: f"https://raw.githubusercontent.com/Ekin-Kahraman/Ekin-Kahraman/{revision}/assets/profile/{m[1]}", text)
    if count != 4:
        raise ValueError("Expected exactly four statistics image URLs")
    year = json.loads((ASSETS / "statistics-metadata.json").read_text())["year"]
    text = re.sub(r"from=\d{4}-01-01&amp;to=\d{4}-12-31", f"from={year}-01-01&amp;to={year}-12-31", text)
    text = re.sub(r"Ekin Kahraman’s \d{4} contribution skyline", f"Ekin Kahraman’s {year} contribution skyline", text)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", type=int, default=datetime.now(timezone.utc).year)
    parser.add_argument("--input", type=Path, help="Saved contributionsCollection JSON for reproducible checks")
    parser.add_argument("--force", action="store_true", help="Regenerate artwork even if the data is unchanged")
    parser.add_argument("--pin-readme", help="Point README images at a published asset commit")
    args = parser.parse_args()
    if args.pin_readme:
        pin_readme(args.pin_readme)
        return
    collection = json.loads(args.input.read_text()) if args.input else read_live_data(args.year)
    snapshot, language_data = normalize(collection, args.year)
    old_snapshot = json.loads((ASSETS / "statistics-metadata.json").read_text())
    old_languages = json.loads((ASSETS / "language-metadata.json").read_text())
    # Do not create hourly commits when the underlying data is unchanged.
    for old in (old_snapshot, old_languages):
        old.pop("snapshotDate", None)
    if not args.force and snapshot == old_snapshot and language_data == old_languages:
        print(f"Statistics already current: {snapshot['totalContributions']:,} contributions")
        return
    graphic = ET.parse(ASSETS / "statistics.svg").getroot()
    graphic.set("aria-label", f"Ekin Kahraman, GitHub contributions in {args.year}")
    graphic.set("data-total-contributions", str(snapshot["totalContributions"]))
    graphic.set("data-year", str(args.year))
    update_skyline(graphic, snapshot["contributionDays"])
    update_radar(graphic, snapshot["contributionTypes"])
    update_languages(graphic, language_data)
    footer = next(g for g in graphic.findall(NS + "g") if any(t.text == "contributions" for t in g.findall(NS + "text")))
    footer.find(NS + "text").text = str(snapshot["totalContributions"])
    (ASSETS / "statistics.svg").write_text(ET.tostring(graphic, encoding="unicode") + "\n")
    for filename, payload in (("statistics-metadata.json", snapshot), ("language-metadata.json", language_data)):
        payload["snapshotDate"] = datetime.now(timezone.utc).date().isoformat()
        (ASSETS / filename).write_text(json.dumps(payload, indent=2) + "\n")
    subprocess.run(["python3", str(ROOT / "scripts/prepare_profile_theme_assets.py")], check=True)
    print(f"Updated statistics: {snapshot['totalContributions']:,} contributions")


if __name__ == "__main__":
    main()
