import time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(5)


thr_list = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i), name=f"thr-{i}")
    thr_list.append(thr)
    thr.start()
print(thr_list)

for i in thr_list:
    i.join()

print("Готово")
# for i in range(100):
#    print(f"current {i}")
#
#    time.sleep(1)
#
#   if i % 10 == 0:
#        print("active thread:", threading.active_count())
#        print("enumerate:", threading.enumerate())
#        print("thr-1 is alive:", thr.is_alive())
