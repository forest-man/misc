#!/usr/bin/env python

import time
import argparse
from multiprocessing import Manager, Pool, Process, cpu_count
eat = 30

def mem_cons(n):
        print(n)
        list=[]
        while n > 1:
            GB = 1024*1024*1024
            a = "a" * (n * GB)
            time.sleep(10)
            list.append(a)
            print("Some memory was eaten")
            n = n/2 
            print(n)

        print("It's time for a sleep for 10 seconds")
        time.sleep(10)

def multiproc(func):
    p1 = Process(target=mem_cons, args=(func,))
    p1.start()
    p1.join()

multiproc(eat)

