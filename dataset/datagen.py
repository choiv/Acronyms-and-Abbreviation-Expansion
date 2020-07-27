# -*- coding: utf-8 -*-
"""
Building a corpus using Wikipedia data
Created on Tue Jul 21 14:50:55 2020

@author: Vince Sing Choi
"""

import os
import wikipediaapi
import wikipedia
import sys

# Define Wiki API 
wiki_wiki = wikipediaapi.Wikipedia(language ='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

# Get number of pages to generate from command line arguments.
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Invalid arguments\n")
    print("This program pulls a user specified number of random pages from wikipedia and stores them in text files.\n")
    print("Usage: datagen.py <number of pages>")
    sys.exit(0)

# Randomly generate pages
    
print("Downloading pages... ")

counter = 0     # Counts current number of pages generated
total_pages = int(sys.argv[1])
rem_pages = total_pages

while (rem_pages > 0):
    generate = 500 if rem_pages > 500 else rem_pages  # Wiki-API allows only 500 pages per request
    rem_pages -= 500  
    
    wiki_pages = wikipedia.random(pages=generate)
    for i in range(generate):
        current_page = wiki_wiki.page(wiki_pages[i])
        # current_page = wiki_wiki.page("Mohamed_Boudia")
        # print ("Page - Exists: %s" % current_page.exists()) 
        print ("Page ", counter+1 ," of ", total_pages)
        counter += 1
        title = list(str(current_page.title))
        
        keywords = ["/", "<", ">", ":", "|", "\"", "?", "*", " "]
        # replace symbols for windows 
        for i in range(len(title)):
            if title[i] in keywords: 
                title[i]= "_"
            
        output_directory = "datagen_output"
        os.makedirs(output_directory,exist_ok=True)
            
        file_path = (''.join(title)+ ".txt") 
        file_path = os.path.join(output_directory, file_path)
        if os.path.exists(file_path):
            print("file already exists")
        else: 
            # print("file does not exists, building document")
            # acronym_detection(current_page.text) :: find acronyms in passage 
            # convert to json file for q/a model
            try:
                f = open(str(file_path), "w+", encoding="utf-8" )
                f.write(current_page.text)
                f.close()
            except:
                print("Error:", sys.exc_info()[0], "\n Skipped")

# Test page
    # page_py = wiki_wiki.page('Python_(programming_language)')
    # print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True
    # print(page_py.text)

