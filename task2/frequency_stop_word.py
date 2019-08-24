# 2.Find frequency of stop words
import re
from nltk.corpus import stopwords

stop_words = {}
with open('./war_n_peace.txt','r') as file:

    for line in file:
        # print(line)
        words = line.split(" ")
        for word in words:
            # print(words)
            word = re.sub('[^A-Za-z]','',word)
            # word = word.lower()
            # print(word)
            if word in stopwords.words('english'):
                if word not in stop_words:
                    stop_words[word] = 1
                else:
                    stop_words[word] += 1
                
    print("Frequency of Stopwords: ", stop_words)