fileName = str(input("Enter a file name: "))

fhandle = open(fileName)
dayCount = dict()

for line in fhandle:
    if (line.startswith("From" ) and len(line.split()) >= 3):
        #print(line.split()[2])
        dayCount[line.split()[2]] = dayCount.get(line.split()[2], 0) + 1

print(dayCount)