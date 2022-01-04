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
    print(recievedData.decode()[:3000])
    print(f"\n{len(recievedData.decode())} characters")

except:
    print("Error: improperly formatted or non-existent URL")

input()