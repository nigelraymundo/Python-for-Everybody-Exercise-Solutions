from urllib import request

url = input("URL: ")
recievedData = bytes()

try:
    fhand = request.urlopen(url)

    for line in fhand:
        recievedData += line

    print(recievedData.decode()[:3000])
    print(len(recievedData.decode()))

except:
    print("Error: improperly formatted or non-existent URL")

input()