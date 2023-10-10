#!/usr/bin/env python3
'''Task 1:
1. Async Comprehensions
'''


from typing import List


async def async_comprehension() -> List[float]:
    '''
    collect 10 random numbers using an async comprehensing
    over async_generator
    '''
    async_generator = __import__('0-async_generator').async_generator
    list_comp = [x async for x in async_generator()]
    return list_comp
