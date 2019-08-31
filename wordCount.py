import re
import sys
#Open File
file = open(sys.argv[1], "r")
#Clear unwanted special characters,split each line into words and put them into a list.
list = re.sub("[^'A-Za-z-\s]+", "", file.read()).replace("-", " ").replace("'"," ").lower().strip().split()
#Sort the list
list.sort()
#Create Disctionary
dictionary = {}
#Iterate trhugh dictionary and if a word is found using the key update value of seen the word
for word in list:
    if word in dictionary.keys():
        dictionary[word] = dictionary.get(word) + 1
    else:
        dictionary[word] = 1
#Open text if not found create it.
f = open(sys.argv[2], "w")
#Iterate through the dictionary and write key and value to each line
for word in dictionary:
    f.write(word + " " + str(dictionary[word]) + "\n")
#Close File
f.close()
