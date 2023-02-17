# Naomi Tesla
# https://py.checkio.org/en/mission/all-the-same/

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 1:
        return True
    palindrome = sorted(''.join(str(c) for c in elements))
    if palindrome == palindrome[::-1]:
        return True
    return False

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True
