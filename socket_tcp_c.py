import socket
from time import ctime

tcp_c = socket.socket()
tcp_c.connect(('localhost', 12306))

while True:
    data = input('>>:')
    if not data:
        break
    tcp_c.send(data.encode('utf-8'))
    data = tcp_c.recv(1024)
    if not data:
        break
    print(data)
tcp_c.close()