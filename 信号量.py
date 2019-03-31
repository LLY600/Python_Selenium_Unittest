import time
import threading
import semaphore


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread %s' % n)
    semaphore.release()


if __name__ == '__main__':
    num = 0