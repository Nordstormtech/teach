class Lesson22:
    def __init__(self, value):
        self.value = value


a = Lesson22(11)
print(hasattr(a, "value"))
print(getattr(Lesson22, "value", None))
print(getattr(a, "value"))
