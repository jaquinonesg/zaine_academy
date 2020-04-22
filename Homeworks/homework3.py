
word = raw_input("Enter a word: ")

z = raw_input("Enter the letter: ")

#o = word.count(z)

#print(o)

c = 0
for i in word:
    if i == z:
        c = c + 1   

message = "The letter {} is {} times in the word {}.".format(z, c, word)
print(message)         

