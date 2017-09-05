#Check if Palindrome
#Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

input_string = input("Let's check for a palindrome! Please type a string: ")
word_length = len(input_string)
halfway = word_length//2
first_half = input_string[:halfway]
second_half = input_string[halfway+word_length%2:]
palindrome = bool(first_half == second_half[::-1])
print(palindrome)