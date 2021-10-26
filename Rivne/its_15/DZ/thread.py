from faker import Faker
import csv
import time
import tracemalloc
import threading

fake = Faker()
data = {'people': []}


def single_function():
    for i in range(1, 10001):
        data['people'].append({
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'user_name': fake.user_name(),
            'password': fake.password(),
            'address': fake.address()
        })

    with open('data.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(['first_name', 'last_name', 'user_name', 'password', 'address']))
        writer.writeheader()
        writer.writerows(data['people'])

        file.close()

threads = []
tracemalloc.start()
start = time.time()
for item in data:
    thread = threading.Thread(target=single_function)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time()-start))






