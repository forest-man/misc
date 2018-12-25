import multiprocessing as mp
import time
from multiprocessing import Pool
from multiprocessing import cpu_count
import threading
import logging

def f(x):
    try:
        while True:
            99999999 * 99999999
    except KeyboardInterrupt:
        print("")
        print("-" * 24)



def cpu_eat_all():
    try:
        if __name__ == '__main__':
            processes = cpu_count()
            print('Running load on CPU')
            print('Utilizing %d core' %processes)
            procs = range(processes)
            map_parameters = range(processes) 
            pool = Pool(processes)
            pool.map(f, map_parameters)
    except KeyboardInterrupt:
        print("Programm has been stoped")

def cpu_eat_one():
    try:
        p = mp.Process(target=f, args=("x"))
        # p.daemon  = True
        p.start()
        time.sleep(10000000)
        p.join()
    except KeyboardInterrupt:
        print("Programm has been stoped")

if __name__ == '__main__':
#    cpu_eat_one()
    cpu_eat_all()
