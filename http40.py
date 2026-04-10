import ssl
import socket


host = "ptl-335f2c5ecd00-87213aad28c3.libcurl.me"
port = 443
path = "/pentesterlab"

body = "key: please"


request = f"POST {path} HTTP/1.1\r\n"
request += f"Host: {host}\r\n"
request += f"Content-length: {len(body)}\r\n"
request += f"Content-Type: application/yaml\r\n"
request += "Connection: close\r\n"
request += "\r\n"
request += body

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
s_secure = context.wrap_socket(s, server_hostname=host)

s_secure.connect((host, port))
s_secure.sendall(request.encode())

response =b''

while True:
    chunk = s_secure.recv(4096)
    if not chunk:
        break
    response += chunk

full = response.decode(errors='ignore')
split = full.split('\r\n\r\n', 1)
body = split[1]

print(body)