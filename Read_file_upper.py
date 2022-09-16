# In this program a file is opened and each line read and printed in uppercase.

fname = input("Enter a file name: ")
fhand = open(fname)

for line in fhand:
    line_up = line.upper()
    line_up = line_up.rstrip()
    print(line_up)