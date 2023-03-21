class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print("in Counter: ", end="")
        return self.func(*args, **kwargs)

    def test(self):
        print("test")


@Counter
def printer():
    print("printer")

printer()
printer()
printer()
printer()
printer.test()
print(printer.count)
