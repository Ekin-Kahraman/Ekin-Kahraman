# Ekin Kahraman

I build computational biology software for single-cell genomics, gene regulation, and reproducible analysis.

## Current focus

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic): Rust + PyO3 rewrite of SCENIC/SCENIC+ for faster, lower-memory regulatory network analysis.

End-to-end multiome pipeline: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons.

| Dataset | Cells | eRegulons | Wall | Peak RSS |
|:---|---:|---:|---:|---:|
| PBMC multiome (v0.3.9) | 2,767 | 1,091 | 451 s | 3.67 GB |
| Mouse brain E18 (v0.3.10) | 4,770 | 1,125 | 826 s | 4.01 GB |

PBMC GRN vs pinned arboreto 0.1.6: **1.78× faster**, per-TF Spearman 0.63, top-50 Jaccard 0.39. Mouse brain: 9/9 expected cortex TFs recovered.

Biological validation with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) (Precision Omics, Icahn Mount Sinai).

## Selected work

- [scverse](https://scverse.org): 7 merged PRs across [scanpy](https://github.com/scverse/scanpy) and [PyDESeq2](https://github.com/scverse/PyDESeq2); open [AnnData concat API PR](https://github.com/scverse/anndata/pull/2416)
- [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression): SARS-CoV-2 airway analysis, 1,773 DE genes, n = 484 sensitivity analysis, [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)
- [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution): PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types; pseudo-bulk 5-fold CV r = 0.954 (upper bound, no batch effects in validation)
- [Single-cell RNA-seq immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling): scanpy pipeline on PBMC 3k, end-to-end in 17 s; multi-resolution Leiden, automated marker annotation, T-cell subclustering, PAGA, tests + CI
- [Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline): FASTQ to differential expression results in 7 containerised steps
- [SafetyNett](https://github.com/Ekin-Kahraman/safetynett): AI safety-netting prototype for NHS GP workflows, built at the OpenClaw Clinical Hackathon ([live](https://safetynett.lovable.app))

evk23umu@uea.ac.uk
