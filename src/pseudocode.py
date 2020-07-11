# -*- coding: utf-8 -*-
# Acronym Expansion using Synonymous Word Integration on BERT
# Authors: Vince Sing Choi and Piyush Puranik



# Requirements:
    # 1. Corpus/Dictionary of synonyms: https://github.com/zaibacu/thesaurus
        # json parser 
    # 2. BERT model
    # 3. Find/create corpus to mask and test


# Let D be the document in question, A be the detected acronym, AE be the expansion of A

# Alg 1: Preparing the data
# For A in D : 
#    mask(AE) 
# D' <- D with masked AE 
# return D' 


# Let C be the collection of candidate words for the expansion
# Alg 2: Find candidate expansions
# For i in |A|:
    # C_i <-  BERT(D')
    # C_i <- C_i + SYN(C_i) // Append synonyms of words found by BERT
    # max_score <- 0
    # For j in C_i :
        # score = Acronym_score(C_j)
        # if max_score < score
        # C' <- C_j
# return C' 


# Alg 3: Acronym_score
    # Considerations: 
        # BERT outputs ordered list of words descending in likelihood
            # implies - synonyms outputted should have a likelihood ratio as well
        # prefixes and starting letters should be considered
        # calculate permutations 


# finally calculate how accurate predicted expansions are to the masked expansions


