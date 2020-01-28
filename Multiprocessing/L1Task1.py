import time
import math
from multiprocessing import Pool

def root(number):
    return math.sqrt(number)

def sleep(x):
    time.sleep(0.1)

def powers(x):
    for ii in range(10):
        x+=x**ii
    return x


def root_Pool():
    start = time.perf_counter()
    numbers=range(101)
    p=Pool()
    results=p.map(root,numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def root_Pool_async():
    start = time.perf_counter()
    numbers=range(101)
    p=Pool()
    results=p.map_async(root,numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def root_sequential():
    start = time.perf_counter()

    results=[]

    for n in range(101):
        results.append(root(n))

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

def sleep_Pool():
    start = time.perf_counter()
    numbers = range(101)
    p=Pool()
    p.map(sleep, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def sleep_Pool_async():
    start = time.perf_counter()
    numbers = range(101)
    p=Pool()
    p.map_async(sleep, numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def sleep_sequential():
    start = time.perf_counter()

    for i in range(101):
        sleep(i)

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

def powers_Pool():
    start = time.perf_counter()
    numbers=range(101)
    p=Pool()
    results=p.map(powers,numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def powers_Pool_async():
    start = time.perf_counter()
    numbers=range(101)
    p=Pool()
    results=p.map_async(powers,numbers)

    p.close()
    p.join()
    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def powers_sequential():
    start = time.perf_counter()

    results=[]

    for n in range(101):
        results.append(powers(n))

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    print('Root function:')
    root_sequential()
    root_Pool()
    root_Pool_async()
    print("Sleep function:")
    sleep_sequential()
    sleep_Pool()
    sleep_Pool_async()
    print('Powers function:')
    powers_sequential()
    powers_Pool()
    powers_Pool_async()