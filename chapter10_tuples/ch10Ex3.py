fname = "mbox-short.txt"
fhandle = open(fname)

letterDict = dict()

for line in fhandle:
    for character in line.lower():
        if (character.isalpha()):
            letterDict[character] = letterDict.get(character, 0) + 1


for (letter, count) in sorted(letterDict.items()):
    print(letter, count)
