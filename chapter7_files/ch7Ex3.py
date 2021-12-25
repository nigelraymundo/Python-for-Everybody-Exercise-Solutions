fname = input("Enter the file name: ")


if (fname == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        fhandle = open(fname)
    except:
        print(f"File cannot be opened: {fname}")
        quit()

    counter = 0
    for line in fhandle:
        if(line.startswith("From ")):
            counter += 1
    print(f"There were {counter} subject lines in {fname}")