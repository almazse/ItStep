from faker import Faker
import csv
import time
import tracemalloc
from multiprocessing import Pool

fake = Faker()
data = {'people': []}


def single_function(data1):
    for i in range(1, 10001):
        data1['people'].append({
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'user_name': fake.user_name(),
            'password': fake.password(),
            'address': fake.address()
        })

    with open('data.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(['first_name', 'last_name', 'user_name', 'password', 'address']))
        writer.writeheader()
        writer.writerows(data1['people'])

        file.close()


def pool_handler():
    p = Pool()
    p.map(single_function, range(10000))


if __name__ == "__main__":
    tracemalloc.start()
    start = time.time()

    pool_handler()

    print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
    print("ALL done {}".format(time.time()-start))
