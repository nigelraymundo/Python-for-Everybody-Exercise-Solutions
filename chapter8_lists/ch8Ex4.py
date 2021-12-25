fhandle = open("romeo.txt")
wordList = [] #initializes list

for line in fhandle: 
    for word in line.split():
        if (word not in wordList): #checks if an element of the list of words in each line is in the wordList list, adds it in if not
            wordList.append(word)
wordList.sort() #capital letters have lower values, shows up first
print(wordList)
