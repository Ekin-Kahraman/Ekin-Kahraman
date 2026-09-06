"""Validate the profile README keeps biological evidence and scope surfaced."""

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
        "Computational biology and bioinformatics, focused on single-cell genomics and gene regulation.",
    ]:
        raise AssertionError("unexpected profile name or headline")

    concept_doi = "https://doi.org/10.5281/zenodo.20246040"
    if concept_doi not in text:
        raise AssertionError("missing RustScenic Zenodo concept DOI")
    if "https://doi.org/10.5281/zenodo.20246041" in text:
        raise AssertionError("RustScenic profile must not pin the v0.4.5 Zenodo record DOI")

    required_repos = [
        "rustscenic",
        "rustscenic-airway-case",
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
        "Kuan-Lin Huang Lab",
        "PyPI",
        "AWS Batch",
        "Zenodo DOI",
        "Python, R, and Rust",
        "1.3 million mouse-brain cells",
        "during analysis",
        "20,000-cell input",
        "2,095 selected genes",
        "71.49 GB",
        "interferon-related",
        "simulated mixtures",
        "synthetic data",
        "not a deployed clinical device",
        "I created and maintain",
        "https://github.com/Ekin-Kahraman/rustscenic/releases)",
        "v0.5.0 release candidate",
        "Icahn School of Medicine at Mount Sinai",
    ]
    for term in required_terms:
        if term not in text:
            raise AssertionError(f"missing evidence term: {term}")

    if "/releases/tag/v0.5.0" in text or "/blob/v0.5.0/" in text:
        raise AssertionError("profile must not link to the unpublished v0.5.0 tag")

    emails = re.findall(r"[\w.+-]+@[\w.-]+", text)
    if emails != ["evk23umu@uea.ac.uk"]:
        raise AssertionError("unexpected profile email state")


if __name__ == "__main__":
    main()
