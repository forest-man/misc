import multiprocessing as mp
import time
from multiprocessing import Pool
from multiprocessing import cpu_count
import threading
import logging
# Make load for the 1-st CPU every time
def f(x):
    try:
        while True:
            99999999 * 99999999
    except KeyboardInterrupt:
        print("")
        print("-" * 24)



def cpu_eat_all(x):

    try:
        if x == 1:
            processes = 1
        elif x == 3:
            processes = cpu_count()

        print('Running load on CPU')
        print('Utilizing %d core' %processes)
        map_parameters = range(processes) 
        pool = Pool(processes)
        pool.map(f, map_parameters)

    except KeyboardInterrupt:
        print("Programm has been stoped")


if __name__ == '__main__':
    cpu_eat_all(3)
