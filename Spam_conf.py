# Program searches for specific string: "X-DSPAM-Confidence: " and calculates average of all floats stored.

fname = input("Enter the file name: ")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

error = "Invalid file name."

try:
    fhand = open(fname)
except:
    print(error)
    quit()

total = 0.0
count = 0
for line in fhand:
    line = line.rstrip()
    # Skip lines we are not concerned with
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    # Process lines we want to use
    space_pos = line.find(" ")
    num_value = float(line[space_pos + 1:])
    total += num_value
    count += 1

average = total / count
print("Average spam confidence: ", average)