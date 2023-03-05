class Lesson11:
    def __new__(cls, *args, **kwargs):
        print("создаем экземпляр")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        self.name = name


a = Lesson11.__new__(Lesson11)