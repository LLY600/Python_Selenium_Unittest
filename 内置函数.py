#_*_coding:utf-8_*_
#@Author:LLY


from functools import reduce
def f(s):
    if s != 'a':
        return s
res = filter(f, ['a', 'b', 'c'])
print('res:', list(res))

def f1(a):
    return a + ':hello'
res1 = map(f1, ['a', 'b', 'c'])
res2 = filter(f1, ['a', 'b', 'c'])
print('res1:', list(res1))
print('res2:', list(res2))

def f2(x,y):
    return x+y
print(reduce(f2, range(1,101)))
#reduce结果就是一个值

