#!/usr/bin/env python3
"""Module containing an asynchronous generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yield 10 random float values between 0 and 10.

    The coroutine waits 1 second before each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
