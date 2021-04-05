# WHILE LOOP

# while условие:
#    тело цикла

import time

counter = 10

if __name__ == '__main__':
    # while counter > 0:
    #     time.sleep(0.5)
    #     print(counter)
    #     counter -= 1
    #
    # print("BOOM!")

    while True:
        print(counter)
        counter -= 1
        if counter == 0:
            break

    print("BOOM!")
