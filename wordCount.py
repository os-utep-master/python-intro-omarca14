import re

file = open("speech.txt", "r")
list = re.sub("[^A-Za-z0-9-" "]+", " ", file.read()).lower().strip().split()
list.sort()
dictionary = {}
counter = 1
for word in list:
    if word in dictionary.keys():
        dictionary[word] = dictionary.get(word) + 1
    else:
        dictionary[word] = counter

f = open("Dictionary.txt","w")
for word in dictionary:
    f.write(word+" "+str(dictionary[word])+"\n")
f.close()
print(dictionary)
