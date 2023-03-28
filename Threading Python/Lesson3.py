import time
import threading

value = 0
locker = threading.Lock()


def inc_value():
    global value
    while True:
        with locker:
            value += 1
            time.sleep(0.01)
            print(value)



for _ in range(5):
    threading.Thread(target=inc_value).start()
