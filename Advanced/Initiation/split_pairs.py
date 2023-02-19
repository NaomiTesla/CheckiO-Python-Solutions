# Naomi Tesla
# https://py.checkio.org/en/mission/split-pairs/

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    pairs = []
    if len(text) % 2:
        text += '_'
    steps = len(text)//2
    n = 0
    while n < steps:
        pairs.append(text[:2])
        text = text[2:]
        n += 1
    return pairs

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []
