# Cytokine dependent time couse analysis

Histone deacetylases (HDACs) have been shown to play significant roles in melanoma signaling pathways. Precisely, HDAC6 controls certain immunomodulatory functions, including antigen presentation and cytokine stimulation. Among those cytokines, interferon-gamma (IFNγ) and interleukin-6 (IL-6) showed modulatory effects in melanoma through various signaling pathways in a time-dependent manner. The dual role of HDAC6 and cytokine stimulation allows investigation of the impact of HDAC6 on the expression pattern of melanoma-related genes.

## Methods and Analysis

Bulk RNA sequencing of human WM164 Non-Target and WM164 HDAC6 Knockdown was performed from collected RNA at 8 distinct time points (0,1,2,4,6,8,12, and 24 hours) after IL6 and IFNγ stimulation. RNA expression at each time point was obtained by alignment-based counts using a HISAT2-StringTie pipeline. Differential expression between knockdown and non-target with NOISeq algorithm provided fold changes to generate clusters based on their expression pattern. [Graphia](https://github.com/graphia-app/graphia) software clustering threshold (gene-to-gene comparison in the RNA-seq atlas, Pearson’s r < 0.8, and Markov clustering (MCL) algorithm was used to construct a network graph with an inflation value of 1.8). Functional analysis was performed through Gene Set Enrichment Analysis (GSEA).


## Results 
70 clusters were generated and mapped to various pathway analyses. Upon HDAC6 knockdown followed by IL6 and IFNγ, respectively, 37 clusters and 33 clusters were generated, showing various patterns of expression associated with immune-related responses as well as metabolic pathways at specific time points. These clusters also show a pattern of interaction with transcription factors, targeting HDAC6, that modulate immune pathways such as p53 and Wnt-beta catenin signaling. Additionally, significant sets of genes have been shown to regulate PD-L1 checkpoint and JAK-STAT signaling pathways upon HDAC6 knockdown and cytokine stimulation, supporting previously published results suggesting the critical role of HDAC6 in the regulation of immunosuppressive pathways. 

Scripts and workflow necessary to reproduce the BulkRNA-Seq analysis can be found in the [CytokineStimulationRNAanalysis](https://github.com/HawaBioinformatics/CytokineStimulationRNAanalysis) sub-directory.
