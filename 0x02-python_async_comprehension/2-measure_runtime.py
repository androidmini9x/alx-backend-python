#!/usr/bin/env python3
'''Task 2:
2. Run time for four parallel comprehensions
'''


import asyncio
import time


async def measure_runtime() -> float:
    '''
    Measure the total runtime and return it
    '''
    async_comprehension = __import__('1-async_comprehension') \
        .async_comprehension
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
