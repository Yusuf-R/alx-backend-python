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
    sorted_delays: List[float] = []
    each_task: List = []

    # get the list of time it takes for each callable
    for _ in range(n):
        each_task.append(wait_random(max_delay))

    # get the sorted list
    for task in asyncio.as_completed(each_task):
        sorted_delays.append(await task)
    return sorted_delays
