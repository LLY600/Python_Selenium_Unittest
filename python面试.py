# 1.生成随机数
# import random
# print(random.random())
# print(random.randint(2, 10))
# print(random.randrange(1, 10, 2))
# list = [2, 10, 'a', 12.34]
# print(random.choice(list))
# print(random.sample(list, 2))

#2.字符串逆序
# s = 'abcde'
# print(s[::-1])
# l = list(s).__reversed__()
# print(''.join(l))


#3.判断是否为回文字符串
# def hw(s):
#     s1 = s[::-1]
#     if len(s) >= 2 and s == s1:
#         return True
#     else:
#         return False
# print(hw('abad'))


# 4.随机生成100个数，写入文件
# import random
# try:
#     with open('test.text', 'w') as f:
#         for i in range(0, 100):
#             f.write(str(random.randint(1, 9999)))
#             f.write('\n')
# except IOError as e:
#     print(e)


# 5.将字典键进行排序
# dict = {'a': 1, 'c': 2, 'b': 3, 'aa': 4}
# l = dict.items()
# print(sorted(l, key=lambda x: x[0], reverse=True))
# [('c', 2), ('b', 3), ('aa', 4), ('a', 1)]

#6.列表嵌套排序
# list = [[1, 3], [2, 5], [4, 7]]
# list_copy = list[::]
# list_copy.sort(key=lambda x: x[0], reverse=True)
# print(list)
# print(list_copy)

# 7.对列表元素去重

# #方法1
# list1 = [1, 2, 2, 3, 3, 4, 5]
# list1_copy = list1[::]
# print(list(set(list1)))
#
# #方法2
# a = dict.fromkeys(list1)
# print(list(a))
#
# #方法3
# for i in list1_copy:
#     if list1_copy.count(i) > 1:
#         list1_copy.remove(i)
# print(list1_copy)
#
# # 方法4
# def l(x,y):
#     if y in x:
#         return x
#     else:
#         return x + [y]
# from functools import reduce
# reduce(lambda x, y: x if y in x else x + [y], [[]] + list1)


#8.去重字符串
# s = 'abcabdagdajkdafhljdak'
# a = ''.join(list(set(list(s))))
# print(a)


# 9.读取硬盘文件，打印到屏幕
# import chardet
# with open('test.txt', 'r') as f:
#     content = f.read()
#     content1 = f.readlines()
#     content2 = f.readline()
#     print(content)
#     print(chardet.detect(content.encode()))
#     print(content1)
#     print(content2)

