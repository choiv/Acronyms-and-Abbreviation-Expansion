# -*- coding: utf-8 -*-
# Acronym Expansion using Synonymous Word Integration on BERT
# Authors: Vince Sing Choi and Piyush Puranik

# Synonym Test
# en_thesarus.jsonl contains json line file with 169001 entries of words structured in: word, synonym, pos, key

import jsonlines


counter = 0

with jsonlines.open("../Thesaurus/en_thesaurus.jsonl", mode = "r") as reader: 
    for obj in reader:
        if (obj["word"] == "abandon"):
            print(obj["synonyms"]);
        #counter += 1
#print(counter)