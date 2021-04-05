import os
from time import time
from threading import Thread
DEFAULT_DIRECTORY = r'D:\Desktop\ШАГ'

FILES = []


def find_files(dir):

    for dir_objects in os.listdir(dir):
        dir_objects = os.path.join(dir, dir_objects)
        if os.path.isfile(dir_objects):
            FILES.append(dir_objects)
        elif os.path.isdir(dir_objects):
            find_files(dir_objects)


def find_files_threads(dir):
    for dir_objects in os.listdir(dir):
        dir_objects = os.path.join(dir, dir_objects)
        if os.path.isfile(dir_objects):
            FILES.append(dir_objects)
        elif os.path.isdir(dir_objects):
            t = Thread(target=find_files,
                   args=(dir_objects,))
            t.start()
            t.join()


if __name__ == '__main__':
    # 0.3179936408996582
    start_time = time()
    find_files(DEFAULT_DIRECTORY)
    end_time = time()
    print(end_time-start_time)
    # 0.3210008144378662
    start_time = time()
    find_files(DEFAULT_DIRECTORY)
    end_time = time()
    print(end_time - start_time)
    print(FILES)
