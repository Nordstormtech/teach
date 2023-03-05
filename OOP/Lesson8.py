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