fname = input("Enter a file name: ")

fhandle = open(fname)

hourDict = dict()

for line in fhandle:
    if (line.startswith("From ")):
        hour = line.split()[5].split(":")[0]
        hourDict[hour] = hourDict.get(hour, 0) + 1

for (time, count) in sorted(hourDict.items()):
    print(time, count)
