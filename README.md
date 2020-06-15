# Acronyms-and-Abbreviation-Expansion
This repository explores potential new ways to restore acronyms past the conventional dictionary approach. 


## Contents
1. **Related Work** - directory containing related work (papers, articles, journals)
1. **README.md** - contains content of repository and background on the topic 

## Background Information
Throughout the development of modern day language, acronyms have been coined and used to shorten commonly used text-based word sequences. By definition acronyms are an abbreviation formed from the initial letters of other words and pronounced as a word. A growing concern presents itself in the medical industry as acronyms are encouraged due to volatile time pressure. Other constraints such as character limitation in databases also play a role in encouraging the use of acronyms. 

A major problem then presents itself as an issue of the reinterpretation of acronyms, especially in inconsistently defined or non-universally used ones.  Acronyms can be classified into two different groups:

1. **Standard abbreviations** - These abbreviations are widely accepted and generally used such as: HIV (Human Immunodeficiency Virus) and SARS (Severe Acute Respiratory Syndromes). 

1. **Ad hoc abbreviations** – These abbreviations are used on more localized cases and are usually specific to the user’s own notations or context. For example, a physician may abbreviate hypertension as HTN. 

Traditionally, acronym expansion is used to reconstruct the meaning of these abbreviated terms. This is imperative to reproduce the original intended meanings of the user. In the medical field this is exceptionally critical to maintain universal understanding amongst all parties. While a dictionary approach may satisfy a majority of standard abbreviations, ad hoc acronyms present a problem for this method. 

### LCS (Least Common Substring) Approach 
One of the methods used to reconstruct acronyms is through Least Common Substrings. By nature, most acronyms follow a rule which utilizes the first letter of each word as an abbreviated letter. In the case of Least Common Substring, we abbreviate it by LCS. LCS’s basic criteria is to look for certain characters in words in the original order that can be candidates for expansion. In other words, it looks for a substring that contains the abbreviated letters.  
This basic approach falls short when either:

1. The search space is too difficult to be determined (ex: the scope of the substring and the use of the acronym are too far apart).

1. The abbreviation matches multiple other expansions. 
Ex: MODS can mean either Multiple Organ Dysfunction Syndrome or short for modest. 

1. The abbreviation has multiple words with similar semantics.

We have included a simple sample code for LCS [here](https://github.com/choiv/Acronyms-and-Abbreviation-Expansion/tree/master/Sample_LCS).

### LMAAE (Language Model-based Automated Abbreviation Expansion) Approach
Du et al. proposed a three step procedure LMAAE to tackle the existing problems of the LCS approach. 

1. Partitioning: the abbreviated word is partitioned into several blocks with each block in correspondence with a word in the phrase. In general the algorithm creates 2^n partitions and reduces them later on. In short the three parts consist of: 

1. Expansion and filter: For each block, any words that follows LCS rules will create the expansion block set. The expansion and the abbreviation are thrown into a Cartesian product. We apply the prefix abbreviation rule (abbreviations consist of the prefixes of the key words of the phrase) to reduce the search space.  For those abbreviations that do not follow this rule, a language model is used to evaluate and search through each sequence to further reduce the expansion. 

1. Cluster: The expansion sets are put through a mean-shift-clustering algorithm to cluster results and reduce redundant expansions.  


[More details on LMAAE approach](https://github.com/choiv/Acronyms-and-Abbreviation-Expansion/blob/master/Related%20Work/FGCSbiomedicaldataanalysis.pdf). 

