# Find and count senders from a given Mbox.txt file

fname = input("Enter a file name: ")

try:
    fhandle = open(fname)
except:
    print("File not found.")
    quit()

counter = 0
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if words == 0 or not line.startswith("From "):
        continue
    counter += 1
    print(words[1])
    
print("There were", counter, "lines in the file with From as the first word")