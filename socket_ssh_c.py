import socket
import os


client = socket.socket()
client.connect(('localhost', 9998))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res = client.recv(1024)
    print(cmd_res)
client.close()