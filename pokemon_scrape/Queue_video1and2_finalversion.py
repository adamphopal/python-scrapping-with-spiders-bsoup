# -*- coding: utf-8 -*-
#Using threading with queue
#queing allows you to make sure you dont save the data unless its been modified
#and you wont try to modify data if you dont have any
#3 types of queue: Fifo(first in n out), Lifo(last in n out), priortiy(takes lowest value first)
import queue
import threading
import time


def putting_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')

q = queue.Queue()
t = threading.Thread(target = putting_thread, args = (q,),daemon = True)
t.start()

q.put(5)
print(q.get())
print('first item gotten')
print(q.get())
print('finished')

#intializing a variable to q.get()

x =q.get()

print(x)
