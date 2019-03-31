#_*_coding:utf-8_*_
#@Author:LLY

import copy
s = [[1, 2], 3, 4]
# s1 = s.copy()
# s1 = s[:]也可以
s1 = copy.copy(s)
s: [[1, 2], 3, 4]
    # 拷贝的s1: [[1, 2], 3, 4]
    # s1更改后的s1: [[1, 22], 3, 4]
    # s1更改后的s: [[1, 22], 3, 4]
# s1 = copy.deepcopy(s)
    # s: [[1, 2], 3, 4]
    # 拷贝的s1: [[1, 2], 3, 4]
    # s1更改后的s1: [[1, 22], 3, 4]
    # s1更改后的s: [[1, 2], 3, 4]

print('s:', s)
print('拷贝的s1:', s1)
s1[0][1] = 22
print('s1更改后的s1:', s1)
print('s1更改后的s:', s)
