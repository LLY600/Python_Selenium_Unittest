import multiprocessing
import time


def run(name):
    time.sleep(1)
    print('hello,', name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=run, args=('lly',))
    p.start()


