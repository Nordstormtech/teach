class Lesson13:
    __slots__ = ["__name"]

    def __init__(self, name="name1"):
        self.__name = name


class Lesson13a:
    def __init__(self, name="name1"):
        self._name = name

    def get(self):
        return self._name
