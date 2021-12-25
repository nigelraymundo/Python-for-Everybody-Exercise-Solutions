count = 0

while True:
    entry = input("Enter a number: ")
    try:
        if (count == 0):
            maxNum = float(entry)
            minNum = float(entry)
        elif (float(entry) > maxNum):
            maxNum = float(entry)
        elif (float(entry) < minNum):
            minNum = float(entry)
        count += 1
    except:
        if (entry == "done"):
            break
        else:
            print("Invalid input")

print(f"Maximum number: {maxNum}")
print(f"Minimum number: {minNum}")

