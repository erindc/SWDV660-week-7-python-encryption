import uuid

cert = b'1234'

def GetCert():
    return cert

def ValidateCert(clientCert):
    if str(clientCert) == str(cert):
        return True
    return False
