# -*- coding: utf-8 -*-
"""
Building a corpus using Wikipedia data
Created on Tue Jul 21 14:50:55 2020

@author: Vince Sing Choi
"""

import os.path
from os import path
import wikipediaapi
import wikipedia 

# Define Wiki API 
wiki_wiki = wikipediaapi.Wikipedia(language ='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

# Define number of pages to be randomly generated
generate = 1


# Randomly generate pages
wiki_pages = wikipedia.random(pages=generate)
for i in range(generate):
    current_page = wiki_wiki.page(wiki_pages[i])
    current_page = wiki_wiki.page("Mohamed_Boudia")
    print ("Page - Exists: %s" % current_page.exists()) 
    title = list(str(current_page.title))
    
    keywords = ["/", "<", ">", ":", "|", "\"", "?", "*", " "]
    # replace symbols for windows 
    for i in range(len(title)):
        if title[i] in keywords: 
            title[i]= "_"
        
    
    file_path = (''.join(title)+ ".txt") 
    if path.exists(file_path):
        print("file already exists")
    else: 
        # print("file does not exists, building document")
        # acronym_detection(current_page.text) :: find acronyms in passage 
        # convert to json file for q/a model
        try:
            f = open(str(file_path), "w", encoding="utf-8" )
            f.write(current_page.text)
            f.close()
        except:
            print("Unable to create file for writing. Skipped.")

# Test page
    # page_py = wiki_wiki.page('Python_(programming_language)')
    # print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True
    # print(page_py.text)

