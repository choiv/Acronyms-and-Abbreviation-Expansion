''' This program is aimed to extract acronyms and their expansions from 20 files attached to this source code.'''

import os
import re
# definitions and initializations of files and documents
# doc_path = "C:\\Users\\Rihanna\\Desktop\\Intro. to CL\\final project\\CL_Final_Project_830597032\\Manual Count statistics\\txt files\\"
# doc_path = "E:\\PythonProjects\\Acronym_detection\\text_files\\"
#doc_path = "C:\\Users\Admin\\Desktop\\Acronyms-and-Abbreviation-Expansion\dataset\\text_files\\"
doc_path = "C:\\Users\Admin\\Desktop\\drug_port_extraction\\output\\"
#doc_path = "E:\\PythonProjects\\acronym-dataset\\smalldata_output\\"


# dataset_path = "C:\\Users\\Rihanna\\Desktop\\Intro. to CL\\final project\\CL_Final_Project_830597032\\Manual Count statistics\\dataset_acr_exp.csv"
#dataset_path = "E:\\PythonProjects\\Acronym_detection\\dataset_acr_exp.csv"
#dataset_path = "E:\\PythonProjects\\acronym-dataset\\dataset_acr_exp.csv" 
dataset_path = "C:\\Users\Admin\\Desktop\\drug_port_extraction\\dataset_drugpot.csv"
dataset_csv_file = open(dataset_path,"w", encoding='utf-8')



# output_file = open("C:\\Users\\Rihanna\\PycharmProjects\\CL_final_project\\output.txt", 'w', encoding='utf-8')
#output_file = open("E:\\PythonProjects\\Acronym_detection\\output.txt", 'w', encoding='utf-8')
#output_file = open("E:\\PythonProjects\\acronym-dataset\\output.txt" , 'w', encoding='utf-8')
output_file= open("C:\\Users\Admin\\Desktop\\drug_port_extraction\\output.txt", 'w', encoding='utf-8')


acronyms_list_total = []    # all detected acronyms will be appended to this list
expansion_list_total = []   # all detected expansions will be appended to this list


'''make_acronym function gets a string (a potential expansion) and builds a word out of initials of the words in it 
the output will be used to compare the initials with the real expansion of an acronym 
to check if it has been detected correctly. '''


def make_acronym(string):                    # takes a string that includes spaces between words
    list_of_words = string.split()           # splits the doc and stores the separated words into a list
    acronym = ""                             # prepares an empty string to store the acronym of the string in it
    for word in list_of_words:
        acronym = acronym + word[0]          # sticks the first char of words together and makes the acronym
    return acronym



'''preprocessing function is aimed to clean and prepare the input raw text for being checked for potential acornyms and 
their expansions. It handles irredularities and removes unwanted characters and stop words.'''
def preprocessing(text):
    # preprocessing:
    stop_words = ["with", "the"]
    #doc_text_main = text
    text = re.sub("for", "", text)
    text = re.sub("and", "", text)
    text = re.sub("institute of", "institute", text)
    text = re.sub("BandWidth", "Band Width", text)
    text = re.sub("Bandwidth", "Band Width", text)
    text = re.sub("bandwidth", "Band Width", text)
    text = re.sub("transmission opportunity", "T X O P", text)
    text = re.sub("wireless local network", "wireless local area network", text)

    text = re.sub("CSMA/CA", "CSMACA", text)
    text = re.sub("demodulation", "de modulation", text)
    text = re.sub("Institute of", "institute", text)
    text = re.sub("the global", "global", text)         # GSM and the like
    text = re.sub("The global", "global", text)         # GSM and the like
    text = re.sub("transmission", "T X", text)          # Transmission = TX
    text = re.sub("Communications \(G", "(G", text)     # GSM
    text = re.sub("adjustment across", "across", text)  # Adjustment across technologies
    # doc_txt = re.sub("\/\(","( ", doc_txt)
    text = re.sub("\\/", " ", text)             # Adjustment across technologies
    for word in text.split():
        if "(" and ")" not in word:             # if the word is not a potential acronym
            text = re.sub("\-", " ", text)      # Adjustment across technologies
            text = re.sub("\/", " ", text)
            text = re.sub('[",]', "", text)     # remove: ", comma
            for word in stop_words:             # remove stop words like "with" and "the". Because these "ruin" the expansions!!!
                text = re.sub(word, " ", text)

        elif "(" and ")" in word:               # if the word is a potential acronym
            text = re.sub("\-", "", text)       # Adjustment across technologies
            text = re.sub("\/", "", text)
            text = re.sub("2", "t", text)



    text = re.sub(r"\s+", r" ", text)  # Turn multiple spaces into one
    return text





''' pattern one is defined using the examples as follows:
# ---------------------------------------------------------------------------------------------------------
        # pattern family 1 : local area network (LAN)
        # local area network ("LAN")             (and the like)
        # local area network ("LAN"),            (and the like)
        # local area networks (LANs)             (and the like)
        # physical random access channel (PRACH) (and the like)
        # unique user identification (UUID)      (and the like)
        # high definition television (HDTV)      (and the like)
        # when L for layer is not present in the acronym
        # Packet data gateway (PDG)              (and the like)
        # wimax
'''


def pattern_one(list_of_words):

    for i in range(len(list_of_words)):  # checks out all the words in the text
        if "(" and ")" in list_of_words[i]:
            # print(list_of_words[i])f
            word_index = i
            acronym_suspect_nested = ""
            acronym_suspect = re.sub(r"[\W|\-]", r"", list_of_words[i])
            acronym_suspect = re.sub("[s]$", "", acronym_suspect)
            acronym_suspect = re.sub(" \\s", "", acronym_suspect)
            acronym_suspect = re.sub(" \\s", "", acronym_suspect)
            acronym_suspect = re.sub("\/", "", acronym_suspect)

            print(acronym_suspect)

            # channel at the end:
            acronym_suspect_channel = re.sub("CH$", "C", acronym_suspect)
            acronym_suspect_identification = re.sub("ID$", "I", acronym_suspect)
            acronym_suspect_television = re.sub("TV$", "T", acronym_suspect)
            acronym_suspect_gateway = re.sub("GW$", "G", acronym_suspect)
            acronym_suspect_wimax = re.sub("ax$", "a", acronym_suspect)
            acronym_suspect_physical_layer = re.sub("^PP", "PLP", acronym_suspect)
            acronym_suspect_wlan = re.sub("WLAN", "WLN", acronym_suspect)

            # print(acronym_suspect)
            # we need to know how many letters it has
            # so we can know how many surrounding words we need to check
            len_of_acronym_suspect = len(acronym_suspect)
            len_of_acronym_suspect_channel = len(acronym_suspect_channel)
            len_of_acronym_suspect_identification = len(acronym_suspect_identification)
            len_of_acronym_suspect_television = len(acronym_suspect_television)
            len_of_acronym_suspect_gateway = len(acronym_suspect_gateway)
            len_of_acronym_suspect_wimax = len(acronym_suspect_wimax)
            len_of_acronym_suspect_physical_layer = len(acronym_suspect_physical_layer)
            len_of_acronym_suspect_wlan = len(acronym_suspect_wlan)
            len_of_acronym_suspect_nested = 0

            # we go back in the text as long as the length of acronym suspect and
            # extract the initials of the words found
            expansion_suspect = ""
            expansion_suspect_channel = ""
            expansion_suspect_identification = ""
            expansion_suspect_television = ""
            expansion_suspect_gateway = ""
            expansion_suspect_wimax = ""
            expansion_suspect_physical_layer = ""
            expansion_suspect_wlan = ""
            expansion_suspect_nested = ""
            the_rest_of_slice = ""

            # initials means a word made up of the first letters of the words in a string
            initials_of_expansion_suspect = ""
            initials_of_expansion_suspect_channel = ""
            initials_of_expansion_suspect_identification = ""
            initials_of_expansion_suspect_dehyphenated = ""
            initials_of_expansion_suspect_television = ""
            initials_of_expansion_suspect_gateway = ""
            initials_of_expansion_suspect_wimax = ""
            initials_of_expansion_suspect_nested = ""
            initials_of_expansion_suspect_physical_layer = ""
            initials_of_expansion_suspect_wlan = ""

            # acronym_suspect_dehyphenated =""


# ADDED THIS CATCH 
            print(str(word_index - len_of_acronym_suspect))
            if (word_index - len_of_acronym_suspect >= 0):
                for j in range(word_index - len_of_acronym_suspect, word_index):
                    expansion_suspect = expansion_suspect + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect = re.sub(r"^\s", r"", expansion_suspect)
                    # expansion_suspect = re.sub(r"[\-]", r" ", expansion_suspect)
                    # remove dash if present
                    expansion_suspect_dehyphenated = ""
                    expansion_suspect_dash_removed = re.sub(r"[\-]", r" ", expansion_suspect)
                    if len(expansion_suspect_dash_removed) > len(expansion_suspect):
                        list_of_words_dash_removed = expansion_suspect_dash_removed.split()
                        for t in range((len(expansion_suspect_dash_removed) - len(acronym_suspect)),
                                       (len(expansion_suspect_dash_removed))):
                            expansion_suspect_dehyphenated += list_of_words_dash_removed[t]
                            # acronym_suspect_dehyphenated = re.sub("\-","",acronym_suspect)
    
                    initials_of_expansion_suspect = make_acronym(expansion_suspect)
                    initials_of_expansion_suspect_dehyphenated = make_acronym(expansion_suspect_dehyphenated)

            ###### detecting nested expansions:##################################################
            # nested expansions are the ones where an expansion includes an acronym which exists in
            # its corresponding acronym. for example: SRAM : synchronous RAM
            # we call these recurring acronyms "slices"
            # we check if a slice is being repeated in one of the words in the expansion or not

            list_of_slice_lengths.clear()
            slices_list.clear()
            number_of_types_of_slices = len_of_acronym_suspect - 1
            # we have slices of types: length_two, length_three, etc
            for t in range(2, number_of_types_of_slices - 1):
                list_of_slice_lengths.append(t)

            for slice_length in list_of_slice_lengths:
                for i in range(len_of_acronym_suspect):
                    if (i + slice_length) < len_of_acronym_suspect:
                        slices_list.append(acronym_suspect[i:i + slice_length + 1])

            for slice in slices_list:
                if slice in expansion_suspect:
                    first_letter_of_slice = slice[0]
                    the_rest_of_slice = slice[1:]
                    acronym_suspect_nested = re.sub(slice, first_letter_of_slice, acronym_suspect)
                    len_of_acronym_suspect_nested = len(acronym_suspect_nested)

# ADDED THIS CATCH
            if (word_index - len_of_acronym_suspect >= 0):
                for j in range(word_index - len_of_acronym_suspect_nested, word_index):
                    expansion_suspect_nested = expansion_suspect_nested + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_nested = re.sub(r"^\s", r"", expansion_suspect_nested)
                    # expansion_suspect = re.sub(r"[\-]", r" ", expansion_suspect)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    initials_of_expansion_suspect_nested = make_acronym(expansion_suspect_nested)
                    ### end of detecting nested expansions###########################################
    
                for j in range(word_index - len_of_acronym_suspect_channel, word_index):
                    expansion_suspect_channel = expansion_suspect_channel + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_channel = re.sub(r"^\s", r"", expansion_suspect_channel)
                    # remove dash if present
                    expansion_suspect_channel = re.sub(r"[\-]", r" ", expansion_suspect_channel)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    initials_of_expansion_suspect_channel = make_acronym(expansion_suspect_channel)
    
                for j in range(word_index - len_of_acronym_suspect_identification, word_index):
                    expansion_suspect_identification = expansion_suspect_identification + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_identification = re.sub(r"^\s", r"", expansion_suspect_identification)
                    # remove dash if present
                    expansion_suspect_identification = re.sub(r"[\-]", r" ", expansion_suspect_identification)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    initials_of_expansion_suspect_identification = make_acronym(expansion_suspect_identification)
    
                for j in range(word_index - len_of_acronym_suspect_television, word_index):
                    expansion_suspect_television = expansion_suspect_television + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_television = re.sub(r"^\s", r"", expansion_suspect_television)
                    # remove dash if present
                    expansion_suspect_television = re.sub(r"[\-]", r" ", expansion_suspect_television)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    initials_of_expansion_suspect_television = make_acronym(expansion_suspect_television)
    
                for j in range(word_index - len_of_acronym_suspect_gateway, word_index):
                    expansion_suspect_gateway = expansion_suspect_gateway + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_gateway = re.sub(r"^\s", r"", expansion_suspect_gateway)
                    # remove dash if present
                    expansion_suspect_gateway = re.sub(r"[\-]", r" ", expansion_suspect_gateway)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    initials_of_expansion_suspect_gateway = make_acronym(expansion_suspect_gateway)
    
                for j in range(word_index - len_of_acronym_suspect_wimax, word_index):
                    expansion_suspect_wimax = expansion_suspect_wimax + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_wimax = re.sub(r"^\s", r"", expansion_suspect_wimax)
                    # remove dash if present
                    expansion_suspect_wimax = re.sub(r"[\-]", r" ", expansion_suspect_wimax)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
    
                    initials_of_expansion_suspect_wimax = make_acronym(expansion_suspect_wimax)
    
                for j in range(word_index - len_of_acronym_suspect_physical_layer, word_index):
                    expansion_suspect_physical_layer = expansion_suspect_physical_layer + " " + list_of_words[j]
                    # we don't need the first space
                    expansion_suspect_physical_layer = re.sub(r"^\s", r"", expansion_suspect_physical_layer)
                    # remove dash if present
                    expansion_suspect_physical_layer = re.sub(r"[\-]", r" ", expansion_suspect_physical_layer)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
    
                    initials_of_expansion_suspect_physical_layer = make_acronym(expansion_suspect_physical_layer)
    
                for j in range(word_index - len_of_acronym_suspect_wlan, word_index):
                    expansion_suspect_wlan = expansion_suspect_wlan + " " + list_of_words[j]
    
                    # we don't need the first space
                    expansion_suspect_wlan = re.sub(r"^\s", r"", expansion_suspect_wlan)
    
                    # remove dash if present
                    expansion_suspect_wlan = re.sub(r"[\-]", r" ", expansion_suspect_wlan)
    
                    # expansion_acronym = expansion_acronym + list_of_words[j][0]
                    # initials_of_expansion_suspect_wlan = make_acronym(expansion_suspect_wlan)
                    initials_of_expansion_suspect_wlan = make_acronym(expansion_suspect_wlan)

            # now we must compare the two suspects. If they match, the acronym-expansion pair
            # has been found:
            # if (initials_of_expansion_suspect.upper() == acronym_suspect.upper() ):
            #    acronyms_list_total.append(acronym_suspect.upper()+",")
            #    expansion_list_total.append(expansion_suspect)
            if (initials_of_expansion_suspect.upper() == acronym_suspect.upper()):        # these "if"s are so similar so the explanations won't be repeated
                acronyms_list_total.append(acronym_suspect.upper() + ",")
                expansion_list_total.append(expansion_suspect)

            elif (initials_of_expansion_suspect_channel.upper() == acronym_suspect_channel.upper()):
                acronyms_list_total.append(acronym_suspect_channel.upper() + "H" + ",")
                expansion_list_total.append(expansion_suspect_channel)

            elif (initials_of_expansion_suspect_identification.upper() == acronym_suspect_identification.upper()):
                acronyms_list_total.append(acronym_suspect_identification.upper() + "D" + ",")
                expansion_list_total.append(expansion_suspect_identification)

            # elif (initials_of_expansion_suspect_dehyphenated.upper() == acronym_suspect.upper()):
            #     acronyms_list_total.append(acronym_suspect_dehyphenated.upper() + ",")
            #     expansion_list_total.append(expansion_suspect_dehyphenated)


            elif (initials_of_expansion_suspect_television.upper() == acronym_suspect_television.upper()):
                acronyms_list_total.append(acronym_suspect_television.upper() + "V" + ",")
                expansion_list_total.append(expansion_suspect_television)

            elif (initials_of_expansion_suspect_gateway.upper() == acronym_suspect_gateway.upper()):
                acronyms_list_total.append(acronym_suspect_gateway.upper() + "W" + ",")
                expansion_list_total.append(expansion_suspect_gateway)

            elif (initials_of_expansion_suspect_wimax.upper() == acronym_suspect_wimax.upper()):
                acronyms_list_total.append(acronym_suspect_wimax.upper() + "X" + ",")
                expansion_list_total.append(expansion_suspect_wimax)

            elif (initials_of_expansion_suspect_physical_layer.upper() == acronym_suspect_physical_layer.upper()):
                temp_acronym_phy_layer = acronym_suspect_physical_layer.upper()
                temp_acronym_phy_layer = re.sub("PLP", "PP", temp_acronym_phy_layer)
                acronyms_list_total.append(temp_acronym_phy_layer + ",")
                expansion_list_total.append(expansion_suspect_physical_layer)

            elif (initials_of_expansion_suspect_nested.upper() == acronym_suspect_nested.upper()):
                acronyms_list_total.append(acronym_suspect_nested + the_rest_of_slice + ",")
                expansion_list_total.append(expansion_suspect_nested + "," + "nested")

            elif (initials_of_expansion_suspect_wlan.upper() == acronym_suspect_wlan.upper()):
                temp_acr = acronym_suspect_wlan.upper()
                temp_acr = re.sub("WLN", "WLAN", temp_acr)
                acronyms_list_total.append(temp_acr + ",")
                expansion_list_total.append(expansion_suspect_wlan)

        # end of pattern family 1
        # ----------------------------------------------------------------------------------------------------
    return


'''pattern two is when the acronym comes first and the expansion comes in parantheses'''

def pattern_two(list_of_words):
    # ----------------------------------------------------------------------------------------------------
    # pattern family 2:
    # LAN (Local area network) (and the like)
    for i in range(len(list_of_words)):  # checks out all the words in the text
        if "(" in list_of_words[i]:                                               # if ( exists and ) doesn't, it is possibly an expansion inside paratheses
            if ")" not in list_of_words[i]:                                       # like: LAN (local area network)
                initials_of_expansion_suspect_p2 = ""
                acronym_suspect_p2_index = i - 1                                  # so we need the previous word, possibly an acronym
                acronym_suspect_p2 = list_of_words[acronym_suspect_p2_index]      # it is the (i-1)th word
                len_of_acronym_suspect_p2 = len(acronym_suspect_p2)
                expansion_suspect_p2 = ""

                print("check here")
                print(len(list_of_words))
                print(str(i + len_of_acronym_suspect_p2 ))
                
                # Added check here
                if (i + len_of_acronym_suspect_p2 <= len(list_of_words)):
                    for j in range(i, i + len_of_acronym_suspect_p2):
                        # expansion_component_p2 = re.sub(r"\-"," ", list_of_words[j])
                        expansion_component_p2 = re.sub(r'\W', r"", list_of_words[j])      # remove unwanted things. non-alphanumetric and underscore
    
                        expansion_suspect_p2 += expansion_component_p2 + " "
                        # we don't need the first space
                        expansion_suspect_p2 = re.sub(r"^\s", r"", expansion_suspect_p2)
    
                        expansion_suspect_p2 = re.sub(r'[\-]', r" ", expansion_suspect_p2)
                        # initials_of_expansion_suspect_p2 += expansion_component_p2[0]
    
                        initials_of_expansion_suspect_p2 = make_acronym(expansion_suspect_p2)

                if initials_of_expansion_suspect_p2.upper() == acronym_suspect_p2.upper():   # if the initials of the expansion suspect matches the acronym suspect, we have
                    acronyms_list_total.append(acronym_suspect_p2.upper() + ",")             # deteceted a pair of acronym and expansion
                    expansion_list_total.append(expansion_suspect_p2)                        # so it will be added to the list of results


                    # end of pattern family 2
                    # -------------------------------------------------------------------------------
    return

'''Detect_acronym function checks out all the text and finds 
pairs of acronyms and expansions. In order to do so, it needs to be capable of detecting various patterns 
by which acronym-expansion pairs are represented. The most common patterns are the following two patterns and their variations: 
example:
LAN (local aread network) 
local area network (LAN)'''


def detect_acronym(doc_txt,filename):     # doc_text: the raw content of a paper
    # definitions:
    global expansion_suspect_p3_initials, initials_of_expansion_suspect_p2_made, acronym_suspect_singular, last, expansion_suspect_dehyphenated, acronym_suspect_dehyphenated, the_rest_of_slice, len_of_acronym_suspect_nested, list_of_slice_lengths, slices_list

    doc_txt = preprocessing(doc_txt)
    list_of_slice_lengths = []
    slices_list = []

    list_of_words = doc_txt.split()
    pattern_one(list_of_words)   # pass the list of all words in the doc to the function of pattern one
    pattern_two(list_of_words)   # pass the list of all words in the doc to the function of pattern two

    # writing the results into the output file
    for i in range(len(acronyms_list_total)):
        if len(acronyms_list_total[i])>2:
            dataset_csv_file.write(filename+",")
            dataset_csv_file.write(acronyms_list_total[i])
            dataset_csv_file.write(expansion_list_total[i])
            dataset_csv_file.write("\n")

    acronyms_list_total.clear()
    expansion_list_total.clear()
    return


###########################################################################33

def main():
    # list of the files existing in the path
    filename_list = os.listdir(doc_path)
    print(filename_list)
    doc_count = 0
    # search the path and for each file, perform the whole acronym detection process
    for filename in filename_list:
        #print(doc_count)
        print(filename)
        file_path = doc_path+filename
        document = open(file_path,'r', encoding='utf-8')
        doc_text = document.read()
        #print(doc_text)
        filename = re.sub("[.txt]", "", filename)
        detect_acronym(doc_text,filename)
        doc_count+=1
    return

main()
dataset_csv_file.close()


