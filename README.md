# Ekin Kahraman

Building [rustscenic](https://github.com/Ekin-Kahraman/rustscenic), a Rust + PyO3 rewrite of SCENIC+, in collaboration with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) at Icahn Mount Sinai.

The standard SCENIC+ pipeline has 40+ Python dependencies and multi-hour runtimes on 100k cells. rustscenic matches it at:

- **88× faster AUCell** vs pyscenic
- **6× less memory** at 100k cells (6.3 GB vs >40 GB)
- **5 runtime dependencies** (numpy, pandas, pyarrow, scipy, anndata)
- **9/9 canonical cortex TFs recovered** on mouse brain E18 multiome

[v0.4.0 release](https://github.com/Ekin-Kahraman/rustscenic/releases/tag/v0.4.0) · v0.3.x measurements · [v0.4.x cross-dataset sweep underway](https://github.com/Ekin-Kahraman/rustscenic/blob/main/docs/v0.4.x-benchmark-plan.md)

## Other work

- **7 merged scverse PRs** across [scanpy](https://github.com/scverse/scanpy) and [PyDESeq2](https://github.com/scverse/PyDESeq2); open [AnnData concat API PR](https://github.com/scverse/anndata/pull/2416)
- **1,773 DE genes** ([Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)): DESeq2 on SARS-CoV-2 nasopharyngeal RNA-seq, n = 60 + 484 sensitivity ([repo](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression))
- **r = 0.954 on pseudo-bulk 5-fold CV**: PyTorch deconvolution into 14 airway cell types ([repo](https://github.com/Ekin-Kahraman/covid-airway-deconvolution))

evk23umu@uea.ac.uk
