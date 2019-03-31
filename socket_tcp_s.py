import socket
from time import ctime

tcp = socket.socket()
tcp.bind(('localhost', 12306))
tcp.listen(5)
while True:
    print('waiting for connection...')
    conn, addr = tcp.accept()
    print('connected from:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send('{%s} %s' % (ctime(), data))
        conn.close()
tcp.close()

