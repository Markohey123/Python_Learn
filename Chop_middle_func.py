# Chop function to remove first and last element of a list.

from tkinter import NONE

def chop(list):
    del list[0]
    del list[-1]

# Middle function takes a list and returns a new list containing all but the first and last elements.
def middle(list):
    new_list = []
    for element in list[1:-1]:
        new_list.append(element)
    return new_list

# Chop function
list_ex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
list_chopped = chop(list_ex)
print(list_ex)

# Middle function
list_b = middle(list_ex)
print(list_b)
# shows list_ex was not modified and list_b was created
print(list_ex)