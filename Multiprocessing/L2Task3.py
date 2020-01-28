import multiprocessing
from multiprocessing import Queue
from random import random

def counter(q):
    for _ in range(100):
        if q.empty():
            q.put(random()*20-10)

def SaveToFile(filename,data):
    filename.encode('unicode_escape')
    file = open(filename, 'a', encoding="utf8")
    file.write((data))
    file.write('\n')
    file.close()

if __name__ == '__main__':

    q=Queue()
    r=Queue()

    p1 = multiprocessing.Process(target=counter,args=(q,))
    p2 = multiprocessing.Process(target=counter, args=(r,))

    p1.start()
    p2.start()

    while 1:
        if not q.empty():
            if not r.empty():
                val=q.get()+r.get()
                print(val)
                SaveToFile('Counters.txt',str(val))

