# Acronyms-and-Abbreviation-Expansion
This repository explores potential new ways to restore acronyms past the conventional dictionary approach. 


## Contents
1. **Related Work** - directory containing related work (papers, articles, journals)
1. **README.md** - contains content of repository and background on the topic 
1. **dataset** - contains programs related to data generation
1. **src**  - contains the main automated QA model program and a program to score Rouge

## Disclaimer ##
Users will have to change working directories to match their needs and download prerequisite packages such as HuggingFace, Jellybeans, Rouge and WikiAPI. 
The version of BERT QA cannot handle non-english characters and will crash if it detects unreadable characters. 
## Data Generation ## 
To generate a corpus we utilize the Wikipedia API to build a collection of Wikipedia pages using **datagen.py**. We recommend creating a directory strictly to store these documents. Not every page in this collection will contain an acronym. The BERT QA Model can roughly store 500 strings in memory so we need to run the **data_split.py** to split longer datasets into multiple smaller datasets. It is possible that during this stage, an acronym or its definition becomes split. Make sure to store the split datasets into a working directory. Next change the directories for **acronym_detector.py**. This program will run through all the split datasets and create a corresponding question and answer dataset for its respective directoires. The detection algorithm is a modified version of the Azimi Method mentioned in the paper. Stop words are removed during this time in both this modified version and the original version (meaning the tagged data will be free of stop words as well). Removal of stopwords is necessary to increase the accuracy and frequency of the detection. If a dataset is provided in a csv file, there is additional code provided to handle some csv files. 

Disclaimer: ensure the files do not have non-english characters. 

## Running the model and Evaluation ##
In the **src** folder, change the working directories of **qa_model_automated.py** and run. This program will load a trained version of BERT QA-model and take in a question file, answer file, and corresponding dataset file generated earlier. It will remove special characters or maskings before printing out a predicted answer to the acronym question as well as the tagged answer. Users can adjust the epsilon values for computing the Jaro Distance as well. The program will caculate the acceptance rate for each epsilon value. This program will also output two files to calculate the ROUGE scores. 

Run **rouge.py** to output the rouge scores after corresponding files have been generated. Unfortunately the pacakage will crash if it detects a null value for a definition. (This can occur if the definition is split and the BERT Model cannot give a reasonable answer to the question). 



