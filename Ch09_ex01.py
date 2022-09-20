# Reads words from a text file and stores them in a dict. 

fhandle = open("words.txt")

words_dict = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        words_dict[word] = ''

print(words_dict)