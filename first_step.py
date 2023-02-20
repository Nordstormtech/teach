class TestClass:
    def get_name(self):
        print("test")


class User:
    name = "Alex"
    age = 17

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)


class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs)


b = B(*[1, 2, 3], **{"name": "name2"})


class Lesson7:
    def __init__(self, name="test"):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


class Lesson8:
    def __init__(self):
        self.value = ""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Lesson8a:
    name = Lesson8()
    surname = Lesson8()


test = Lesson8a()


class Lesson9:
    def __init__(self, name="name1", age=20):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def get_sum(x, y):
        print(x + y)


print(Lesson9.get_sum(1, 3))


class Lesson10:
    __slots__ = ["name", "age"]

    def __init__(self, name="name1", age=20):
        self.name = name
        self.age = age


class Lesson11:
    def __new__(cls, *args, **kwargs):
        print("создаем экземпляр")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        self.name = name


a = Lesson11.__new__(Lesson11)


class Lesson12:
    def __init__(self, name="name1"):
        self.name = name

    @classmethod
    def set_name(cls, value):
        cls.version = value


f = Lesson12()
f.set_name(3)


class Lesson13:
    __slots__ = ["__name"]

    def __init__(self, name="name1"):
        self.__name = name


class Lesson13a:
    def __init__(self, name="name1"):
        self._name = name

    def get(self):
        return self._name


class Lesson14:
    args = {
        "version": 1,
        "flag": 2
    }

    def __init__(self):
        self.__dict__ = self.args


from functools import singledispatch


class Lesson15:
    @singledispatch
    def get_value(value):
        print("default:", value)

    @get_value.register(int)
    def _(value):
        print("int:", value)

    @get_value.register(str)
    def _(value):
        print("str:", value)


class Lesson16:
    def __init__(self, value="test"):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.value} {hex(id(self.value))}object>"

    def __del__(self):
        print("Экземпляр класса был удален!")

s = Lesson16()
len(s)
str(s)
print(s)
s
