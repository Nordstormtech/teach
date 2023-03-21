from typing import Any
from dataclasses import dataclass


@dataclass
class User:
    name: str = "name"
    age: int = "age"
    flags: list = "list"
    comment: Any = "Any"


class Test(User):
    def get_name(self):
        return self.name


a = Test(
    name="Name",
    age=17,
    flags=[1, 2, 3],
    comment=True
)
print(a.get_name())