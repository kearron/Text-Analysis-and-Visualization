
# 1. count frequency of letters in a text.file


charcount = {} 
validchars = "abcdefghijklmnopqrstuvwxyz" 
with open('./war_n_peace.txt','r') as file: 

    for i in range(97,123): # lowercase range
        c = (chr(i)) # the chars a-z
        charcount[c] = 0 

    for line in file:
        words = line.split(" ") # line into words
        # print(words)
        for word in words:  
            chars = list(word) #convert word into a char list
            # print(chars)
            for c in chars:  
                if c.isalpha(): 
                    if c.isupper():
                        c = c.lower()  
                    if c in validchars: # if in valid char set
                        # print(c)
                        charcount[c] += 1 

    # print(charcount)
    for key, value in sorted(charcount.items()):
        print(key, ' = ', value)

