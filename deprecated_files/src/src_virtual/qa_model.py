# -*- coding: utf-8 -*-
from transformers import BertTokenizer
from transformers.modeling_tf_bert import TFBertForQuestionAnswering
import tensorflow as tf

tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

model = TFBertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

# question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"

print("\n ====================  Sentence format: whole passage =============================" ) 
question, text = "What does PFLP mean? ", "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of Popular Front for the Liberation of Palestine (PFLP). He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal. == References ==" 
input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 


print ("\n ========================= Just acronym. ============================== \n")
question = "PFLP?" 

input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])
print(str(question) + " \nAnswer: " + str(answer)) 



print("\n ========================= Acronym that isn't in the passage ===================================") 

question = "What does ASAP mean?" 

input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])
print(str(question) + " \nAnswer: " + str(answer)) 



print("\n ========================= Acronym that isn't in the passage version 2 ======================") 

question = "ASAP?" 

input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])
print(str(question) + " \nAnswer: " + str(answer)) 


print("\n ===================================== Modified text removed all acronyms in passage :: left definition in passage ===================================") 
question = "What does PFLP mean?"
text = "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of Popular Front for the Liberation of Palestine. He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of operations in Europe. Boudia was replaced by Carlos the Jackal.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal." 

input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 



print("\n ===================================== Modified text replaced definition with acronym:: ===================================") 

question, text = "What does PFLP mean? ", "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of PFLP. He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal. == References ==" 
input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 








print("\n ================================================= Acronym that is asked that is made up: Carlos the Jackal but exists in the passage =======================================") 
question = "What does CTJ mean?"
input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 





print("\n =========================== Acronym that is asked that is made up: Carlos the Jackal Hunter (added Hunter to the passage) ======================== ") 
question = "What does CTJH mean?"

text = "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of Popular Front for the Liberation of Palestine. He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal Hunter.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal Hunter." 


input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 



print("\n =========================== Acronym that is asked that is made up: Carlos the Jackal Hunter (added CTJH) ======================== ") 
question = "What does CTJH mean?"

text = "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet and member of Popular Front for the Liberation of Palestine. He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal Hunter (CTJH).Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal Hunter." 


input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 






print("\n ==================== Testing adhoc abrv such as: premedical/ premedication as premed :: Added those words in the passage ======================== ")
question, text = "What does premed mean? ", "Mohamed Boudia (24 February 1932 – 28 June 1973) was an Algerian poet, premedical student, and member of Popular Front for the Liberation of Palestine (PFLP). He was assassinated in a state terrorist attack in Paris by a car bomb placed under his seat. His assassination was carried out by Mossad agents as part of the Operation Wrath of God. At the time of his assassination, Boudia was the Chief of PFLP operations in Europe. Boudia was replaced by Carlos the Jackal.Boudia had been a participant in the Algerian War, during which he had been jailed for an attack on a petrol depot in southern France. The end of the war and Algerian independence in 1962 led to his release, having spent three years in prison. Boudia was a playwright, and after independence became director of Algeria's national theatre. He fled to France after Houari Boumediène seized power in June 1965. He ran a theatre in Paris, whilst beginning to work with figures such as Carlos the Jackal. == References ==" 
input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)

all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])

print(str(question) + " \nAnswer: " + str(answer)) 



