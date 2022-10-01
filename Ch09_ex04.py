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

max = 0
max_sender = ''
for key in emails:
    if emails[key] > max:
        max = emails[key]
        max_sender = key

print(max_sender, max)
