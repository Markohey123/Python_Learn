# Prompt user for list of numbers until "done" is entered. Max and min of numbers is printed as result.
  
numbers = []
while True:
    number = input("Enter a number: ")
    try:
        if number == 'done':
            break
        int_num = int(number)
    except:
        print("Enter an integer.")

    numbers.append(int_num)

print("Maximum: ", float(max(numbers)))
print("Minimum: ", float(min(numbers)))