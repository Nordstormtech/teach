class Lesson23:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other


a = Lesson23(3)
print(a * 5)


class Lesson23a:
    def __init__(self, arrage=[1, 2, 3]):
        self.arrage = arrage

    def __getitem__(self, index):
        return self.arrage[index]

    def __setitem__(self, index, value):
        self.arrage[index] = value
        print("Значение записано!")

    def __delitem__(self, index):
        del self.arrage[index]
        print("Значение удалено!")


b = Lesson23a()
print(b.arrage[0])
b[0] = 111
print(b.arrage[0])
del b[2]
print(b.arrage)
