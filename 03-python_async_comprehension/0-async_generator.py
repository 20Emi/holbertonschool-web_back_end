#!/usr/bin/env python3
"""Task 0"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yield a random number between 0 and 10"""

    for rand in range(0, 10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
