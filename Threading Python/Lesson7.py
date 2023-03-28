import multiprocessing

lock = multiprocessing.Lock()


def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f"Процесс [{pr_name}] запущен")


if __name__ == '__main__':
    prc = []
    for i in range(3):
        pr = multiprocessing.Process(target=get_value, args=(lock,), name=f"prc-{i}")
        prc.append(pr)
        pr.start()
    for i in prc:
        i.join()
    print("Процесс завершен")
