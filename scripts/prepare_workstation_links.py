"""Give the laptop URL its own link using GitHub-compatible SVG views.

The five views partition the existing artwork; no pixels or motion are edited.
All animated views share one URL/download and the same animation clock.
"""
import argparse
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/profile"
START = "<!-- workstation-links:start -->"
END = "<!-- workstation-links:end -->"
VIEWS = {
    "top": (30, 110, 1645, 514),
    "left": (30, 624, 1292, 38),
    "linkedin": (1322, 624, 210, 38),
    "right": (1532, 624, 143, 38),
    "bottom": (30, 662, 1645, 183),
}


def linked_artwork(source):
    # Each of the three middle images contributes this intrinsic width to
    # GitHub's shrink-to-fit layout. Explicit 700px top/bottom images retain
    # the original maximum width; max-width:100% handles narrower screens.
    source = source.replace('width="1645" height="735"', 'width="233.333333333333"', 1)
    views = "\n".join(
        f'  <view id="workstation-{name}" viewBox="{" ".join(map(str, box))}"/>'
        for name, box in VIEWS.items()
    )
    prefix, suffix = source.rsplit("</svg>", 1)
    result = prefix + views + "\n</svg>" + suffix
    ET.fromstring(result)
    return result


def hero_markup(revision):
    base = f"https://raw.githubusercontent.com/Ekin-Kahraman/Ekin-Kahraman/{revision}/assets/profile/"

    def picture(name, width):
        alt = ""
        if name == "top":
            alt = "A visitor exploring Ekin Kahraman’s GitHub profile and LinkedIn at a pixel-art workstation."
        elif name == "linkedin":
            alt = "Open Ekin Kahraman’s LinkedIn profile"
        fragment = f"#workstation-{name}"
        return (
            '<picture><source media="(prefers-reduced-motion: reduce)" '
            f'srcset="{base}workstation-linked-still.svg{fragment}">'
            f'<img src="{base}workstation-linked.svg{fragment}" '
            f'width="{width}" align="top" alt="{alt}"></picture>'
        )

    middle = (
        picture("left", "78.5410334346%")
        + '<a href="https://www.linkedin.com/in/ekinka" title="Open LinkedIn profile">'
        + picture("linkedin", "12.7659574468%")
        + "</a>"
        + picture("right", "8.6930091185%")
    )
    # GitHub strips layout CSS. These supported elements provide a centered,
    # responsive inline block, no list marker, and a line strut shorter than
    # the narrow URL strip. Keep image tags adjacent to avoid whitespace seams.
    return (
        START + '\n<div align="center"><sup><sub><sup><sub><li type="none"><summary><h6>'
        + picture("top", "700") + "<br>" + middle + "<br>"
        + picture("bottom", "700")
        + "</h6></summary></li></sub></sup></sub></sup></div>\n" + END
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pin-readme", metavar="REVISION")
    args = parser.parse_args()
    for source, target in (
        ("workstation.svg", "workstation-linked.svg"),
        ("workstation-still.svg", "workstation-linked-still.svg"),
    ):
        (ASSETS / target).write_text(linked_artwork((ASSETS / source).read_text()))
    if args.pin_readme:
        path = ROOT / "README.md"
        readme = path.read_text()
        if START in readme:
            pattern = re.escape(START) + r".*?" + re.escape(END)
        else:
            pattern = r'\A<p align="center">.*?</p>'
        readme, count = re.subn(pattern, lambda _: hero_markup(args.pin_readme), readme, count=1, flags=re.S)
        assert count == 1, "Could not find the workstation hero"
        path.write_text(readme)
    print("Prepared workstation views; only the laptop URL receives a LinkedIn link.")


if __name__ == "__main__":
    main()
