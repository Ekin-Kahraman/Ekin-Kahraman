### Ekin Kahraman

I build computational biology software for single-cell genomics, gene regulation, and reproducible analysis.

**Current focus**

[rustscenic](https://github.com/Ekin-Kahraman/rustscenic): Rust + PyO3 rewrite of SCENIC/SCENIC+ for faster, lower-memory regulatory network analysis.

- End-to-end multiome pipeline: GRN, AUCell, topics, cisTarget, enhancer links, eRegulons
- Real PBMC multiome: 2,767 cells, 1,091 eRegulons, 451 s, 3.67 GB peak RSS
- Mouse brain E18 multiome: 4,770 cells, 1,125 eRegulons, 826 s, 4.01 GB peak RSS, 9/9 expected cortex TFs recovered
- PBMC GRN vs pinned arboreto reference: 1.78x faster wall time, 0.611 shared-edge Spearman
- Collaborating with researchers at the Huang Lab, Mount Sinai, on biological validation

**Selected work**

- [scverse](https://scverse.org): 7 merged PRs across [scanpy](https://github.com/scverse/scanpy) and [PyDESeq2](https://github.com/scverse/PyDESeq2); open AnnData concat API PR
- [Bulk RNA-seq differential expression](https://github.com/Ekin-Kahraman/bulk-rnaseq-differential-expression): SARS-CoV-2 airway analysis, 1,773 DE genes, n = 484 sensitivity analysis, [Zenodo DOI](https://doi.org/10.5281/zenodo.19429954)
- [Airway cell-type deconvolution](https://github.com/Ekin-Kahraman/covid-airway-deconvolution): PyTorch deconvolution of 484 bulk RNA-seq samples into 14 airway cell types, pseudo-bulk validation r = 0.954
- [Single-cell RNA-seq immune profiling](https://github.com/Ekin-Kahraman/single-cell-rnaseq-immune-profiling): PBMC 3k clustering, T cell subclustering, marker annotation, PAGA trajectory
- [Nextflow RNA-seq pipeline](https://github.com/Ekin-Kahraman/rnaseq-nextflow-pipeline): FASTQ to differential expression results in 7 containerised steps
- [SafetyNett](https://github.com/Ekin-Kahraman/safetynett): AI safety-netting prototype for NHS GP workflows, built at the OpenClaw Clinical Hackathon, [live](https://safetynett.lovable.app)

Research volunteer in the [Grieshop Lab](https://github.com/karlgrieshop), working around evolutionary genetics.

evk23umu@uea.ac.uk
