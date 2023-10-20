#!/usr/bin/env python3
""" Execute multiple coroutine at the same time with a sync """
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for `n` iterations, then returns a list of the delays.

    Args:
    - n (int): The number of iterations to wait for.
    - max_delay (int): The maximum delay (in seconds) for each iteration.

    Returns:
    - A list of the delays (in seconds) for each iteration.
    """
    delays: List[float] = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays.sort()
    return delays
