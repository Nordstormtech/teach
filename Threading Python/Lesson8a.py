import multiprocessing
import random


def end_func(response):
    print("end_func:", response)


def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return x, y, z


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        # если метод принимает только одну переменную
        # for i in range(10):
        #    p.apply_async(out, args=(i,), callback=end_func)
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        p.close()
        p.join()
