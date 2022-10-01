# Read through mail log, find from whom emails were sent in dict.

fname = input('Enter a file name: ')

try:
    fhandle = open(fname)
except:
    print('File name not valid: ', fname)

emails = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or not line.startswith('From'):
        continue
    emails[words[1]] = emails.get(words[1], 0) + 1

print(emails)