def kCh(string, letter):
  cont = 0

  for i in string:
    if i == letter:
      cont = cont + 1
  return cont

word = raw_input("Enter a word: ")
character = raw_input("Enter a character: ")

cont = kCh(word, character)

print("The character {} is repeated {} times in the word {}.".format(character, cont,word))