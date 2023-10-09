#!/usr/bin/env python3
'''4. Tasks:
The code is nearly identical to wait_n except task_wait_random is being called.
'''


import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return list of all the delays'''
    task_wait_random = __import__('3-tasks').task_wait_random
    res = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(res)
