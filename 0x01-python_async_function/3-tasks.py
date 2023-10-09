#!/usr/bin/env python3
'''3. Tasks:
Write a function that takes an integer max_delay and returns a asyncio.Task.
'''


import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''returns a asyncio.Task'''
    wait_random = __import__('0-basic_async_syntax').wait_random
    res = asyncio.create_task(wait_random(max_delay))
    return res
