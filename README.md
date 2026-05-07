# Ekin Kahraman

Computational biology + scientific software: RNA-seq, single-cell analysis, and Rust/Python tooling.

## Currently building

[**rustscenic**](https://github.com/Ekin-Kahraman/rustscenic) ([v0.4.1](https://github.com/Ekin-Kahraman/rustscenic/releases/tag/v0.4.1), [PyPI](https://pypi.org/project/rustscenic/)): rewriting fragile SCENIC/SCENIC+ regulatory-network workflows as installable, CPU-efficient Rust + PyO3 software, built in collaboration with the [Kuan-lin Huang Lab](https://icahn.mssm.edu/profiles/kuan-lin-huang) at Icahn Mount Sinai.

- One install: `pip install rustscenic`
- Python 3.10–3.13; Linux/macOS wheels for x86_64 and aarch64
- Five runtime dependencies: numpy, pandas, pyarrow, scipy, anndata
- Core stages in one package: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons
- End-to-end multiome validated on human PBMC and mouse brain E18; stage-level checks across airway, melanoma, and dopaminergic-neuron datasets

## Selected work

- scverse: 4 doc improvements to [scanpy](https://github.com/scverse/scanpy) plotting, fix to [PyDESeq2](https://github.com/scverse/PyDESeq2) dataframe handling, open algorithmic PR on [AnnData `concat` API](https://github.com/scverse/anndata/pull/2416)
- [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression): DESeq2 on SARS-CoV-2 nasopharyngeal RNA-seq, 1,773 DE genes (n = 60 primary, 99.8% concordant with n = 484 sensitivity), [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)
- [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution): PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types, r = 0.954 on pseudo-bulk 5-fold CV (upper bound, no batch effects)

evk23umu@uea.ac.uk
