# Naomi Tesla
# https://py.checkio.org/en/mission/flatten-list/

from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    return [int(x) for x in str(array).replace(
        '[', '').replace(']', '').replace(',', '').split(None)] if any(char.isdigit() for char in str(array)) else []


assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]