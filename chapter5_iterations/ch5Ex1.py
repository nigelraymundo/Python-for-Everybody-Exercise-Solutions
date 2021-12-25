total = 0
count = 0

while True:
    entry = input("Enter a number: ")
    try:
        total += float(entry)
        count += 1
    except:
        if (entry == "done"):
            break
        else:
            print("Invalid input")

average = (total / count)

print(f"{total} {count} {average}")