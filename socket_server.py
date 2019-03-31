import socket

server = socket.socket()  # 声明socket类型，同时生成socket连接对象
server.bind(('localhost', 6969))
server.listen()
print('waiting...')
conn, addr = server.accept()  # 等待
# conn就是客户端连过来，在服务器为其生成的一个连接实例
print(conn, addr)
print('coming！')
while True:
    data = conn.recv(1024)
    print('recv:', data)
    conn.send(data.upper())
server.close()
