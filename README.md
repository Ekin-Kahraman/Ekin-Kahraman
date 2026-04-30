### Ekin Kahraman

I build pipelines that find things in genomics data — then build systems that act on what they find.

---

**What I've found**

[1,773 genes](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) change expression during SARS-CoV-2 infection. A formal condition-by-sex model finds 12 genes with sex-differential host response, and the full 484-sample cohort preserves 99.8% of shared effect directions.

[Which cells are responsible?](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) A PyTorch deconvolution model trained on tissue-matched single-cell data decomposes 484 bulk samples into 14 airway cell types. Ciliated and basal cells are depleted; goblet-lineage cells, T cells, macrophages and dendritic cells expand. 11 cell types significantly change; pseudo-bulk validation r = 0.954.

[5 immune cell types](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) in 2,604 PBMCs — subclustered T cells to split CD4⁺/CD8⁺ that standard resolution misses.

**What I've built**

[rustscenic](https://github.com/Ekin-Kahraman/rustscenic) — Rust + PyO3 rewrite of SCENIC+. 200k cells in 17 min at 7.4 GB (~5.4× less memory than scenicplus); pip install with no Java/dask/CUDA. Active collaboration with the Huang Lab (Mount Sinai).

[Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) — FASTQ to DE results in 7 containerised steps. Docker, Singularity, CI.

[SafetyNett](https://github.com/Ekin-Kahraman/safetynett) — AI safety netting for NHS GPs. 39 conditions. Built in 2.5 hours. [Live.](https://safetynett.lovable.app)

---

7 merged pull requests to the [scverse](https://scverse.org) ecosystem ([scanpy](https://github.com/scverse/scanpy), [PyDESeq2](https://github.com/scverse/PyDESeq2)).

Molecular Biology & Genetics, UEA. Volunteer in the [Grieshop Lab](https://github.com/karlgrieshop) (evolutionary genetics).

ekinkhrmn@outlook.com
