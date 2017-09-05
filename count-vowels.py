#Count Vowels
#Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

input_string = input("Please type a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count =[0]*5
for n,vowel in enumerate(vowels):
  for a in input_string:
    if a == vowel:
      vowel_count[n] = vowel_count[n]+1
print("Total number of vowels: " + str(sum(vowel_count)))
for n, vowel in enumerate(vowels):
  print("Total of " + str(vowel.upper()) + ":" + str(vowel_count[n]))