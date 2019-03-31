#_*_coding:utf-8_*_
#@Author:LLY

#跟操作系统交互
import os

# print(os.getcwd())
# print(os.chdir(u'e:/python_project/dir1'))
# print(os.getcwd())
# print(os.curdir)
# print(os.pardir)
# os.makedirs('a/b/c/')
# os.removedirs('a/b/c/')  # 只能删除空文件
# os.mkdir('w')
# os.mkdir('a\\b')
# print(os.listdir('E:\python_project'))
# os.remove('file.txt')  # 只能删除文件，不能删除文件夹
# os.rename('yum.log', 'xxx.log')
# print(os.stat('xxx.log').st_size)
# print(os.sep)
# print(os.pathsep)
# print(os.system('dir'))
# print(os.environ)
# print(os.path.abspath('./xxx.log'))
# print(os.path.split(r'E:\python_project\xxx.log'))
print(os.path.dirname(r'E:\python_project\xxx.log'))