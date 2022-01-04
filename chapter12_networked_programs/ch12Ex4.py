from urllib import request
import re


url = input("URL: ")
recievedData = bytes()

try:
    fhand = request.urlopen(url)

    for line in fhand:
        recievedData += line

    pCount = re.findall("\<p.+", recievedData.decode())

    print(f"{len(pCount)} paragraphs")

except:
    print("Error: improperly formatted or non-existent URL")

input()