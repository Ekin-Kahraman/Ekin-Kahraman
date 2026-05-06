# Ekin Kahraman

Building [rustscenic](https://github.com/Ekin-Kahraman/rustscenic), a Rust + PyO3 rewrite of SCENIC+, in collaboration with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) at Icahn Mount Sinai.

[v0.4.0](https://github.com/Ekin-Kahraman/rustscenic/releases/tag/v0.4.0) covers the full SCENIC+ pipeline: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons.

Benchmarks vs the reference Python stack on identical input (v0.3.x measurements; [v0.4.x cross-dataset sweep underway](https://github.com/Ekin-Kahraman/rustscenic/blob/main/docs/v0.4.x-benchmark-plan.md)):

- **AUCell 88× faster** than pyscenic at per-cell Pearson 0.99 (0.21 s vs 18.6 s on 10x Multiome, 10k cells × 1,457 regulons)
- **GRN 1.78× faster** than pinned arboreto 0.1.6 on PBMC (per-TF Spearman 0.63)
- **~6.3× less memory** at 100k cells × 20k genes × 4 stages (6.3 GB vs >40 GB reported for scenicplus)
- **5 runtime dependencies** (numpy, pandas, pyarrow, scipy, anndata) vs 40+ for the reference stack
- **9/9 canonical cortex TFs recovered** on mouse brain E18 multiome (biological validation)

## Selected work

- **7 merged scverse PRs** across [scanpy](https://github.com/scverse/scanpy) and [PyDESeq2](https://github.com/scverse/PyDESeq2); open [AnnData concat API PR](https://github.com/scverse/anndata/pull/2416)
- **1,773 DE genes** ([Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)): DESeq2 on SARS-CoV-2 nasopharyngeal RNA-seq, n = 60 primary, 99.8% concordant with n = 484 sensitivity ([repo](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression))
- **r = 0.954 on pseudo-bulk 5-fold CV**: PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types, upper bound with no batch effects ([repo](https://github.com/Ekin-Kahraman/covid-airway-deconvolution))

evk23umu@uea.ac.uk
