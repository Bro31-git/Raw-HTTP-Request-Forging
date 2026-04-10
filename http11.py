import socket
import ssl

host = "ptl-f9730874d7d2-55f4c2a5d164.libcurl.me"
port = 443
path = '/pentesterlab?key=please'
body = 'key=please'
content_length = len(body)


request = f"POST {path} HTTP/1.1\r\n"
request += f"Host: {host}\r\n"
request += f"Content-Type: application/x-www-form-urlencoded\r\n"
request += f"Content-Length: {content_length}\r\n" 
request += "Connection: close\r\n"
request += "\r\n"

request += body

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
context = ssl.create_default_context()
s_secure = context.wrap_socket(s, server_hostname=host)

s_secure.connect((host,port))
s_secure.sendall(request.encode())

response = b""

while True:
    chunk = s_secure.recv(4096)
    if not chunk:
        break
    response +=chunk

full_response = response.decode(errors='ignore')
splits = full_response.split('\r\n\r\n',1)

body_info = splits[1]

print(body_info)

