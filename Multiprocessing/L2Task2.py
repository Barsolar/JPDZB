import multiprocessing
from multiprocessing import Lock, Manager



def add(table,lock):
    lock.acquire();
    for _ in range(10):
        table.append(table[-1]+1);
    lock.release();

def sub(table, lock):
    lock.acquire();
    for _ in range(10):
        table.append(table[-1] - 1);
    lock.release();

if __name__ == '__main__':

    manager=Manager();
    l=manager.list();
    l.append(0);
    lock=Lock();

    p1 = multiprocessing.Process(target=add,args=[l,lock])
    p2 = multiprocessing.Process(target=sub, args=[l,lock])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(l)