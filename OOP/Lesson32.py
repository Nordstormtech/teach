import sys


class Test:
    pass


def get_version(self):
    return 22


Test.version = get_version
a = Test()
print(a.version())


class ChangeMe:
    def __init__(self):
        local = sys._getframe(1).f_locals
        print(local)
        self.__dict__.update(
            (key, value) for key, value in local.items()
            if callable(value)
        )

b = ChangeMe()
