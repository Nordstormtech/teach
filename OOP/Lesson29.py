class Lesson29:
    version = "1.0"

    def get_version(self):
        return self.version


# print(vars(Lesson29)) # тоже самое что дикт
# print(Lesson29.__dict__)
for key in vars(Lesson29):
    attr_value = vars(Lesson29)[key]
    if callable(attr_value):
        print(f"{key} - вызываемый!")
    else:
        print(f"{key} - не вызываемый!")


class Lesson29a:
    def __init__(self, name):
        self.name = name

    def get(self):
        print("test")


class Lesson29c:
    def __init__(self, age):
        self.age = age

    def get(self):
        print("test2")


class Lesson29b(Lesson29a, Lesson29c):
    def __init__(self, version):
        self.version = version
        Lesson29a.__init__(self, "name")
        Lesson29c.__init__(self, 100)


a = Lesson29b("Pass")
print(vars(a))
a.get()

print(Lesson29b.mro())  # проверка наследования
