class Test:
    pass


a = Test()


def get_version():
    return 222


cls_dict = {}
cls_dict["version"] = get_version
cls_dict["name"] = "name"
cls_dict["age"] = 20
new_cls = type("Test1", (), cls_dict)
print(vars(new_cls))


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Невозможно создать экземпляр!")


class Test1(metaclass=NoInstances):
    def test(self):
        print("test")


# b = Test1()
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Test2(metaclass=Singleton):
    def __init__(self):
        print("Test created!")


c = Test2()
v = Test2()
