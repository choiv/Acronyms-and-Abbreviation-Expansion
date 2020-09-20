# -*- coding: utf-8 -*-
"""
Find acronyms in a set of txt files.

@author Piyush Puranik
"""

import os
import sys
import acronym

def cleanLine(line):
    new_line = line
    new_line = new_line.replace("(", "")
    new_line = new_line.replace(")", "")
    new_line = new_line.replace("\n", "")
    new_line = new_line.replace(".", "")
    new_line = new_line.replace("?", "")
    new_line = new_line.replace("!", "")
    new_line = new_line.replace(",", "")
    new_line = new_line.replace(";", "")
    new_line = new_line.replace("\"", "")
    new_line = new_line.replace("\'", "")
    new_line = new_line.replace(":", "")

    return new_line


# Get stopwords from file
stopwords = []
try: 
    with open("stopwords.txt", "r") as stopword_file:
        for line in stopword_file.readlines():
            line = line.replace("\n", "")
            stopwords.append(line)
                
except IOError():
    print ("Unable to read stopword.txt")

# Insert all files from the generated data set into a list
datapath = "datagen_output/"
datalist = []
for root, dirs, files in os.walk(datapath):
    for fname in files:
        current_file = "{}{}{}".format(os.path.abspath(root), os.path.sep, fname)
        datalist.append(current_file)

# Find acronyms for each line in each file
not_empty = []
definition = []

for data_file in datalist:
    print ("Reading file: ", data_file)
    with open(data_file, "r", encoding='utf-8') as data:
        for line in data.readlines():
            line = cleanLine(line)      # Removes symbols
            not_empty = acronym.findacronym(stopwords, line)
            definition.append(not_empty)


