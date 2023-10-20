#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the wait_n function.
    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to wait_random.
    Returns:
        float: The average runtime of wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.perf_counter() - start_time
    return stop_time / n
