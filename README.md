# Ekin Kahraman

Computational biology and bioinformatics, focused on single-cell genomics and gene regulation.

I analyse gene expression data and build research software in Python, R, and Rust.
I created and maintain RustScenic, alongside projects in differential expression,
cell-type analysis, and reproducible RNA-seq workflows.

## RustScenic

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic) ([releases](https://github.com/Ekin-Kahraman/rustscenic/releases), [PyPI](https://pypi.org/project/rustscenic/), [docs](https://ekin-kahraman.github.io/rustscenic/), [Zenodo DOI](https://doi.org/10.5281/zenodo.20246040)): a toolkit for studying gene regulation using single-cell RNA and chromatin-accessibility data.

Developed in collaboration with the [Kuan-Lin Huang Lab](https://profiles.icahn.mssm.edu/kuan-lin-huang)
at the Icahn School of Medicine at Mount Sinai.

- [Gene-network inference on 1.3 million mouse-brain cells](https://github.com/Ekin-Kahraman/rustscenic/blob/0c8eb00539e3860c78e452c8661cc2735c169386/validation/scaling/IFB_REAL_RNA_GRN_2026-08-28.md) in under 47 minutes, with `4.28 GB` peak memory during analysis on 16 CPU cores.
- [`3.3x` faster with about `81%` less peak physical memory than arboreto](https://github.com/Ekin-Kahraman/rustscenic/blob/0c8eb00539e3860c78e452c8661cc2735c169386/validation/scaling/IFB_REAL_RNA_GRN_2026-08-28.md), using the same hardware and 20,000-cell input for gene-network inference.
- Available as a Python package for Linux, macOS, and Windows, with automated tests and documented workflows: `pip install rustscenic`.

These benchmarks use the v0.5.0 release candidate.
The million-cell run used prepared RNA data and 2,095 selected genes; preparing
the full dataset separately peaked at `71.49 GB`. Linked benchmarks record the
workload, hardware, and validation scope.

## Stack

- Analysis: Python, R, Scanpy, AnnData, DESeq2, PyTorch
- Research software: Rust, PyO3, NumPy, SciPy, pandas
- Workflows: Nextflow, Docker, Singularity, GitHub Actions

## Selected work

| Project | Stack | Evidence |
| --- | --- | --- |
| [RustScenic airway case study](https://github.com/Ekin-Kahraman/rustscenic-airway-case) | Python, RustScenic, pySCENIC | Explored gene-regulation differences in COVID-19 airway data; activity scores agreed closely with pySCENIC across 31,602 cells (mean per-cell Pearson r = 0.984). [DOI](https://doi.org/10.5281/zenodo.20230540) |
| [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) | R, DESeq2, clusterProfiler | Identified an interferon-related COVID-19 host-response signature; checked effect estimates against the full cohort. [DOI](https://doi.org/10.5281/zenodo.19429954) |
| [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) | Python, PyTorch | Estimated proportions of 14 airway cell types in 484 samples; cross-validation on simulated mixtures gave r = 0.954. |
| [Single-cell immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) | Python, Scanpy, Scrublet | Identified immune-cell populations and examined T-cell subtypes in blood single-cell data, with quality control and reproducible outputs. |
| [RNA-seq Nextflow pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) | Nextflow, Docker, Singularity, AWS Batch | Takes raw sequencing reads through quality control to differential expression and reports, with automated end-to-end tests on synthetic data. |
| External open-source contributions | Scanpy, PyDESeq2, AnnData | 5 merged contributions to [Scanpy](https://github.com/scverse/scanpy), 2 to [PyDESeq2](https://github.com/scverse/PyDESeq2), plus an open [AnnData contribution](https://github.com/scverse/anndata/pull/2416). |
| [SafetyNett](https://github.com/Ekin-Kahraman/safetynett) | React, TypeScript, Supabase | Hackathon prototype for patient follow-up and clinician alerts, with automated tests; not a deployed clinical device. |

## Contact

evk23umu@uea.ac.uk
