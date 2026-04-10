import socket

host = "ptl-0682f0f60f63-65e3f9bc698e.libcurl.me"
port = 80
request  = "GET /pentesterlab HTTP/1.1\r\n"
request  += f"Host: {host}\r\n"
request += "\r\n"
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(request.encode())

response = b''

while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    response += chunk

print(response.decode())

s.close()
