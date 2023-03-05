class Lesson12:
    def __init__(self, name="name1"):
        self.name = name

    @classmethod
    def set_name(cls, value):
        cls.version = value


f = Lesson12()
f.set_name(3)