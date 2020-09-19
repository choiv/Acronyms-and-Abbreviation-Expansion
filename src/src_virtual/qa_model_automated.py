# -*- coding: utf-8 -*-
"""
Traverse for text files and question files to put in QA_model testing
@author: Vince
"""
from transformers import BertTokenizer
from transformers.modeling_tf_bert import TFBertForQuestionAnswering
import tensorflow as tf
import os

# Define Model parameters 
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = TFBertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")


# Code to traverse directory of test datasets
# MAKE SURE TO CHANGE DIRECTORY

dataset_dir = "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/datagen_p_output"
answer_dir =  "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/answer_output/"
question_dir = "C:/Users/Admin/Desktop/Acronyms-and-Abbreviation-Expansion/dataset/question_output/"

answer_file  = ""
question_file = ""

#directory = '/dataset/datagen_output'

file_list = [] # dataset 
y_predict = []


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
    text = open(file,"r").read()
    basename = os.path.basename(file)
    basename = basename.replace(".txt", "")
    
    # formats the directory to find the q/a files
    answer_file = answer_dir + basename + "_answer.txt"
    question_file = question_dir + basename + "_question.txt"
    
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
        question = questions[i]
        input_dict = tokenizer(question, text, return_tensors='tf')
        start_scores, end_scores = model(input_dict)

        all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
        answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

        print(str(question) + " \nAnswer: " + str(answer))

