import threading
import time

def test(n):
    print(n)
    time.sleep(2)
    print(n, threading.current_thread())
start_time = time.time()
t_objs = []
for i in range(10):
    t = threading.Thread(target=test, args=('t%s' % i,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()
print(time.time()-start_time)

# #继承式调用
# class MyThread(threading.Thread):
#     def __init__(self, n):
#         super(MyThread, self).__init__()
#         self.n = n
#     def run(self):
#         print(self.n)
# if __name__ == '__main__':
#
#     t1 = MyThread('t1')
#     t1.start()
#     t2 = MyThread('t2')
#     t2.start()