import re

fname = "mbox.txt"
fhandle = open(fname)

regex = str(input("Enter a regular expression: "))
matchCount = int()

for line in fhandle:
    line = line.rstrip()
    if (len(re.findall(regex, line))): #1 = true
        matchCount += 1
    
print(f"{fname} had {matchCount} lines that matched {regex}")