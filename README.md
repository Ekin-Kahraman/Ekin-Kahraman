# Ekin Kahraman

Computational biology + scientific software: Rust/Python tooling, RNA-seq workflows, single-cell analysis, and deployable clinical/product prototypes.

## Currently building

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic) ([v0.4.5](https://github.com/Ekin-Kahraman/rustscenic/releases/tag/v0.4.5), [PyPI](https://pypi.org/project/rustscenic/), [docs](https://ekin-kahraman.github.io/rustscenic/), [Zenodo DOI](https://doi.org/10.5281/zenodo.20246041)): turning fragile SCENIC/SCENIC+ regulatory-network workflows into installable, CPU-efficient Rust + PyO3 software, built in collaboration with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) at Icahn Mount Sinai.

Legacy SCENIC stacks need Java, dask, and a long chain of transitive packages that frequently break on current Python; rustscenic ships the practical compute path without them.

- `pip install rustscenic`; Python 3.10 to 3.13; Linux, macOS, and Windows wheels
- Five runtime dependencies: numpy, pandas, pyarrow, scipy, anndata
- Core stages in one package: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons
- Live docs, Zenodo DOI, typed wheels, and branch-protected CI across Rust, Python, docs, and optional extras
- End-to-end multiome validated on human PBMC and mouse brain E18; stage-level checks across airway, melanoma, and dopaminergic-neuron datasets

## Selected work

- [RNA-seq Nextflow pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline): containerised DSL2 workflow for FASTQ -> QC -> trimming -> HISAT2 -> featureCounts -> DESeq2 -> MultiQC, with Docker/Singularity/AWS Batch profiles, Seqera-ready schema, run reports/traces, and synthetic end-to-end CI.
- [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression): DESeq2 on SARS-CoV-2 nasopharyngeal RNA-seq, 1,773 DE genes (n = 60 primary, 99.8% concordant with n = 484 sensitivity), tracked output manifest, full rebuild CI, and [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954).
- [RustScenic airway validation case study](https://github.com/Ekin-Kahraman/rustscenic-airway-case): real-atlas head-to-head against pySCENIC on 31,602 airway cells and 59 regulons, mean per-cell Pearson r = 0.984, 27x AUCell timing difference, CI-tested reference smoke, and [Zenodo DOI](https://doi.org/10.5281/zenodo.20230540).
- [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution): PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types, r = 0.954 on pseudo-bulk 5-fold CV (upper bound), synthetic smoke tests, and model metadata for HVG/cell-type reuse.
- [Single-cell immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling): Scanpy PBMC pipeline with Scrublet QC, Leiden resolution selection, marker-based annotation, PAGA trajectory inference, T-cell subclustering, full-pipeline CI smoke validation, and generated output checksums.
- [SafetyNett](https://github.com/Ekin-Kahraman/safetynett): React/TypeScript + Supabase clinical safety-netting prototype from the OpenClaw Clinical Hackathon; CI covers lint, explicit TypeScript checking, production build, and tests.
- scverse: 4 doc improvements to [scanpy](https://github.com/scverse/scanpy) plotting, fix to [PyDESeq2](https://github.com/scverse/PyDESeq2) dataframe handling, open algorithmic PR on [AnnData `concat` API](https://github.com/scverse/anndata/pull/2416).

evk23umu@uea.ac.uk
