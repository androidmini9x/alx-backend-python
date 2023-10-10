#!/usr/bin/env python3
'''Task 0:
0. Async Generator
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''The coroutine will loop 10 times'''
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
