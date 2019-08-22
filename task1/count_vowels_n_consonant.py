#3. count consonant and vowel frequency


vowels_char = "aeiou"
vowels = 0
consonants = 0
with open('./war_n_peace.txt','r') as file:
   for line in file:
       words = line.split(" ")
       for word in words:
           # print(word)
           for c in word:
               if c.isalpha():
                   if c.isupper():
                       c = c.lower()
                   if c in vowels_char:
                       vowels += 1
                   else:
                       consonants +=1
   print("Total vowel frequency: ",vowels)
   print("Total consonant frequency: ",consonants)
