numList = [] #initializes list

while (True):
    entry = input("Enter a number: ")
    try: 
        numList.append(float(entry)) #converts string input to float
    except: #executes block if float is not a number
        if (entry == "done"): #beaks loop if input = "done"
            break
        else:
            print("Invalid input")
print(f"Maximum: {max(numList)}")
print(f"Minimum: {min(numList)}")