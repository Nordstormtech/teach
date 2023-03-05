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
