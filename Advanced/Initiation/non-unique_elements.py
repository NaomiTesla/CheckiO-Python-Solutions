# Naomi Tesla
# https://py.checkio.org/en/mission/non-unique-elements/
# Not the most efficient but I kinda just wanted to do it from scratch without importing 3rd party stufffff :3


from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    occurence_count = {}

    for item in data:
        occurence_count[item] = occurence_count.get(item, 0) + 1

    for item, count in occurence_count.items():
        if count == 1:
            data.pop(data.index(item))

    return data


assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]
