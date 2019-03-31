import time
import threading


def run():
    lock.acquire()
    global num
    num += 1
    lock.release()

lock = threading.Lock()
num = 0
t_objs = []
for i in range(50):
    t = threading.Thread(target=run)
    t.start()
    t_objs.append(t)


for t in t_objs:
    t.join()

print('num:', num)
