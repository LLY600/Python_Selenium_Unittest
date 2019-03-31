#_*_coding:utf-8_*_
#@Author:LLY

import random

# print(random.random())
# print(random.randint(1, 3)) # 包括3
# print(random.choice('asdfg'))
# list = [1,2,3,4]
# random.shuffle(list) #打乱顺序
# print(list)
# print(random.sample(([1,2],3,'4'), 2))
# print(random.randrange(1, 3)) #不包括3

# print(random.randrange(10))
# print(chr(random.randrange(65, 91)))
# print(random.choice([1,'a',3,'b']))
def verify_code():
    code = ''
    for i in range(5):
        ele = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(ele)
    print(code)

verify_code()

