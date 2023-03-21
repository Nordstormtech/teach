from abc import ABCMeta, abstractmethod


class Users(metaclass=ABCMeta):
    @abstractmethod
    def go_to(self):
        pass

    @abstractmethod
    def read(self):
        pass


class Test(Users):
    def go_to(self):
        print("go_to")

    def read(self):
        print("read")
