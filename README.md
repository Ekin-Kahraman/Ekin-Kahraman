# Ekin Kahraman

Rust/Python software engineer building scientific software and data systems for computational biology.

I ship installable bioinformatics packages, reproducible pipelines, and clinical software prototypes with CI, real-data validation, and published artefacts.

## RustScenic

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic) ([v0.4.7](https://github.com/Ekin-Kahraman/rustscenic/releases/tag/v0.4.7), [PyPI](https://pypi.org/project/rustscenic/), [docs](https://ekin-kahraman.github.io/rustscenic/), [Zenodo DOI](https://doi.org/10.5281/zenodo.20246040)): faster, lower-overhead regulatory-network analysis for single-cell and multiome data, shipped as one Python package with Rust kernels.

- [`11x` to `52x` faster](https://ekin-kahraman.github.io/rustscenic/benchmarks/#setup) than SCENIC+ on tested real-data core E2E rows; sampled inputs on one machine, median speedup `27x`
- Historical RustScenic `v0.3.2` synthetic 100k-cell seven-stage scale check peaked at `7.09 GB` RSS; a `v0.5.0` rerun is still required
- One install: `pip install rustscenic`; Python 3.10 to 3.13; Linux, macOS, and Windows wheels
- Core install avoids Java, dask, CUDA, and Snakemake
- Rust + PyO3 stages: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons
- Evidence: [benchmarks](https://ekin-kahraman.github.io/rustscenic/benchmarks/), PyPI, docs, Zenodo DOI, branch-protected CI, committed validation artefacts
- Built with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) at Icahn Mount Sinai

## Stack

- Core: Rust, PyO3, Python, pandas, numpy, scipy, scanpy, anndata
- Pipelines: Nextflow DSL2, Docker, Singularity, GitHub Actions
- Applications: PyTorch, React, TypeScript, Supabase

## Selected work

| Project | Stack | Evidence |
| --- | --- | --- |
| [RustScenic airway validation case study](https://github.com/Ekin-Kahraman/rustscenic-airway-case) | Python, pySCENIC comparison, CI | Real-atlas head-to-head on 31,602 airway cells and 59 regulons; mean per-cell Pearson r = 0.984; 27x AUCell timing difference; [Zenodo DOI](https://doi.org/10.5281/zenodo.20230540) |
| External open-source contributions | scverse scientific Python ecosystem | 5 merged PRs to [scanpy](https://github.com/scverse/scanpy), 2 merged PRs to [PyDESeq2](https://github.com/scverse/PyDESeq2), and open algorithmic PR on [AnnData `concat` API](https://github.com/scverse/anndata/pull/2416) |
| [RNA-seq Nextflow pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) | Nextflow DSL2, Docker, Singularity, AWS Batch | FASTQ to QC, trimming, HISAT2, featureCounts, DESeq2, and MultiQC; Seqera-ready schema; synthetic end-to-end CI |
| [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) | R, DESeq2, CI, reproducible artefacts | SARS-CoV-2 nasopharyngeal RNA-seq; 1,773 DE genes in primary cohort; 99.8% concordance with larger sensitivity set; [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954) |
| [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) | PyTorch, single-cell references, pseudo-bulk validation | Deconvolution of 484 bulk RNA-seq samples into 14 airway cell types; r = 0.954 on pseudo-bulk 5-fold CV; model metadata for reuse |
| [Single-cell immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) | Scanpy, Scrublet, Leiden, PAGA, CI | PBMC pipeline with QC, marker annotation, trajectory inference, T-cell subclustering, full-pipeline CI smoke validation, and output checksums |
| [SafetyNett](https://github.com/Ekin-Kahraman/safetynett) | React, TypeScript, Supabase | Clinical safety-netting prototype; CI covers lint, explicit TypeScript checking, production build, and tests |

## Contact

evk23umu@uea.ac.uk
