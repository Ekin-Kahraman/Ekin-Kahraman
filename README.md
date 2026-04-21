### Ekin Kahraman

I build pipelines that find things in genomics data — then build systems that act on what they find.

---

**What I've found**

[1,773 genes](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression) change expression during SARS-CoV-2 infection. 12 do so differently in men vs women. Nobody had tested for that interaction in the original study.

[Which cells are responsible?](https://github.com/Ekin-Kahraman/covid-airway-deconvolution) A PyTorch neural network trained on tissue-matched single-cell data decomposes 484 bulk samples into 14 airway cell types. Basal stem cells are depleted. Goblet cells expand. Immune cells infiltrate. 10 cell types significantly changed (r = 0.954). First tissue-matched deconvolution of this dataset.

[5 immune cell types](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling) in 2,604 PBMCs — subclustered T cells to split CD4⁺/CD8⁺ that standard resolution misses.

**What I've built**

[rustscenic](https://github.com/Ekin-Kahraman/rustscenic) — Rust + PyO3 rewrite of the four slow SCENIC+ single-cell regulatory-network stages. Installs where arboreto + pyscenic no longer do. 27–90× faster per-cell scoring, 6 GB vs 40+ GB memory at 100k cells, 0.98 per-cell correlation with pyscenic on the Ziegler 31k airway atlas. Active remote collaboration with the Huang Lab (Mount Sinai).

[Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline) — FASTQ to DE results in 7 containerised steps. Docker, Singularity, CI.

[SafetyNett](https://github.com/Ekin-Kahraman/safetynett) — AI safety netting for NHS GPs. 39 conditions. Built in 2.5 hours. [Live.](https://safetynett.lovable.app)

---

7 merged pull requests to the [scverse](https://scverse.org) ecosystem ([scanpy](https://github.com/scverse/scanpy), [PyDESeq2](https://github.com/scverse/PyDESeq2)); [muon](https://github.com/scverse/muon) PR open.

Molecular Biology & Genetics, UEA. Volunteer in the [Grieshop Lab](https://github.com/karlgrieshop) (evolutionary genetics).

ekinkhrmn@outlook.com
