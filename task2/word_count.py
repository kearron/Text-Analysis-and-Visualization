# SubTask 2:
# 1.Find word count,

# find the longest and shortest word and there frequency,
# find top 100 verbs, nouns, adjectives and adverbs,find their composition of text based on part of speech ( like 10% is noun, 20% is verb ..) ,
# find top 100 noun-noun phrase and noun-verb pair .
import re

word_count = {}
with open('./war_n_peace.txt','r') as file:
   for line in file:
       words = line.split(" ")
       for word in words:
           word = re.sub('[^A-Za-z]','',word) #remove character other than A-Z, a-z
           if word not in word_count:
               word_count[word] = 1
           else:
               word_count[word] += 1
   for key,value in word_count.items():
       print(key,": ",value)