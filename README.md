# Ekin Kahraman

I rebuild scientific Python in Rust where it stops fitting in memory.

**Looking for:** summer 2026 research placement (UK / EU / remote) · PhD entry 2027 (comp-bio, single-cell ML).

---

**Performance engineering**

[rustscenic](https://github.com/Ekin-Kahraman/rustscenic) — Rust + PyO3 reimplementation of the full SCENIC+ pipeline (González-Blas et al., *Nat. Methods* 2024): GRN, AUCell, topics, cistarget, peak calling, enhancer→gene, eRegulon assembly. Installs and runs where `arboreto + pyscenic + pycisTopic` no longer do. **5.4× lower memory** than the reference stack at comparable scale. 200k-cell atlas E2E in 17 min @ 7.4 GB RSS. Parallel collapsed-Gibbs LDA delivers 2.7× higher topic coherence than VB at K=30. v0.3.3, MIT, 135 Python + 57 Rust tests.

```
pip install git+https://github.com/Ekin-Kahraman/rustscenic@v0.3.3
```

**ML methodology**

[covid-airway-deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) — PyTorch ensemble deconvolving 484 bulk COVID NP samples into 14 airway cell types using tissue-matched Ziegler 2021 scRNA-seq reference. Pseudo-bulk training with prevalence-weighted Dirichlet sampling, noise augmentation (gene dropout, library size, Gaussian), KL divergence loss for simplex-constrained output. Ensemble 5-fold CV r = 0.954 vs NNLS baseline r = 0.609. External validation on GSE163151 (404 independent samples): 8/14 cell types replicate direction.

**Statistical genomics**

[bulk-rnaseq-differential-expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) — DESeq2 with `~ condition + gender` covariate model on GSE152075 (484 samples, Lieberman et al. 2020). 1,773 DE genes, 12 sex-biased, 99.8% concordance with the published result. Reproducibility-tested via GitHub Actions on every commit. [Zenodo DOI 10.5281/zenodo.19429954](https://doi.org/10.5281/zenodo.19429954). v2.1.0.

**Single-cell analysis**

[single-cell-rnaseq-immune-profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) — 8-step scanpy pipeline on 2,604 PBMCs (10x Genomics 3k). Leiden clustering at multiple resolutions, CD4⁺/CD8⁺ T-cell subclustering, PAGA trajectory inference, Scrublet doublet detection, marker-gene-driven manual annotation across 5 cell types. Containerised, CI-tested.

**Workflow engineering**

[rnaseq-nextflow-pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) — Nextflow DSL2, 7 processes (FastQC → trimming → HISAT2 → featureCounts → DESeq2 → reports). Docker + Singularity profiles, GitHub Actions CI on every commit. Designed for HPC deployment (Slurm-compatible).

---

**Open source.** 7 merged pull requests to the [scverse](https://scverse.org) ecosystem ([scanpy](https://github.com/scverse/scanpy), [PyDESeq2](https://github.com/scverse/PyDESeq2)). Co-designing `aligned_axis_key_join` for `ad.concat()` with [anndata](https://github.com/scverse/anndata) core maintainer ([#2374](https://github.com/scverse/anndata/issues/2374)).

**Affiliations.**
[Huang Lab, Mount Sinai](https://labs.icahn.mssm.edu/huanglab/) — remote collaborator (Apr 2026 –). Rust reimplementations of single-cell tooling.
[Grieshop Lab, UEA](https://github.com/karlgrieshop) — research assistant (Mar 2026 –). Sex-biased gene expression in bulk RNA-seq.

**Currently.** rustscenic real-PBMC E2E shipping in v0.3.4. Mouse motif rankings + pySCENIC migration tutorial next.

**Education.** BSc Molecular Biology & Genetics, University of East Anglia (2024–2027).

evk23umu@uea.ac.uk
