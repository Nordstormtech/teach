class Lesson17:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)

    def __bytes__(self):
        return bytes(int(self.value))

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)