from functools import singledispatch


class Lesson15:
    @singledispatch
    def get_value(value):
        print("default:", value)

    @get_value.register(int)
    def _(value):
        print("int:", value)

    @get_value.register(str)
    def _(value):
        print("str:", value)
