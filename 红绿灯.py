import time
import threading

event = threading.Event()
def light():
    count = 1
    event.set()
    while True:
        if count > 5 and count < 11:
            event.clear()
            print('\033[41;1mred   light\033[0m')
        elif count >= 10:
            event.set()
            count = 0
        else:
            print('\033[30;42mgreen light\033[0m')
        time.sleep(1)
        count +=1


def car(name):
    while True:
        if event.is_set():
            print('[%s] running' % name)
            time.sleep(1)
        else:
            print('[%s] waiting' % name)
            event.wait()


l = threading.Thread(target=light,)
l.start()

car1 = threading.Thread(target=car, args=("TSL", ))
car1.start()

