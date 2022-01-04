import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("URL: ")

try:
    host = url.split("/")[2]

    mysocket.connect((host, 80))
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
    mysocket.send(cmd)

    while (True):
        data = mysocket.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end="")

    mysocket.close()

except:
    print("Error: improperly formatted or non-existent URL")

input()