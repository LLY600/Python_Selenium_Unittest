import paramiko

#创建ssh对象
transport = paramiko.Transport(('192.168.119.129', 22))
#连接服务器
transport.connect(username='root', password='ay921028')
#执行命令
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('test.txt', '/tmp/test.txt')
sftp.get('/tmp/ks-script-QuEOXG', 'yum.log')
#关闭连接
transport.close()