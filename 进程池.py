from multiprocessing import Process,Pool
import time

def Foo(i):

    time.sleep(2)
    return i + 100

def Bar(arg):
    print('')

pool = Pool(5)

for i in range(10):
    pool.apply(func=Foo, args=(i,))


print('end')
pool.close()
pool.join()