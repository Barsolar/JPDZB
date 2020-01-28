import os
import re
import time
from multiprocessing import Pool


def load_files(filename,thr=5):
       if filename.endswith('.txt'):
            filename.encode('unicode_escape')
            file = open(filename, 'r', encoding="utf8")
            list = file.read().split('\n')
            n=0
            for str in list:
                temp = re.split(' |;|,|\n|\t',str)
                for word in temp:
                    if len(word)>thr:
                        n+=1
            file.close()
            print(f'File {filename} has {n} of words of length >= {thr}')

def file_Pool(filelist):
    start = time.perf_counter()

    p=Pool()
    p.map(load_files, filelist)
    p.close()
    p.join()

    finish = time.perf_counter()
    print(f'Pool: finished in {round(finish - start, 2)} second(s)')

def file_Pool_async(filelist):
    start = time.perf_counter()

    p=Pool()
    p.map_async(load_files, filelist)
    p.close()
    p.join()

    finish = time.perf_counter()
    print(f'Pool_async: finished in {round(finish - start, 2)} second(s)')

def file_sequential(filelist):
    start = time.perf_counter()

    for filename in filelist:
        load_files(filename,5)

    finish = time.perf_counter()
    print(f'Sequential: finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    filelist = os.listdir()

    file_sequential(filelist)
    file_Pool(filelist)
    file_Pool_async(filelist)