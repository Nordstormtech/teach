from typing import List, Dict, Optional, Any, Union


def add_number(a: Union[int, float], b: Optional[int] = None) -> int:
    return a + b


def upper_list(lst: List[str]):
    for elem in lst:
        print(elem.upper())


print(add_number(11, 12))
print(add_number([2, 4], [1, 1, 3]))
print(add_number.__annotations__)
upper_list(['sdfgb'])
d: Dict[str, int] = {'f': 112, 'd': 234}
c: Any = 11
c = 'asdc'
print(c)
