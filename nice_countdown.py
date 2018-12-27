import os
import sys
from time import sleep
 
def wait(sec):
    while sec > 0:
        sys.stdout.write(str(sec) + '\r')
        sys.stdout.flush()
        sec -= 1
        sleep(1)
        

