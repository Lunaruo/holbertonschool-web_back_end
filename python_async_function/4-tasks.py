#!/usr/bin/env python3
"""Module that runs multiple asyncio tasks concurrently."""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times concurrently and return
    the delays in ascending order.

    Args:
        n: Number of tasks to create.
        max_delay: Maximum delay for each task.

    Returns:
        A list of delays sorted in ascending order.
    """
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        delays.append(await completed_task)

    return delays
