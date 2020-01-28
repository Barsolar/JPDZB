import time
import threading
import multiprocessing
from multiprocessing import Pool


def loop(x):
    while x<10000:
        x+=1
        #print(x)

def loop_Pool():
    start = time.perf_counter()
    numbers=[0,0,0,0]
    p=Pool()
    p.map(loop, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def loop_Pool_async():
    start = time.perf_counter()
    numbers = numbers=[0,0,0,0]
    p=Pool()
    p.map_async(loop, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def loop_threading():
    start = time.perf_counter()

    threads=[]

    for _ in range(4):
        t=threading.Thread(target=loop,args=[0])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Threads: finished in {round(finish - start, 2)} second(s)')

def loop_multiprocessing():
    start = time.perf_counter()

    proccesses=[]

    for _ in range(4):
        p=multiprocessing.Process(target=loop,args=[0])
        p.start()
        proccesses.append(p)

    for p in proccesses:
        p.join()

    finish = time.perf_counter()
    print(f'Multiprocessing (no Pools): finished in {round(finish - start, 2)} second(s)')

def loop_sequential():
    start = time.perf_counter()

    for i in range(4):
        loop(0)

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    print("Loop function:")
    loop_sequential()
    loop_Pool()
    loop_Pool_async()
    loop_threading()
    loop_multiprocessing()