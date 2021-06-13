import socket

req = b'Hello, TCP!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
s.send(req)
res = s.recv(1024)
print(res)
s.close()
