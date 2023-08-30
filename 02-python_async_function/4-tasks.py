#!/usr/bin/env python3
"""Task 4"""

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)"""

    new_list = []
    for al in range(0, n):
        num = await task_wait_random(max_delay)
        new_list.append(num)
    return sorted(new_list)
