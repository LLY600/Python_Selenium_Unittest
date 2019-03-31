import paramiko

private_key = paramiko.RSAKey.from_private_key_file('key_192.168.119.129_22.pub')
#创建ssh对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#paramiko.ssh_exception.SSHException: Server '192.168.119.129' not found in known_hosts
#连接服务器
ssh.connect(hostname='192.168.119.129', port=22, username='root', key_filename=private_key)
#执行命令
stdin, stdout, stderr = ssh.exec_command('top -bn 1')
#获取命令结果
result_correct = stdout.read().decode()
result_erro = stderr.read().decode()
result = result_correct if result_correct else result_erro
print(result)