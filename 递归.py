#_*_coding:utf-8_*_
#@Author:LLY



#1.自己调用自己
#2.必须有一个结束条件
#3.递归可以实现的，用循环都可以实现
#4.效率低，递归层次过多会导致栈溢出
#5.计算机函数调用是通过栈stack这种数据结构实现的
#6.当函数调用，栈增加一层栈帧，当函数返回，减少一层栈帧
#7.栈不是无限大，当递归次数过多，会导致栈溢出


def foo(n):
    if n == 1:
        return 1
    return n * foo(n-1)

print(foo(5))

#0,1,1,2,3,5,8,13...
def fb(n):
    if n in (0, 1):
        return n
    return fb(n-1)+fb(n-2)
print(fb(0))