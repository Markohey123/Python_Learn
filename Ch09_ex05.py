# Create a dict of domain names.

fname = input('Enter a file name: ')

try:
    fhandle = open(fname)
except:
    print('File name not valid:', fname)
    quit()

domains = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or not line.startswith('From'):
        continue
    email = words[1]
    name, domain = email.split('@')
    domains[domain] = domains.get(domain, 0) + 1

print(domains)