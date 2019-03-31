#_*_coding:utf-8_*_
#@Author:LLY


import hashlib

m = hashlib.md5()
m.update('123456'.encode('utf-8'))
# print(m.digest())#十进制
print(m.hexdigest()) #十六进制
m.update('789101'.encode('utf-8'))
print(m.hexdigest())
m1 = hashlib.md5()
m1.update('789101'.encode('utf-8'))
print(m.hexdigest())

m2 = hashlib.sha256()  # 算法复杂一些
m2.update('123456'.encode('utf-8'))
print(m2.hexdigest())
