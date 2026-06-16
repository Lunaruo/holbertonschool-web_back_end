#!/usr/bin/env python3
"""Module for measuring the runtime of wait_n."""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine.

    Args:
        n: Number of coroutines to execute.
        max_delay: Maximum delay for each coroutine.

    Returns:
        The total execution time divided by n.
    """
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n
