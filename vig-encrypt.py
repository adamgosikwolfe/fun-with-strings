#Vigenere / Vernam / Ceasar Ciphers 
#Functions for encrypting and decrypting data messages. Then send them to a friend.

import string

def numToLetter(encryption,coded):
  for n, alpha in enumerate(string.ascii_lowercase):
    for num, c in enumerate(coded):
      if c == n+1:
        encryption[num] = alpha

def letterToNum(message,coded):
  for n, alpha in enumerate(string.ascii_lowercase):
    for m, letter in enumerate(message):
      if letter == alpha:
        coded[m] = n+1

choice = input("Encrpyt(e) or decrypt(d)?")
message = input("What's the message?").strip()
key = input("What's the key?").strip()

coded = [0]*len(message)

while len(key) < len(message):
  key = key + key
key_offset=len(message)-len(key)
key = key[:key_offset]

letterToNum(message,coded)

for n, alpha in enumerate(string.ascii_lowercase):      
  for k, letter_k in enumerate(key):
    if letter_k == alpha:
      if choice == 'e':
        #Encrypting
        coded[k] = coded[k] + n
      elif choice == 'd':
        #Decrypting
        coded[k] = (26 + coded[k] - n)

for num, c in enumerate(coded):
  coded[num] = c%26
encryption = [""]*len(coded)

numToLetter(encryption,coded)

print ("".join(encryption))