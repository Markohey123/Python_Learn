# Find unique words in a subset written by Shakespear.

fhandle = open('romeo.txt')
unique_words = []

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)

unique_words.sort()
print(unique_words)