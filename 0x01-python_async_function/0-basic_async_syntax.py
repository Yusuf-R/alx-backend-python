#!/usr/bin/env python3

# Write a coroutine called async_generator that takes no arguments.

# The coroutine will loop 10 times, each time asynchronously wait 1 second,
# then yield a random number between 0 and 10. Use the random module.

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yield a random integer between 0 and 10 asynchronously, 10 times.

    This coroutine function simulates some asynchronous
    work by sleeping for 1 second between each yield statement.

    Yields:
      float: a random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Simulate some asynchronous work
        yield random.uniform(0, 10)
