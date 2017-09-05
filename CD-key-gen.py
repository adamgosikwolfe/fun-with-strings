#CD Key Generator
#Generates a unique key for your applications to use based on some arbitrary algorithm that you can specify. Great for software developers looking to make shareware that can be activated.

#12 character key
#randomly generate 12 numbers
#Choose 6 numbers randomly to become letters
import random 
import string

key_length = 24
alpha_amount = key_length//2
bunch_size = 3
alpha_slots=random.sample(range(1, key_length), alpha_amount)
key = [""]*key_length

for n in range(0, key_length):
  key[n] = random.randint (0,9)

for slot in alpha_slots:
  key[slot] = random.choice(string.ascii_uppercase)

key = ''.join(str(e) for e in key)
key = '-'.join(key[i:i+bunch_size] for i in range(0, len(key), bunch_size))

print(key)