import socket
from ca import *
import base64


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('', 9500))
    s.sendall(b'Initial message')
    cert = s.recv(1024)
    valid = ValidateCert(cert)
    if valid:
        for i in range(9):
            secretData = "super secret " + str(i)
            s.sendall(base64.b64encode(secretData.encode('utf-8')))
            data = s.recv(1024)
            print('encrypted: ', data)
            print('decrypted: ', base64.b64decode(data).decode('utf-8'))
        exit()
    else:
        print('Invalid connection')
        exit()
