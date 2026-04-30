### Ekin Kahraman

I build pipelines that find things in genomics data — then build systems that act on what they find.

---

**What I've found**

[1,773 DE genes](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) during SARS-CoV-2 infection ([Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)). A condition-by-sex model identifies 12 sex-biased genes; full-cohort sensitivity analysis (n = 484) preserves 99.8% of effect directions.

[Which cells are responsible?](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) PyTorch deconvolution of 484 bulk samples into 14 airway cell types. 11 of 14 significantly change — basal/ciliated depleted, goblet-lineage and T cells expanded. Pseudo-bulk validation r = 0.954 (overestimates real-bulk; partial external replication on GSE163151).

[5 immune cell types](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) in PBMC 3k — Leiden clustering, T cell subclustering (CD4⁺/CD8⁺), PAGA trajectory.

**What I've built**

[rustscenic](https://github.com/Ekin-Kahraman/rustscenic) — Rust + PyO3 rewrite of SCENIC+. 200k cells end-to-end in 17 min at 7.4 GB (~5.4× less memory than scenicplus). Real PBMC multiome E2E proven. Pip install, no Java/dask/CUDA. Active collaboration with the Huang Lab (Mount Sinai).

[Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) — FASTQ to DE results in 7 containerised steps. Docker, Singularity, CI.

[SafetyNett](https://github.com/Ekin-Kahraman/safetynett) — AI safety netting for NHS GPs. 39 conditions. Built in 2.5 hours at the OpenClaw Clinical Hackathon. [Live.](https://safetynett.lovable.app)

---

7 merged pull requests to the [scverse](https://scverse.org) ecosystem ([scanpy](https://github.com/scverse/scanpy), [PyDESeq2](https://github.com/scverse/PyDESeq2)). In design discussion with the [anndata](https://github.com/scverse/anndata) maintainer on a `concat()` API extension.

Molecular Biology & Genetics, UEA. Volunteer in the [Grieshop Lab](https://github.com/karlgrieshop) (evolutionary genetics).

ekinkhrmn@outlook.com
