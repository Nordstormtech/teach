class Lesson27(dict):
    def __setitem__(self, key, value):
        print("__setitem__")
        super().__setitem__(key, [value] * 3)

    def __getitem__(self, key):
        print("__getitem__")
        return super().__getitem__(key)


res = Lesson27(one=1, two=2)
print("class:", res)
print(res["one"])
print(res)
res["two"] = 3
print("class:", res)
