import ssl
import socket
import base64


host = "ptl-c98d8abd3527-9a42f3309869.libcurl.me"
port = 443
path = "/pentesterlab"

#or
#body = "key:\n"
#body += "  - please\n"
#body += "  - please2\n"
credentials = "key:please"
encoded_creds = base64.b64encode(credentials.encode()).decode()

request = f"GET {path} HTTP/1.1\r\n"
request += f"Host: {host}\r\n"
request += f"Authorization: Basic {encoded_creds}\r\n"
request += "Connection: close\r\n"
request += "\r\n"


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