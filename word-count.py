#Count Words in a String 
#Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

def wordCount(text):
  return len(text.split())

count = 0
file = open("test.txt","r")
for line in file:
  count = count + wordCount(line)
file.close()

print(count)