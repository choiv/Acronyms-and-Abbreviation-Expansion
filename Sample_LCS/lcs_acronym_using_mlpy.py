#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:02:33 2018

@author: Piyush Puranik
"""
import sys
import mlpy
from prettytable import PrettyTable

#Simple string max/min functions
def minString(s):
    return 0 if s < 0 else s

def maxString(s,length):
    return length if s > length else s

#Check for filename argument
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
filename = sys.argv[1]

#Loading Stopwords
try:
    f = open("stopwords","r")
except IOError:
    print "Cannot find stopwords file"
stopwords = f.read().splitlines()
print "Stopwords loaded from file\n"

#Loading Text File
print "<",filename,">"
try:
    f = open(filename, "r")
except IOError:
    print "Cannot open this file!"
text = f.readlines()

#Split line into words
acronym_list = []
allwords = []
acronym_indices = []
for i in text  :  
    allwords += i.split()
    
for index, word in enumerate(allwords):
    if word.isupper() and len(word) > 2:
        acronym_list.append (''.join(e for e in word if e.isalnum()))
        acronym_indices.append(index)
        
x = PrettyTable(["Acronym","Definition"])
for index, acronym in enumerate(acronym_list):
    acronym_split = []
    for c in acronym:
        acronym_split.append(ord(c.upper()))
    word_window = [word for word in allwords[minString(acronym_indices[index] - 10):maxString(acronym_indices[index] + 10, len(allwords))]]
    letter_window = [ord(word[0]) for word in word_window]
    length, path = mlpy.lcs_std(letter_window,acronym_split)
    printacronym = ''.join(chr(c).upper() for c in acronym_split)
    printfull = []
    word_path = path[0]
    print word_path
    printfull = [word for word in word_window[word_path[0]:word_path[-1] + 1]]
    printfull = ' '.join(printfull)
    x.add_row([printacronym,printfull])
print x
       
#print acronym_list
#print acronym_indices





    
