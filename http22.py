import socket
import ssl

host = "ptl-27febb3beaad-e0f9628480a6.libcurl.me"
port = 443
path = "/pentesterlab"

request = f"POST {path} HTTP/1.1\r\n"
request += f"Host: {host}\r\n"
request += "X-HTTP-Method-Override: HACK\r\n"
request += "Connection: close\r\n"
request += "\r\n"

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