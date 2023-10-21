#!/usr/bin/env python3
""" Measure times """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    Asynchronously measures the runtime of a function.

    - This function uses the `asyncio.gather()`function to concurrently execute
    the `async_comprehension()` function multiple times.
    - It creates a list comprehension that repeats the
    `async_comprehension()` function 4 times.
    - The `asyncio.gather()` function is then used to execute all
    the `async_comprehension()` instances concurrently.

    Returns:
        A list of results from executing the
        `async_comprehension()` function 4 times concurrently.

    Raises:
        Any exceptions raised by the `async_comprehension()` function.

    Example Usage:
        result = await measure_runtime()
    """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    stop_time = time.perf_counter()
    return stop_time - start_time
