#!/usr/bin/env python3
"""Task 1"""


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)"""

    new_list = []
    for al in range(0, n):
        num = await wait_random(max_delay)
        new_list.append(num)
    return sorted(new_list)
