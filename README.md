# Ekin Kahraman

I build computational biology software for single-cell genomics and gene regulation.

## Current focus

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic): Rust + PyO3 rewrite of SCENIC/SCENIC+ for single-cell regulatory network analysis. End-to-end multiome pipeline: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons.

Head-to-head vs reference implementations on identical input, same hardware:

- **AUCell 88× faster** than pyscenic at per-cell Pearson 0.99 (0.21 s vs 18.6 s on 10x Multiome, 10k cells × 1,457 regulons)
- **GRN 1.78× faster** than pinned arboreto 0.1.6 on PBMC (per-TF Spearman 0.63)
- **~6.3× less memory** at 100k cells × 20k genes × 4 stages (6.3 GB vs >40 GB reported for scenicplus)
- **5 runtime dependencies** (numpy, pandas, pyarrow, scipy, anndata) vs 40+ for the reference stack
- Biological validation: 9/9 expected cortex TFs recovered on mouse brain E18 multiome; collaboration with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) (Precision Omics, Icahn Mount Sinai)

## Selected work

- [scverse](https://scverse.org): 7 merged PRs across [scanpy](https://github.com/scverse/scanpy) and [PyDESeq2](https://github.com/scverse/PyDESeq2); open [AnnData concat API PR](https://github.com/scverse/anndata/pull/2416)
- [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression): DESeq2 on SARS-CoV-2 nasopharyngeal RNA-seq: 1,773 DE genes (n = 60 primary, 99.8% concordant with n = 484 sensitivity), [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)
- [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution): PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types; r = 0.954 on pseudo-bulk 5-fold CV (upper bound, no batch effects)
- [Single-cell RNA-seq immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling): scanpy pipeline on PBMC 3k, end-to-end in 17 s; multi-resolution Leiden, automated marker annotation, T-cell subclustering, PAGA, tests + CI
- [Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline): FASTQ to differential expression results in 7 containerised steps
- [SafetyNett](https://github.com/Ekin-Kahraman/safetynett): AI safety-netting prototype for NHS GP workflows, built at the OpenClaw Clinical Hackathon ([live](https://safetynett.lovable.app))

evk23umu@uea.ac.uk
