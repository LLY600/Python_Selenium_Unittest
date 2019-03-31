#_*_coding:utf-8_*_
#@Author:LLY


# 匹配字符串
import re

s = 'hello world'
# print(s.find('ll'))
# print(s.replace('ll', 'xx'))
# print(s.split(' '))
# print(re.findall('w\w{2}l', s))
# print(re.findall('w..l',s)) # 点只能代指任意一个字符
# print(re.findall('^h...o', s))
# print(re.findall('hello$', 'ahfghhello'))
# print(re.findall('h.*o', 'shool')) * [0, +00]
# print(re.findall('h+llo', 'hllo'))  # + [1, +00]
# print(re.findall('h?e', 'helhheloei'))# ? [0, 1]
# print(re.findall('a{1,2}b{2}', 'aaabb'))
#
# 总结：
# * = {0， +00}
# + = {1， +00}
# ？ = {0，1}