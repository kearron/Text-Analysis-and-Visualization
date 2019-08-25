# 3. find frequency of top 100 words excluding stop words,

import re
from nltk.corpus import stopwords

other_words = {}
with open('./war_n_peace.txt','r') as file:

    for line in file:
        # print(line)
        words = line.split(" ")
        for word in words:
            # print(words)
            word = re.sub('[^A-Za-z]','',word)
            # word = word.lower()
            # print(word)
            if word not in stopwords.words('english'):
                if word not in other_words:
                    other_words[word] = 1
                else:
                    other_words[word] += 1
    count = 0
    for key,value in other_words.items():
        print(key,": ",value)
        count += 1
        if count == 100:
            break
        
    