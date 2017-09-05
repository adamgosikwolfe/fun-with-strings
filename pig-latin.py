#Pig latin
#Translates a sentence into pig latin

import string 

def hasNumbers(input_s):
  return not any(char.isdigit() for char in input_s)
  
def isPunctuation(word_test):
  if word_test in string.punctuation:
    return True
  
running = True
while (running == True):
  input_string = input("Translate: ")
  if hasNumbers(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cosonant=True
    input_array = input_string.split()
    word_count = len(input_array)
    sentence = ""
    for x in range(0, word_count):
      cosonant=True
      word = input_array[x]
      for vowel in vowels:
        if word[0] == vowel:
          if isPunctuation(word[-1]):
            sentence = sentence + word[0:-1].lower() + "ay" + word[-1] + " "
          else:
            sentence = sentence + word.lower() + "ay "
          cosonant=False
      if cosonant == True:
        if isPunctuation(word[-1]):
          sentence = sentence + word[1:-1].lower() + word[0].lower() + "ay" + word[-1] + " "
        else:
          sentence = sentence + word[1:].lower() + word[0].lower() + "ay "
    sentence = sentence[0].capitalize() + sentence[1:].rstrip()
    print(sentence)
    toggle = input("Try another? Y/N")
    if toggle.lower() == "n":
      running = False
    else:
      running = True
  else:
    print("Can only contain alphabetic characters, try again.")