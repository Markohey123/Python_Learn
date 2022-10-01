# Categorize each mail by which day of the week the commit was done.

fname = input('Enter a file name: ')

try:
    fhandle = open(fname)
except:
    print('File name not valid: ', fname)
    quit()

days = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or not line.startswith('From'):
        continue
    days[words[2]] = days.get(words[2], 0) + 1

print(days)