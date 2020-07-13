# Wordnet test
# make sure to use  >> import nltk >> nltk.download()  [download wordnet]

from nltk.corpus import wordnet as wn


dog = wn.synset("dog.n.01")
print(dog.hypernyms())