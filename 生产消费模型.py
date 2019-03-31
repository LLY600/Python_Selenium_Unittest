import threading,time
import queue


q = queue.Queue(maxsize=10)
def producer(name):
    count = 1
    while True:
        q.put('骨头 %s' % count)
        print('生产了骨头%s' % count)
        count +=1
        time.sleep(1)

def consumer(name):
    while True:
        print('%s 取到 %s，并吃了它' % (name, q.get()))
        time.sleep(1)

p = threading.Thread(target=producer, args=('lly', ))
c = threading.Thread(target=consumer, args=('heitu', ))
c2 = threading.Thread(target=consumer, args=('heitu2', ))
c3 = threading.Thread(target=consumer, args=('heitu3', ))
p.start()
c.start()
c2.start()
c3.start()


