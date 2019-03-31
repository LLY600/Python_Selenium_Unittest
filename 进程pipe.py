from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    print('from parent,', conn.recv())
    conn.close()


if __name__ == '__main__':
    p_conn, c_conn = Pipe()
    p = Process(target=f, args=(c_conn,))
    p.start()
    print(p_conn.recv())
    print(p_conn.send('hello ya'))
    p.join()
