class Lesson18:
    def __init__(self, value):
        self.value = value
        self.arrage = [1, 2, 3]

    def __pow__(self, power, modulo=None):  # возведение в степень
        return self.value ** power

    def __reversed__(self):  # переворачивает список
        self.arrage.reverse()
        return self.arrage

    def __truediv__(self, other):
        return int(self.value / other)


a = Lesson18(10)
