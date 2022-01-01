fname = input("Enter a file name: ")

fhandle = open(fname)

senderDict = dict()
for line in fhandle:
    if (line.startswith("From ")):
        senderDict[line.split()[1]] = senderDict.get(line.split()[1], 0) + 1

#senderList = list()

#for (key, value) in senderDict.items():
#    senderList.append((value, key))

senderList = sorted([(count, sender) for (sender, count) in senderDict.items()], reverse = True)


print(senderList[0][1], senderList[0][0])

#print(sorted([(count, sender) for (sender, count) in senderDict.items()], reverse = True)[0])