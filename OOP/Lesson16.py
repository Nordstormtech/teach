class Lesson16:
    def __init__(self, value="test"):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.value} {hex(id(self.value))}object>"

    def __del__(self):
        print("Экземпляр класса был удален!")


s = Lesson16()
len(s)
str(s)
print(s)
