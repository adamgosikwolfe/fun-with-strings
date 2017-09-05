#Enter a string and the program will reverse it and print it out.

input_string = input("String to reverse: ")
b=""
for x in input_string:
  b = x + b

print(b) 
