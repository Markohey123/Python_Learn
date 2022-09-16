# This program takes a series of numbers and calculates the total, count and average of all input numbers.
# The program runs until a user enters the value "done".
count = 0
total = 0
average = 0

try:
    while True:
        number = input("Enter a number: ")
        if number.lower() != "done":
            int_num = int(number)
            count += 1
            total += int_num
        else:
            break
    average = total / count
    print(total, count, average)
except:
    print("Invalid input!")