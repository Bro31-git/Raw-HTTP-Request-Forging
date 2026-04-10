import socket
import ssl

host = "ptl-0682f0f60f63-65e3f9bc698e.libcurl.me"
path = "/pentesterlab"
port = 443

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
context = ssl.create_default_context()
secure = context.wrap_socket(s,server_hostname=host)

request = f"GET {path}  HTTP/1.1\r\n"
request += f"Host:{host}\r\n"
request += "\r\n"
secure.connect((host,port))
secure.sendall(request.encode())

response = b""
while True:
    chunk = secure.recv(4090)
    if not chunk:
        break
    response += chunk

print(response.decode())
secure.close()