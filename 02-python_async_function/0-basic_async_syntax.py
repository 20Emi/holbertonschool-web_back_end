#!/usr/bin/env python3
"""Task 0"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay and return the number"""

    num = uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
