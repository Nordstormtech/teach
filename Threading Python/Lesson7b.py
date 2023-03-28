import random
import multiprocessing
import time


def get_text(q):
    val = random.randint(0, 10)
    q.put(str(val))


if __name__ == '__main__':
    pr_list = []
    q = multiprocessing.Queue()
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(q,))
        pr_list.append(pr)
        pr.start()
    for i in pr_list:
        i.join()
    for elem in iter(q.get, None):
        print(elem)


