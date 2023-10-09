#!/usr/bin/env python3
'''0. The basics of async
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value
seconds and eventually returns it.
'''


import asyncio
import random


async def wait_random(max_delay: int = 10):
    '''wait and return delayed value'''
    delayed = random.random() * max_delay
    await asyncio.sleep(delay=delayed)
    return delayed
