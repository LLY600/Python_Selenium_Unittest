from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()  # 主线程
    p = Process(target=f, args=(q, ))  # 子线程
    p.start()
    print(q.get())
    p.join()
