fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
    print(type(fhandle))
except:
    print("File does not exist")
    quit()

#for line in fhandle:
    #print(line.rstrip().upper())