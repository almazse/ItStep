import logging
import asyncio


async def connection(router):
    logging.info(f'router {router} connected.')
    await asyncio.sleep(3)


async def commands(router, sem):
    async with sem:
        await connection(router)
        print(f'router {router} command1')
        print(f'router {router} command2')
        print(f'router {router} command3')
        print(f'router {router} closed')
    return f'router {router} completed'


async def main():
    sem = asyncio.Semaphore(3)
    tasks = [asyncio.create_task(commands(router, sem)) for router in range(1, 11)]

    for res in asyncio.as_completed(tasks):
        results = await res
        print(results)


if __name__ == '__main__':
    formatLogging = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatLogging, level=logging.INFO, datefmt="%H:%M:%S")
    asyncio.run(main())
