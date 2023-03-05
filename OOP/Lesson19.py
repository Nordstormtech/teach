class Lesson19:
    def __init__(self, value):
        self.value = value

    def __call__(self, comment):
        print("__call__:", self.value)
        print("comment:", comment)


class Lesson19a:
    def __iter__(self):
        print("__iter__")
        self.arrage = [1, 2, 3]
        return self

    def __next__(self):
        if self.arrage:
            return f"__next__: {self.arrage.pop()}"
        else:
            raise StopIteration("self.arrage - пустой!")


a = Lesson19(10)
#a("test")

b = Lesson19a()
for i in b:
    print(i)