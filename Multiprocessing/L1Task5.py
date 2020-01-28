import os
import multiprocessing
from multiprocessing import Queue


def load_files(queue):
    filelist = os.listdir()
    for filename in filelist:
        if filename.endswith('.txt'):
            filename.encode('unicode_escape')
            file = open(filename, 'r', encoding="utf8")
            list = file.read().split('\n')
            file.close()
            queue.put(len(list))
    queue.put('END')


def results(queue):
    while 1:
        if not queue.empty():
            item=queue.get()
            if item=='END':
                break
            else:
                print(item)



if __name__ == '__main__':
    q=Queue()
    p1 = multiprocessing.Process(target=load_files,args=[q])
    p2 = multiprocessing.Process(target=results, args=[q])

    p1.start()
    p2.start()