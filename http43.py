import websocket 
import ssl


host = "ptl-413f469eaa5a-b6bbc5c4569a.libcurl.me" 

url = f"wss://{host}/pentesterlab" 

print(f"[*] Connecting to {url}...")


ws = websocket.WebSocket(websocketsslopt={"cert_reqs": ssl.CERT_NONE})

try:
    
    ws.connect(url)
    print("[+] Connection established!")

    
    payload = "key"
    print(f"[*] Sending payload: {payload}")
    ws.send(payload)

    
    response = ws.recv()
    print("[+] Response received:")
    print(response)

finally:
    
    ws.close()
    print("[*] Connection closed.")