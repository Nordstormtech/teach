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