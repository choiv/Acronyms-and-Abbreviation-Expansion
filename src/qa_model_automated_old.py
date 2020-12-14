# -*- coding: utf-8 -*-
"""
Traverse for text files and question files to put in QA_model testing
@author: Vince
"""
from transformers import BertTokenizer
from transformers.modeling_tf_bert import TFBertForQuestionAnswering
import tensorflow as tf
import os
import os.path
import jellyfish
# Define Model parameters 
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = TFBertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")


# Code to traverse directory of test datasets
# MAKE SURE TO CHANGE DIRECTORY

#dataset_dir = "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/datagen_p_output"
#answer_dir =  "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/answer_output/"
#question_dir = "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/question_output/"

dataset_dir = "E:\\PythonProjects\\acronym-dataset\\smalldata_output\\"
answer_dir = "E:\\PythonProjects\\acronym-dataset\\answer_output\\"
question_dir = "E:\\PythonProjects\\acronym-dataset\\question_output\\" 

answer_file  = ""
question_file = ""

#directory = '/dataset/datagen_output'

file_list = [] # dataset 
y_predict = []


# Testing metrics
detected = 0                # counter for number of acronyms detected
correct8 = 0                 # number of acronyms passing JaroDistance]
correct7 = 0
correct5 = 0
epsilon8 = .8                # Threshold
epsilon7 =.7
epsilon5 =.5


# Code to traverse directory of questions
    # match name + "_question.txt"
    # load file and dump each line
    # figure out how many questions (acronyms) are needed to be found
    
print ("Getting file listing....")
for root, dirs, files in os.walk(dataset_dir):
    for fname in files:
        # print("file name :" + str(fname))
        current_file = "{}{}{}".format(os.path.abspath(root), os.path.sep, fname)
        file_list.append(current_file)


for file in file_list:        
    text = open(file,"r", encoding = 'utf-8').read()
    basename = os.path.basename(file)
    basename = basename.replace(".txt", "")
    
    # formats the directory to find the q/a files
    answer_file = answer_dir + basename + "_answer.txt"
    question_file = question_dir + basename + "_question.txt"
    
    if os.path.exists(answer_file):
        if os.path.exists(question_file):

            answer = open(answer_file, "r")
            question = open(question_file, "r")
            
            question_lines = question.readlines()
            answer_lines = answer.readlines()
            
            questions = [] 
            answers = [] 
            
            # parse each question/answer and store in a list to measure later
            for line in question_lines:
                questions.append(line.replace("\n", ""))
            for line in answer_lines:
                answers.append(line.replace("\n", ""))
               
            qnum = len(questions)

            for i in range(qnum):
                detected += 1
                question = str(questions[i])
                input_dict = tokenizer(question, str(text), return_tensors='tf')
                start_scores, end_scores = model(input_dict)
        
                all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
                answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])
                target = answers[i]
                target = target.lower()
        
                unmasked = answer.replace("#", "")
                unmasked = unmasked.replace(".", "")
                unmasked = unmasked.replace(",", "")
                unmasked = unmasked.replace("-", "")
                unmasked = unmasked.lower()
                print(str(question) + " \nAnswer: " + str(unmasked))
                print("target answer: " + target)
                
                score = jellyfish.jaro_distance(target, unmasked)
                if (score >= epsilon8)
                    correct8 += 1
                if (score >= epsilon7)
                    correct7 += 1
                if (score >= epsilon5)
                    correct5 += 1
                    
print ("Correct8: " + str(correct8) + " / Detected " + str(detected) + " = " + str(correct8/detected)) 
print ("Correct7: " + str(correct7) + " / Detected " + str(detected) + " = " + str(correct7/detected)) 
print ("Correct5: " + str(correct5) + " / Detected " + str(detected) + " = " + str(correct5/detected)) 
