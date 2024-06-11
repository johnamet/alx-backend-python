#!/usr/bin/env python3
"""The module contains coroutines for concurrent tasks."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Waits n times."""

    tasks = [asyncio.create_task(wait_random(n, max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
