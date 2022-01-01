import re

fname = input("Enter file: ")
fhandle = open(fname)

numList = list()

for line in fhandle:
    line = line.rstrip()
    num = re.findall("^New Revision: ([0-9]+)", line)
    if (len(num) == 1): 
        numList.append(int(num[0]))

print(sum(numList)/len(numList))