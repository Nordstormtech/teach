import multiprocessing
import time


def test():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)


if __name__ == '__main__':
    prc = []
    for i in range(3):
        pr = multiprocessing.Process(target=test, name=f"prc-{i}")
        prc.append(pr)
        pr.start()
    for i in prc:
        i.join()
    print("Процесс завершен")
