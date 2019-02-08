#!/usr/bin/env python

import time
import argparse

def mem_cons(n):
    try:
        GB = 1024*1024*1024
        a = "a" * (n * GB)
        time.sleep(100000)
    except KeyboardInterrupt:
        pass

parser = argparse.ArgumentParser()
parser.add_argument("mem", help="Select mode amount of memory to consume", type=int, default=None)
args = parser.parse_args()

mem_cons(args.mem)


