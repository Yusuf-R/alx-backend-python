#!/usr/bin/env python3
""" Async comprenhesion gen """
from typing import List
import asyncio


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    # sourcery skip: inline-immediately-returned-variable
    """
    Coroutine that collects 10 random numbers using an async comprehension.

    Returns:
      A list of 10 random numbers.

    Raises:
      Any error raised by async_generator().
    """
    result = [i async for i in async_generator()]
    return result
