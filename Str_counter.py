# Asks the user for a word and a letter.
# A count value is returned for the number of times the letter appears in the given word.
from typing import Counter

def count(word, letter):
    counter = 0
    for let in word:
        if let == letter:
            counter += 1
    return counter

word = input("Please enter a word: ")
letter = input("Which letter would you like to count? ")

count_letters = count(word, letter)
print(count_letters)