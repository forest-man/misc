import os
import sys
from multiprocessing import Process, Manager
from multiprocessing import cpu_count

def f(x):
    try:
        while True:
            x ** x
            x = x + 99999
    except KeyboardInterrupt:
        a = 1 # Just a stub for nicer output of KeyboardInterrupt exception
    

def cpu_eat(processes):
    try:
        manager = Manager()
        x = manager.dict()
        for i in range(processes):
            pi = Process(target=f, args=(processes,))
            pi.start()
        x[i] = '1'
        pi.join()
    except KeyboardInterrupt:
        print("The script has been stoped")
        print(x)


cpu_eat(cpu_count())
#cpu_eat(1)
