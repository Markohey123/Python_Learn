# This program takes a string and prints it backwards, each letter on a new line.

word = input("Please enter any word: ")

index = len(word)
while index > 0:
    letter = word[index-1]
    index -= 1
    print(letter)