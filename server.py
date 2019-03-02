import socket  
from ca import GetCert
import base64

cert = GetCert()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 9500))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        conn.send(cert)
        while True:
            data = conn.recv(1024)
            print("encrypted data: ", data)
            print("decrypted data: ", base64.b64decode(data).decode('utf-8'))
            conn.send(base64.b64encode('secret response'.encode('utf-8')))