import time
import tracemalloc
import logging
import requests
from multiprocessing import Pool


def fetch_url(url):
    try:
        response = requests.get(url)
    except Exception as e:
        logging.info(f'Could not fetch {url}. Error {e}.')
    return response.content


def fetch_all(url_list):
    p = Pool()
    p.map()
    for link in url_list:
        response = fetch_url(link)


if __name__ == '__main__':

    format_logging = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_logging, level=logging.INFO,
                        datefmt="%H:%M:%S")

    test_url = "https://www.google.com/"
    tracemalloc.start()

    for ntimes in [1, 10, 100, 500]:
        start = time.time()
        responses = fetch_all([test_url] * ntimes)
        logging.info(f'Fetch {ntimes} url for {time.time()-start} seconds.')

    print("Current %d, Peak %d" %tracemalloc.get_traced_memory())