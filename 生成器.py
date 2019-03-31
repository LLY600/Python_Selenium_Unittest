#_*_coding:utf-8_*_
#@Author:LLY

#创建生成器两种方式
#1.（x*2 for x in range(5)）
#2.def f()
    # yield 1

# s = (x*2 for x in range(5))
# print(s)
#<generator object <genexpr> at 0x0000000002504678>

# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
#print(next(s))  StopIteration

#生成器是一个可迭代的对象
# for i in s:def f():
#     print('加yield之后直接调用f()不会打印此句')
#     yield 1#只要有yield就是一个生成器函数
#     print('加yield之后直接调用f()不会打印此句1')
#     yield 2#只要有yield就是一个生成器函数
# g = f()
# # print(g)#<generator object f at 0x0000000002514728>
# print(next(g))
# print(next(g))
    # print(i)


def bar():
    print('ok1')
    count = yield 1
    print(count)
    print('ok2')
    yield 2

b = bar()
# next(b)
#send和next差不多，只不过send可以传值

# b.send('asdfg')
# Traceback (most recent call last):
#   File "E:/python_project/生成器.py", line 39, in <module>
#     b.send('asdfg')
# TypeError: can't send non-None value to a just-started generator
s = b.send(None)  # b.send(None) = next(b)
s = b.send('asd')
#第一次send前如果没有next，只能传一个send(none)
print(s)