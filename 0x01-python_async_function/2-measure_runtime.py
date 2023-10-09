#!/usr/bin/env python3
'''2. Measure the runtime
'''


import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    '''return measured execution time'''
    wait_n = __import__('1-concurrent_coroutines').wait_n
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
