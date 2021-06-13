import socket


req = b'Hello TCP!'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 1234))
    s.send(req)
    rsp = s.recv(1024)

print(repr(rsp))
