fileName = str(input("Enter a file name: "))

fhandle = open(fileName)
senderCount = dict()

for line in fhandle:
    if (line.startswith("From") and len(line.split()) >= 3):
        #print((line.split()[1]).split("@", 1)[1])
        senderCount[(line.split()[1]).split("@", 1)[1]] = senderCount.get((line.split()[1]).split("@", 1)[1], 0) + 1
    
print(senderCount)