from concurrent.futures import ThreadPoolExecutor
import time


def return_after(message, interval):
    time.sleep(interval)
    return message


if __name__ == '__main__':
    pool = ThreadPoolExecutor()
    future = pool.submit(return_after, 'hello!', 2.5)
    print(future.done())
    print(future.result())
    print(future.done())