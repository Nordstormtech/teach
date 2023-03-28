import time
import random
import threading


def test(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f"Поток [{threading.currentThread().name}] запущен в ({time.ctime()})")

    barrier.wait()

    print(f"Поток [{threading.currentThread().name}] преодолел барьер в ({time.ctime()})")


bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()