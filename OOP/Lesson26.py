class Lesson26:
    def __getattr__(self, item):
        print("Вызван не существующий атрибут!")


class Lesson26a:
    # _fields = []

    def __init__(self, *args):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Lesson26b(Lesson26a):
    _fields = ["name", "shares", "price"]


a = Lesson26b(1, 2, 3)
print(getattr(a, "name"))


class Lesson26c:
    def __getattribute__(self, name):
        print("getting:", name)
        return super().__getattribute__(name)


class Lesson26d(Lesson26c):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


c = Lesson26d(11)
print(c.x)
print(c.spam())
