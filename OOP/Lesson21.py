import webbrowser


class Lesson21:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        webbrowser.open("https://duckduckgo.com")
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __hash__(self):
        print("__hash__")
        return hash(self.value)

    def __eq__(self, other):
        print("hash:", other)
        return isinstance(other, Lesson21) and self.value == other


a = Lesson21(22)
b = Lesson21(22)
print(a == b)
