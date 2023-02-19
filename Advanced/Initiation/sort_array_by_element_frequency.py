# Naomi Tesla
# https://py.checkio.org/en/mission/sort-array-by-element-frequency/

from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    container = []
    pos_container = []
    [pos_container.append(item) for item in items if item not in pos_container]
    [container.append([]) for i in range(len(pos_container))]
    for item in items:
        container[pos_container.index(item)].append(item)
    container.sort(key=len, reverse=True)
    return sum(container, [])


assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
    4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]
