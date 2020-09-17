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
directory = '/data'
for filename in os.listdri(directory): 
    qfile = fil


# Code to traverse directory of questions
    # match name + "_question.txt"
    # load file and dump each line
    # figure out how many questions (acronyms) are needed to be found
    





# question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"


# question, text = "What does PFLP mean? ", "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of Popular Front for the Liberation of Palestine (PFLP). He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal. == References ==" 
# input_dict = tokenizer(question, text, return_tensors='tf')
# start_scores, end_scores = model(input_dict)

# all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
# answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

# print(str(question) + " \nAnswer: " + str(answer)) 