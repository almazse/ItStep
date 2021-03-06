import asyncio
import concurrent.futures
import logging
import time
import sys


def block(n):
    log = logging.getLogger(f'bloc {n}')
    log.info('block is running')
    time.sleep(1)
    log.info('block was finished')
    return n ** 2


async def running_blocks(executor_blocks):
    log = logging.getLogger('run_blocks')
    log.info('run_block starting')

    log.info('executor was created')
    loop = asyncio.get_event_loop()
    block_tasks = [loop.run_in_executor(executor_blocks, block, i) for i in range(1, 11)]
    log.info('waiting for executor tasks')
    completed, _ = await asyncio.wait(block_tasks)
    results = [task.results() for task in completed]
    log.info(f'results {results}')

    log.info('run_block finished')


if __name__ == '__main__':
    formatLogging = "PID %(process)5s %(name)s: %(message)s"
    logging.basicConfig(format=formatLogging, level=logging.INFO, stream=sys.stderr)

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(running_blocks(executor))
    finally:
        event_loop.close()
