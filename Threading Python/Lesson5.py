from threading import Thread, BoundedSemaphore, currentThread
import time
import random

max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    with pool:
        slp = random.randrange(1, 5)
        time.sleep(slp)
        print('end: ', currentThread().name)


for i in range(10):
    Thread(target=test, name=f't{i}').start()
