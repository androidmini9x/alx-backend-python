#!/usr/bin/env python3
'''Task 0:
0. Async Generator
'''


import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    '''The coroutine will loop 10 times'''
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
