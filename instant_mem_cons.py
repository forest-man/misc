#!/usr/bin/env python
try:
    GB = 1024*1024*1024
    a = "a" * (2 * GB)
except MemoryError:
    pass

