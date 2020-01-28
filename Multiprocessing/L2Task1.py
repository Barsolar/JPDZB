import multiprocessing
import time
from random import random

def good_morning(send):
    for _ in range(10):
        print('good morning')
        send.send('')
        time.sleep(random()*10)
        send.recv()
    send.send("break")

def good_bye(recv):
    while 1:
        msg=recv.recv()
        if msg=='break':
            break
        print('goodbye')
        time.sleep(random()*10)
        recv.send('')

if __name__ == '__main__':

    send, recv = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=good_morning,args=[send])
    p2 = multiprocessing.Process(target=good_bye, args=[recv])

    p1.start()
    p2.start()

    p1.join()
    p2.join()