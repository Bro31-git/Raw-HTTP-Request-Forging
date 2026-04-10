import ssl
import socket

boundary ="---my custom boundary"
body = f"--{boundary}\r\n"
body += f"Content-Disposition: form-data; name='test'\r\n\r\n"
body += f"HelloLab\r\n"
body += f"--{boundary}--"

host = "ptl-6c8740e5d672-d0b027072561.libcurl.me"
port = 443
path = "/pentesterlab"

request = f"POST {path} HTTP/1.1\r\n"
request += f"HOST: {host}\r\n"
request += f"Content-Length: {len(body)}\r\n"
request += f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
request += f"Connection: cloase\r\n"
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
header = split[1]

print(header)