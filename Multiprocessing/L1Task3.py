import time
import threading
import multiprocessing
from multiprocessing import Pool


def sleep(x):
    time.sleep(1)

def sleep_Pool():
    start = time.perf_counter()
    numbers = range(4)
    p=Pool()
    p.map(sleep, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def sleep_Pool_async():
    start = time.perf_counter()
    numbers = range(4)
    p=Pool()
    p.map_async(sleep, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def sleep_threading():
    start = time.perf_counter()

    threads=[]

    for _ in range(4):
        t=threading.Thread(target=sleep,args=[0])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Threads: finished in {round(finish - start, 2)} second(s)')

def sleep_multiprocessing():
    start = time.perf_counter()

    proccesses=[]

    for _ in range(4):
        p=multiprocessing.Process(target=sleep,args=[0])
        p.start()
        proccesses.append(p)

    for p in proccesses:
        p.join()

    finish = time.perf_counter()
    print(f'Multiprocessing (no Pools): finished in {round(finish - start, 2)} second(s)')

def sleep_sequential():
    start = time.perf_counter()

    for i in range(4):
        sleep(i)

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    print("Sleep function:")
    sleep_sequential()
    sleep_Pool()
    sleep_Pool_async()
    sleep_threading()
    sleep_multiprocessing()