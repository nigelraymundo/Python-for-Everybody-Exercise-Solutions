fhandle = open("mbox-short.txt")
fromCount = 0 #counts lines beginning with "From"

for line in fhandle:
    if (line.startswith("From: ")): #checks if line starts with "From"
        fromCount += 1 #iterates variable
        print(line.split()[1]) #prints second word in the line (email address)
print(f"There were {fromCount} lines in the file with From as the first word")