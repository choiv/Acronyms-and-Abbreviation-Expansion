# separte big datasets

import os
import os.path


dataset_dir = "C:\\Users\\Admin\\Desktop\\virtual\\datagen_output\\"
smalldata_dir = "C:\\Users\\Admin\\Desktop\\virtual\\smalldata_output\\"


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
    textfile = open(file,encoding = 'utf-8')
    text = textfile.read()
    basename = os.path.basename(file)
    basename = basename.replace(".txt", "")
    split = text.split() 
    
    temp_string = ""
    counter  = 0
    file_count = 0 
    for i in split:
        counter += len(i)
        if (counter >= 500): # start new file
            file_count = file_count + 1
            output = open(smalldata_dir + basename + "_" + str(file_count) +".txt", "w", encoding = 'utf-8')
            output.write(temp_string)
            temp_string = ""
            counter = 0
        temp_string += i
        temp_string += " "
        counter = counter + 1
        
file_count = file_count + 1
output = open(smalldata_dir + basename + "_" + str(file_count) +".txt", "w", encoding = 'utf-8')
output.write(temp_string)