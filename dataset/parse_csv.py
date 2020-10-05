# Parse CSV file and generate a question.txt and an answer.txt for BERT modeling
# CSV file contains: <name_of_file>, <acronym_detected>, <definition>, <notes> 

import csv

# paths
datapath = "C:\\Users\\Admin\\Desktop\\virtual\\"
answer_dir = "C:\\Users\Admin\\Desktop\\virtual\\answer_output\\"
question_dir = "C:\\Users\Admin\\Desktop\\virtual\\question_output\\" 

# hack to close file in loop without doing comparison check
answers = open("C:\\Users\\Admin\\Desktop\\virtual\\requirements.txt")
questions = open("C:\\Users\\Admin\\Desktop\\virtual\\requirements.txt")


dataset = open(datapath + "dataset_acr_exp.csv")
reader = csv.reader(dataset)

current_file = ""
file_name = ""
for row in reader:
    file_name = str(row[0])
    if (file_name != current_file): 
        answers.close()
        questions.close()
        current_file = file_name
        answer_file = answer_dir + file_name + "_answer.txt"
        question_file = question_dir + file_name + "_question.txt"
        
        answers = open(answer_file, "w")
        questions = open(question_file, "w")
    questions.write("What does " + row[1] + " mean?\n")    
    answers.write(row[2] + "\n")

        



answers.close()
questions.close() 