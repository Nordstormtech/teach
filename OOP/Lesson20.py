class Lesson20:
    def __init__(self):
        self.arrage = [1, 2, 3]

    def __enter__(self):
        print("__enter__")
        return self.arrage

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        del self.arrage


a = Lesson20()
with a as arr:
    print(arr[0])


class Lesson20a:
    def __init__(self, filename, flag="r"):
        self.file = open(filename, flag)

    def __enter__(self):
        print("__enter__")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.file.close()


with Lesson20a("test.txt") as file:
    res = file.read()
    print(res)
