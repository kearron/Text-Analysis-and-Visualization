# 2. count word frequency from particular alphabet


letter = input("Enter alphabet for which to count word frequency: ")
letter = letter.lower()
count = 0
with open('./war_n_peace.txt','r') as text:
    for line in text:
        words = line.split(" ")
        for word in words:
            # word = list(word)
            # print(word)
            if word:
                # print(word[0])
                if word[0].isalpha():
                    if word[0].isupper():
                        first_letter = word[0].lower()
                
                        if first_letter == letter:
                            # print(word[0])
                            count +=1
    print("word frequency starting from alphabet",letter," = ",count )