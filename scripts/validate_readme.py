"""Validate the profile README keeps the portfolio evidence surfaced."""

from __future__ import annotations

import re
from pathlib import Path


README = Path("README.md")


def main() -> None:
    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines[:3] != [
        "# Ekin Kahraman",
        "",
        "Rust/Python software engineer building scientific software and data systems for computational biology.",
    ]:
        raise AssertionError("unexpected profile name or headline")

    concept_doi = "https://doi.org/10.5281/zenodo.20246040"
    if concept_doi not in text:
        raise AssertionError("missing RustScenic Zenodo concept DOI")
    if "https://doi.org/10.5281/zenodo.20246041" in text:
        raise AssertionError("RustScenic profile must not pin the v0.4.5 Zenodo record DOI")

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
