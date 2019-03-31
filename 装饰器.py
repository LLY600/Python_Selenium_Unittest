#_*_coding:utf-8_*_
#@Author:LLY


#闭包
# def outer():
#     x = 10
#     def inner(): #内部函数
#         print(x) #引用外部环境的变量
#         return inner #内部函数inner就是一个闭包
# f = outer()
# print(f)
# print(f())


import time



# def c_time(f):
#     s_time = time.time()
#     f()
#     time.sleep(1)
#     e_time = time.time()
#     print('耗时：%s S' %(e_time-s_time))
# c_time(f)


# def c_time(f):
#     def inner():
#         s_time = time.time()
#         f()
#         time.sleep(1)
#         e_time = time.time()
#         print('耗时：%s S' %(e_time-s_time))
#     return inner
# f = c_time(f)
# f()

#
# def c_time(f):
#     def inner():
#         s_time = time.time()
#         f()
#         time.sleep(1)
#         e_time = time.time()
#         print('耗时：%s S' %(e_time-s_time))
#     return inner
#
# @c_time
# def f():
#     print('执行%s函数' % f.__name__)
# f()




# def c_time(f):
#     def inner(a, b):
#         s_time = time.time()
#         f(a, b)
#         time.sleep(1)
#         e_time = time.time()
#         print('耗时：%s S' % (e_time-s_time))
#     return inner
#
# @c_time
# def add(a, b):
#     print('执行%s函数' % add.__name__)
#     print(a+b)
# add(1,2)


# def c_time(f):
#     def inner(*a, **b):
#         s_time = time.time()
#         f(*a, **b)
#         time.sleep(1)
#         e_time = time.time()
#         print('耗时：%s S' % (e_time-s_time))
#     return inner
#
# @c_time
# def add(*a, **b):
#     print('执行%s函数' % add.__name__)
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)
# add(1,2,3,4,5)


def logger(flag=''):
    def c_time(f):
        def inner(*a, **b):
            s_time = time.time()
            f(*a, **b)
            if flag == 'T':
                print('这里是一个日志记录')
            time.sleep(1)
            e_time = time.time()
            print('耗时：%s S' % (e_time-s_time))
        return inner
    return c_time

@logger('T')
def add(*a, **b):
    print('执行%s函数' % add.__name__)
    sum = 0
    for i in a:
        sum += i
    print('函数功能实现求和：',sum)
add(1,2,3,4,5)