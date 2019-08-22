#4. count word starting with a and ending with e

import re


a_word_e = 0
with open('./war_n_peace.txt','r') as file:
    for line in file:
        words = line.split(" ")
        for word in words:
            # print(word)
            if len(word) > 1:
                regex = re.compile('[,.;@_!#$%^&*()<>?/\|}{~:]')
                # print(word)
                if bool(regex.search(word[-1])): #remove last character of word if is special character
                    # print(word)
                    word = word[:-1]
                # print(word)
                if len(word) > 1:
                    # print(word)
                    if word[0].isalpha() and word[-1].isalpha():
                        if word[0].lower() == 'a' and word[-1].lower() == 'e':
                            # print(word)
                            a_word_e += 1
    print("Total words starting with 'a' and ending with 'e': ",a_word_e)