"""Validate the profile README keeps the portfolio evidence surfaced."""

from __future__ import annotations

import re
from pathlib import Path


README = Path("README.md")


def main() -> None:
    text = README.read_text(encoding="utf-8")
    required_repos = [
        "rustscenic",
        "rnaseq-nextflow-pipeline",
        "bulk-rnaseq-differential-expression",
        "covid-airway-deconvolution",
        "single-cell-rnaseq-immune-profiling",
        "safetynett",
    ]
    for repo in required_repos:
        needle = f"https://github.com/Ekin-Kahraman/{repo}"
        if needle not in text:
            raise AssertionError(f"missing portfolio link: {repo}")

    required_terms = [
        "Kuan-lin Huang Lab",
        "PyPI",
        "AWS Batch",
        "Zenodo DOI",
        "model metadata",
        "full-pipeline CI",
        "TypeScript checking",
    ]
    for term in required_terms:
        if term not in text:
            raise AssertionError(f"missing evidence term: {term}")

    emails = re.findall(r"[\w.+-]+@[\w.-]+", text)
    if emails != ["evk23umu@uea.ac.uk"]:
        raise AssertionError("unexpected profile email state")


if __name__ == "__main__":
    main()
