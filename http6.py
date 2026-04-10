import socket 
import ssl

host = "ptl-25e38bc48e89-eba316e8c1d6.libcurl.me"
port = 443
path = "/pentesterlab"
body = "key=please"


request = f"POST {path} HTTP/1.1\r\n"
request += f"Host: {host}\r\n"
request += f"Content-Type: application/x-www-form-urlencoded\r\n"
request += f"Content-Length: {len(body)}\r\n"
request += "Connection: close\r\n"
request += "\r\n"
request += body

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
s_secure = context.wrap_socket(s, server_hostname=host)

s_secure.connect((host,port))
s_secure.sendall(request.encode())

response = b""

while True :
    chunk = s_secure.recv(4096)
    if not chunk:
        break
    response +=chunk

result = response.decode(errors="ignore")

header = result.split('\r\n\r\n', 1)

print(header[1])