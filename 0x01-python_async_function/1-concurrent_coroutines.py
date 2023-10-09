#!/usr/bin/env python3
'''Task: 0x01
1. Let's execute multiple coroutines at the same time with async
'''


import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return list of all the delays'''
    wait_random = __import__('0-basic_async_syntax').wait_random
    res = await asyncio.gather(*(wait_random(max_delay) for x in range(n)))
    return sorted(res)
