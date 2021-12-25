fname = input("Enter the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist")
    quit()

counter = 0
total = 0
for line in fhandle:
    if (line.startswith("X-DSPAM-Confidence")):
        counter += 1
        total += float(line[line.find(":") + 1:].strip()) #line sliced, stripped, and converted to float
print(f"Average spam confidence: {total / counter}")