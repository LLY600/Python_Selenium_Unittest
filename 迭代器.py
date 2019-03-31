#_*_coding:utf-8_*_
#@Author:LLY

#生成器都是迭代器，迭代器不一定是生成器
#1.有iter方法
#2.有next方法
l = [1, 2, 3, 4]
# print(l.__iter__())
d = iter(l) # 返回一个可迭代对象
print(d.__next__())
print(next(d))




# for 循环内部三件事for i in [1,2,3,4]:
# 1.调用可迭代对象的iter方法，返回一个迭代器对象
# 2.调用迭代器的next方法
# 3.处理stopIteration异常



from collections import Iterable, Iterator


l = [1,2,3]
d = iter(l)
print(isinstance(l, Iterable))