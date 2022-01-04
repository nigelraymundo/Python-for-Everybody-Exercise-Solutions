import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("URL: ")
recievedData = bytes()

try:
    host = url.split("/")[2]

    mysocket.connect((host, 80))
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
    mysocket.send(cmd)

    while (True):
        data = mysocket.recv(512)
        if (len(data) < 1):
            break
        recievedData += data
        
    mysocket.close()

    #headerPos = str(recievedData).find(r"\r\n\r\n")
    #print(str(recievedData)[headerPos + 6:])

    headerPos = recievedData.decode().find("\r\n\r\n")
    print(recievedData.decode()[headerPos:].strip())

except:
    print("Error: improperly formatted or non-existent URL")

input()