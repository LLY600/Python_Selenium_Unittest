def bulk(self):
    print('%s is bulking' % self.name)

class Dog(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('%s is eating' % self.name)

d = Dog('dog')
choice = input('>>:').strip()



if hasattr(d, choice):
    # delattr(d, choice)
    getattr(d, choice)

else:
    setattr(d, choice, bulk)  # d.talk = bulk
    func = getattr(d, choice)
    print(func(d))
# print(d.name)
# setattr(x, 'y', v) is equivalent to ``x.y = v''  v是一个内存对象
#hasattr（obj,name_str）判断一个对象obj里是否有对应name_str字符串的方法
#getattr（obj,name_str）根据字符串去获取obj对象里的对应的方法的内存地址